from ast import NodeVisitor, AST
from collections.abc import Sequence
import inspect
import importlib

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
    def __init__(self, nodes, ast=None, safe_parsing=True):
        """Wrapper to instantiate and use a Selector using node names."""
        self.nodes = nodes
        self.ast = ast
        self.safe_parsing = safe_parsing

        self.ParseError = getattr(self.ast, 'ParseError', None) or \
                          getattr(self.ast, 'AntlrException', None)

    def __call__(self, name, index, node, *args, **kwargs):
        # TODO: gentle error handling
        ast_cls = self.nodes[name]

        selector = Selector(ast_cls, *args, **kwargs)
        selector.visit(node, head=True)

        return selector.out[index]

    def parse(self, code):
        # AST modules should define exception as ParseError, but use AntlrException
        # for backwards compatibility
        try:
            return self.ast.parse(code, strict=True)
        except self.ParseError as e:
            if self.safe_parsing: return e
            else: raise e

    def describe(self, node, msg, field = "", **kwargs):
        speaker = getattr(self.ast, 'speaker', None)

        has_index = kwargs.get('index') is not None
        if has_index: 
            phrase = "{} entry in the " if field else "{} "
            kwargs['index'] = phrase.format(get_ord(kwargs['index'] + 1))
        else: 
            kwargs['index'] = ""

        if speaker:
            return self.ast.speaker.describe(node, field = field, 
                                             fmt = msg, **kwargs)

    @classmethod
    def from_module(cls, mod):
        if isinstance(mod, str): mod = importlib.import_module(mod)

        ast_nodes = {k: v for k, v in vars(mod).items() if (inspect.isclass(v) and issubclass(v, mod.AstNode))}
        dispatcher = cls(ast_nodes, ast=mod)
        return dispatcher

def get_ord(num):
    assert num != 0, "use strictly positive numbers in get_ord()"
    nums = {1: "first", 2: "second", 3:"third", 4:"fourth",
            5: "fifth", 6: "sixth", 7:"seventh", 8:"eight",
            9: "ninth", 10: "tenth"}
    if num in nums:
        return(nums[num])
    else:
        return("%dth" % num)
