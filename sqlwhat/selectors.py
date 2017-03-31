from ast import NodeVisitor, AST
from collections.abc import Sequence
import inspect

import importlib
def get_ast_parser(dialect_name):
    mod_map = {
            'postgresql': 'antlr_plsql.ast', 
            'sqlite': 'antlr_plsql.ast',        # uses postgres parser for now
            'mssql': 'antlr_tsql.ast'}

    ast_parser = importlib.import_module(mod_map[dialect_name])
    return ast_parser

class Selector(NodeVisitor):

    def __init__(self, src, priority = None):
        self.src = src
        self.priority = src._priority if priority is None else priority
        self.out = []

    # TODO: needed to repeat this function, since _fields is more complex on the
    #       custom ASTs, should simplify _fields, so this can be removed..
    @staticmethod
    def iter_fields(node): 
        return [(k, getattr(node, k)) for k in node._get_field_names() if hasattr(node, k)]

    def generic_visit(self, node):
        """Called if no explicit visitor function exists for a node."""
        for field, value in self.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, AST):
                        self.visit(item)
            elif isinstance(value, AST):
                self.visit(value)

    def visit(self, node, head=False):
        if head: return super().visit(node)

        if self.is_match(node): self.out.append(node)
        if self.has_priority_over(node):
            return super().visit(node)

    def visit_list(self, lst):
        for item in lst: self.visit(item)

    def is_match(self, node):
        if type(node) is self.src: return True
        else: return False

    def has_priority_over(self, node):
        return self.priority > node._priority

class Dispatcher:
    def __init__(self, nodes, rules, ast=None, safe_parsing=True):
        """Wrapper to instantiate and use a Selector using node names."""
        self.types = {}
        self.ast = ast
        self.safe_parsing = safe_parsing

        for name, funcs in rules.items():
            pred, map_name = funcs if len(funcs) == 2 else funcs + None

            self.types[name] = self.get(nodes, pred, map_name)

    def __call__(self, check, name, index, node, *args, **kwargs):
        # TODO: gentle error handling
        ast_cls = self.types[check][name]

        selector = Selector(ast_cls, *args, **kwargs)
        selector.visit(node, head=True)

        return selector.out[index]

    def parse(self, code):
        try:
            return self.ast.parse(code, strict=True)
        except self.ast.AntlrException as e:
            if self.safe_parsing: return e
            else: raise e

    @staticmethod
    def get(nodes, predicate, map_name = lambda x: x):
        return {map_name(k): v for k, v in nodes.items() if predicate(k, v)}

    @classmethod
    def from_module(cls, mod, rules):
        ast_nodes = {k: v for k, v in vars(mod).items() if (inspect.isclass(v) and issubclass(v, mod.AstNode))}
        dispatcher = cls(ast_nodes, rules, ast=mod)
        return dispatcher

    @classmethod
    def from_dialect(cls, dialect_name):
        rules = {
                "statement":     [lambda k, v: "Stmt" in k,     lambda k: k.replace("Stmt", "").lower()],
                "other":         [lambda k, v: "Stmt" not in k, lambda k: k.lower()],
                "node":          [lambda k, v: True,            lambda k: k]
                }

        ast_parser = get_ast_parser(dialect_name)
        
        # TODO: the code below monkney patches the mssql ast to use only lowercase
        #       representations. This is because msft server has a setting to be
        #       case sensitive. However, this is often not the case, and probably
        #       detremental to DataCamp courses. Need to move to more sane configuration.
        if dialect_name == 'mssql':
            ast_parser.AstNode.__repr__ = lower_case(ast_parser.AstNode.__repr__)

        return cls.from_module(ast_parser, rules)

from functools import wraps
def lower_case(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs).lower()
    return wrapper

