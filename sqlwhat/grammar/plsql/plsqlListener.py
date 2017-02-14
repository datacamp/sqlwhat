# Generated from sqlwhat/grammar/plsql/plsql.g4 by ANTLR 4.6.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .plsqlParser import plsqlParser
else:
    from plsqlParser import plsqlParser

# This class defines a complete listener for a parse tree produced by plsqlParser.
class plsqlListener(ParseTreeListener):

    # Enter a parse tree produced by plsqlParser#swallow_to_semi.
    def enterSwallow_to_semi(self, ctx:plsqlParser.Swallow_to_semiContext):
        pass

    # Exit a parse tree produced by plsqlParser#swallow_to_semi.
    def exitSwallow_to_semi(self, ctx:plsqlParser.Swallow_to_semiContext):
        pass


    # Enter a parse tree produced by plsqlParser#compilation_unit.
    def enterCompilation_unit(self, ctx:plsqlParser.Compilation_unitContext):
        pass

    # Exit a parse tree produced by plsqlParser#compilation_unit.
    def exitCompilation_unit(self, ctx:plsqlParser.Compilation_unitContext):
        pass


    # Enter a parse tree produced by plsqlParser#sql_script.
    def enterSql_script(self, ctx:plsqlParser.Sql_scriptContext):
        pass

    # Exit a parse tree produced by plsqlParser#sql_script.
    def exitSql_script(self, ctx:plsqlParser.Sql_scriptContext):
        pass


    # Enter a parse tree produced by plsqlParser#unit_statement.
    def enterUnit_statement(self, ctx:plsqlParser.Unit_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#unit_statement.
    def exitUnit_statement(self, ctx:plsqlParser.Unit_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#drop_function.
    def enterDrop_function(self, ctx:plsqlParser.Drop_functionContext):
        pass

    # Exit a parse tree produced by plsqlParser#drop_function.
    def exitDrop_function(self, ctx:plsqlParser.Drop_functionContext):
        pass


    # Enter a parse tree produced by plsqlParser#alter_function.
    def enterAlter_function(self, ctx:plsqlParser.Alter_functionContext):
        pass

    # Exit a parse tree produced by plsqlParser#alter_function.
    def exitAlter_function(self, ctx:plsqlParser.Alter_functionContext):
        pass


    # Enter a parse tree produced by plsqlParser#create_function_body.
    def enterCreate_function_body(self, ctx:plsqlParser.Create_function_bodyContext):
        pass

    # Exit a parse tree produced by plsqlParser#create_function_body.
    def exitCreate_function_body(self, ctx:plsqlParser.Create_function_bodyContext):
        pass


    # Enter a parse tree produced by plsqlParser#parallel_enable_clause.
    def enterParallel_enable_clause(self, ctx:plsqlParser.Parallel_enable_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#parallel_enable_clause.
    def exitParallel_enable_clause(self, ctx:plsqlParser.Parallel_enable_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#partition_by_clause.
    def enterPartition_by_clause(self, ctx:plsqlParser.Partition_by_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#partition_by_clause.
    def exitPartition_by_clause(self, ctx:plsqlParser.Partition_by_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#result_cache_clause.
    def enterResult_cache_clause(self, ctx:plsqlParser.Result_cache_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#result_cache_clause.
    def exitResult_cache_clause(self, ctx:plsqlParser.Result_cache_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#relies_on_part.
    def enterRelies_on_part(self, ctx:plsqlParser.Relies_on_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#relies_on_part.
    def exitRelies_on_part(self, ctx:plsqlParser.Relies_on_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#streaming_clause.
    def enterStreaming_clause(self, ctx:plsqlParser.Streaming_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#streaming_clause.
    def exitStreaming_clause(self, ctx:plsqlParser.Streaming_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#drop_package.
    def enterDrop_package(self, ctx:plsqlParser.Drop_packageContext):
        pass

    # Exit a parse tree produced by plsqlParser#drop_package.
    def exitDrop_package(self, ctx:plsqlParser.Drop_packageContext):
        pass


    # Enter a parse tree produced by plsqlParser#alter_package.
    def enterAlter_package(self, ctx:plsqlParser.Alter_packageContext):
        pass

    # Exit a parse tree produced by plsqlParser#alter_package.
    def exitAlter_package(self, ctx:plsqlParser.Alter_packageContext):
        pass


    # Enter a parse tree produced by plsqlParser#create_package.
    def enterCreate_package(self, ctx:plsqlParser.Create_packageContext):
        pass

    # Exit a parse tree produced by plsqlParser#create_package.
    def exitCreate_package(self, ctx:plsqlParser.Create_packageContext):
        pass


    # Enter a parse tree produced by plsqlParser#package_body.
    def enterPackage_body(self, ctx:plsqlParser.Package_bodyContext):
        pass

    # Exit a parse tree produced by plsqlParser#package_body.
    def exitPackage_body(self, ctx:plsqlParser.Package_bodyContext):
        pass


    # Enter a parse tree produced by plsqlParser#package_spec.
    def enterPackage_spec(self, ctx:plsqlParser.Package_specContext):
        pass

    # Exit a parse tree produced by plsqlParser#package_spec.
    def exitPackage_spec(self, ctx:plsqlParser.Package_specContext):
        pass


    # Enter a parse tree produced by plsqlParser#package_obj_spec.
    def enterPackage_obj_spec(self, ctx:plsqlParser.Package_obj_specContext):
        pass

    # Exit a parse tree produced by plsqlParser#package_obj_spec.
    def exitPackage_obj_spec(self, ctx:plsqlParser.Package_obj_specContext):
        pass


    # Enter a parse tree produced by plsqlParser#procedure_spec.
    def enterProcedure_spec(self, ctx:plsqlParser.Procedure_specContext):
        pass

    # Exit a parse tree produced by plsqlParser#procedure_spec.
    def exitProcedure_spec(self, ctx:plsqlParser.Procedure_specContext):
        pass


    # Enter a parse tree produced by plsqlParser#function_spec.
    def enterFunction_spec(self, ctx:plsqlParser.Function_specContext):
        pass

    # Exit a parse tree produced by plsqlParser#function_spec.
    def exitFunction_spec(self, ctx:plsqlParser.Function_specContext):
        pass


    # Enter a parse tree produced by plsqlParser#package_obj_body.
    def enterPackage_obj_body(self, ctx:plsqlParser.Package_obj_bodyContext):
        pass

    # Exit a parse tree produced by plsqlParser#package_obj_body.
    def exitPackage_obj_body(self, ctx:plsqlParser.Package_obj_bodyContext):
        pass


    # Enter a parse tree produced by plsqlParser#drop_procedure.
    def enterDrop_procedure(self, ctx:plsqlParser.Drop_procedureContext):
        pass

    # Exit a parse tree produced by plsqlParser#drop_procedure.
    def exitDrop_procedure(self, ctx:plsqlParser.Drop_procedureContext):
        pass


    # Enter a parse tree produced by plsqlParser#alter_procedure.
    def enterAlter_procedure(self, ctx:plsqlParser.Alter_procedureContext):
        pass

    # Exit a parse tree produced by plsqlParser#alter_procedure.
    def exitAlter_procedure(self, ctx:plsqlParser.Alter_procedureContext):
        pass


    # Enter a parse tree produced by plsqlParser#create_procedure_body.
    def enterCreate_procedure_body(self, ctx:plsqlParser.Create_procedure_bodyContext):
        pass

    # Exit a parse tree produced by plsqlParser#create_procedure_body.
    def exitCreate_procedure_body(self, ctx:plsqlParser.Create_procedure_bodyContext):
        pass


    # Enter a parse tree produced by plsqlParser#drop_trigger.
    def enterDrop_trigger(self, ctx:plsqlParser.Drop_triggerContext):
        pass

    # Exit a parse tree produced by plsqlParser#drop_trigger.
    def exitDrop_trigger(self, ctx:plsqlParser.Drop_triggerContext):
        pass


    # Enter a parse tree produced by plsqlParser#alter_trigger.
    def enterAlter_trigger(self, ctx:plsqlParser.Alter_triggerContext):
        pass

    # Exit a parse tree produced by plsqlParser#alter_trigger.
    def exitAlter_trigger(self, ctx:plsqlParser.Alter_triggerContext):
        pass


    # Enter a parse tree produced by plsqlParser#create_trigger.
    def enterCreate_trigger(self, ctx:plsqlParser.Create_triggerContext):
        pass

    # Exit a parse tree produced by plsqlParser#create_trigger.
    def exitCreate_trigger(self, ctx:plsqlParser.Create_triggerContext):
        pass


    # Enter a parse tree produced by plsqlParser#trigger_follows_clause.
    def enterTrigger_follows_clause(self, ctx:plsqlParser.Trigger_follows_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#trigger_follows_clause.
    def exitTrigger_follows_clause(self, ctx:plsqlParser.Trigger_follows_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#trigger_when_clause.
    def enterTrigger_when_clause(self, ctx:plsqlParser.Trigger_when_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#trigger_when_clause.
    def exitTrigger_when_clause(self, ctx:plsqlParser.Trigger_when_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#simple_dml_trigger.
    def enterSimple_dml_trigger(self, ctx:plsqlParser.Simple_dml_triggerContext):
        pass

    # Exit a parse tree produced by plsqlParser#simple_dml_trigger.
    def exitSimple_dml_trigger(self, ctx:plsqlParser.Simple_dml_triggerContext):
        pass


    # Enter a parse tree produced by plsqlParser#for_each_row.
    def enterFor_each_row(self, ctx:plsqlParser.For_each_rowContext):
        pass

    # Exit a parse tree produced by plsqlParser#for_each_row.
    def exitFor_each_row(self, ctx:plsqlParser.For_each_rowContext):
        pass


    # Enter a parse tree produced by plsqlParser#compound_dml_trigger.
    def enterCompound_dml_trigger(self, ctx:plsqlParser.Compound_dml_triggerContext):
        pass

    # Exit a parse tree produced by plsqlParser#compound_dml_trigger.
    def exitCompound_dml_trigger(self, ctx:plsqlParser.Compound_dml_triggerContext):
        pass


    # Enter a parse tree produced by plsqlParser#non_dml_trigger.
    def enterNon_dml_trigger(self, ctx:plsqlParser.Non_dml_triggerContext):
        pass

    # Exit a parse tree produced by plsqlParser#non_dml_trigger.
    def exitNon_dml_trigger(self, ctx:plsqlParser.Non_dml_triggerContext):
        pass


    # Enter a parse tree produced by plsqlParser#trigger_body.
    def enterTrigger_body(self, ctx:plsqlParser.Trigger_bodyContext):
        pass

    # Exit a parse tree produced by plsqlParser#trigger_body.
    def exitTrigger_body(self, ctx:plsqlParser.Trigger_bodyContext):
        pass


    # Enter a parse tree produced by plsqlParser#routine_clause.
    def enterRoutine_clause(self, ctx:plsqlParser.Routine_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#routine_clause.
    def exitRoutine_clause(self, ctx:plsqlParser.Routine_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#compound_trigger_block.
    def enterCompound_trigger_block(self, ctx:plsqlParser.Compound_trigger_blockContext):
        pass

    # Exit a parse tree produced by plsqlParser#compound_trigger_block.
    def exitCompound_trigger_block(self, ctx:plsqlParser.Compound_trigger_blockContext):
        pass


    # Enter a parse tree produced by plsqlParser#timing_point_section.
    def enterTiming_point_section(self, ctx:plsqlParser.Timing_point_sectionContext):
        pass

    # Exit a parse tree produced by plsqlParser#timing_point_section.
    def exitTiming_point_section(self, ctx:plsqlParser.Timing_point_sectionContext):
        pass


    # Enter a parse tree produced by plsqlParser#non_dml_event.
    def enterNon_dml_event(self, ctx:plsqlParser.Non_dml_eventContext):
        pass

    # Exit a parse tree produced by plsqlParser#non_dml_event.
    def exitNon_dml_event(self, ctx:plsqlParser.Non_dml_eventContext):
        pass


    # Enter a parse tree produced by plsqlParser#dml_event_clause.
    def enterDml_event_clause(self, ctx:plsqlParser.Dml_event_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#dml_event_clause.
    def exitDml_event_clause(self, ctx:plsqlParser.Dml_event_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#dml_event_element.
    def enterDml_event_element(self, ctx:plsqlParser.Dml_event_elementContext):
        pass

    # Exit a parse tree produced by plsqlParser#dml_event_element.
    def exitDml_event_element(self, ctx:plsqlParser.Dml_event_elementContext):
        pass


    # Enter a parse tree produced by plsqlParser#dml_event_nested_clause.
    def enterDml_event_nested_clause(self, ctx:plsqlParser.Dml_event_nested_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#dml_event_nested_clause.
    def exitDml_event_nested_clause(self, ctx:plsqlParser.Dml_event_nested_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#referencing_clause.
    def enterReferencing_clause(self, ctx:plsqlParser.Referencing_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#referencing_clause.
    def exitReferencing_clause(self, ctx:plsqlParser.Referencing_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#referencing_element.
    def enterReferencing_element(self, ctx:plsqlParser.Referencing_elementContext):
        pass

    # Exit a parse tree produced by plsqlParser#referencing_element.
    def exitReferencing_element(self, ctx:plsqlParser.Referencing_elementContext):
        pass


    # Enter a parse tree produced by plsqlParser#drop_type.
    def enterDrop_type(self, ctx:plsqlParser.Drop_typeContext):
        pass

    # Exit a parse tree produced by plsqlParser#drop_type.
    def exitDrop_type(self, ctx:plsqlParser.Drop_typeContext):
        pass


    # Enter a parse tree produced by plsqlParser#alter_type.
    def enterAlter_type(self, ctx:plsqlParser.Alter_typeContext):
        pass

    # Exit a parse tree produced by plsqlParser#alter_type.
    def exitAlter_type(self, ctx:plsqlParser.Alter_typeContext):
        pass


    # Enter a parse tree produced by plsqlParser#compile_type_clause.
    def enterCompile_type_clause(self, ctx:plsqlParser.Compile_type_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#compile_type_clause.
    def exitCompile_type_clause(self, ctx:plsqlParser.Compile_type_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#replace_type_clause.
    def enterReplace_type_clause(self, ctx:plsqlParser.Replace_type_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#replace_type_clause.
    def exitReplace_type_clause(self, ctx:plsqlParser.Replace_type_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#alter_method_spec.
    def enterAlter_method_spec(self, ctx:plsqlParser.Alter_method_specContext):
        pass

    # Exit a parse tree produced by plsqlParser#alter_method_spec.
    def exitAlter_method_spec(self, ctx:plsqlParser.Alter_method_specContext):
        pass


    # Enter a parse tree produced by plsqlParser#alter_method_element.
    def enterAlter_method_element(self, ctx:plsqlParser.Alter_method_elementContext):
        pass

    # Exit a parse tree produced by plsqlParser#alter_method_element.
    def exitAlter_method_element(self, ctx:plsqlParser.Alter_method_elementContext):
        pass


    # Enter a parse tree produced by plsqlParser#alter_attribute_definition.
    def enterAlter_attribute_definition(self, ctx:plsqlParser.Alter_attribute_definitionContext):
        pass

    # Exit a parse tree produced by plsqlParser#alter_attribute_definition.
    def exitAlter_attribute_definition(self, ctx:plsqlParser.Alter_attribute_definitionContext):
        pass


    # Enter a parse tree produced by plsqlParser#attribute_definition.
    def enterAttribute_definition(self, ctx:plsqlParser.Attribute_definitionContext):
        pass

    # Exit a parse tree produced by plsqlParser#attribute_definition.
    def exitAttribute_definition(self, ctx:plsqlParser.Attribute_definitionContext):
        pass


    # Enter a parse tree produced by plsqlParser#alter_collection_clauses.
    def enterAlter_collection_clauses(self, ctx:plsqlParser.Alter_collection_clausesContext):
        pass

    # Exit a parse tree produced by plsqlParser#alter_collection_clauses.
    def exitAlter_collection_clauses(self, ctx:plsqlParser.Alter_collection_clausesContext):
        pass


    # Enter a parse tree produced by plsqlParser#dependent_handling_clause.
    def enterDependent_handling_clause(self, ctx:plsqlParser.Dependent_handling_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#dependent_handling_clause.
    def exitDependent_handling_clause(self, ctx:plsqlParser.Dependent_handling_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#dependent_exceptions_part.
    def enterDependent_exceptions_part(self, ctx:plsqlParser.Dependent_exceptions_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#dependent_exceptions_part.
    def exitDependent_exceptions_part(self, ctx:plsqlParser.Dependent_exceptions_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#create_type.
    def enterCreate_type(self, ctx:plsqlParser.Create_typeContext):
        pass

    # Exit a parse tree produced by plsqlParser#create_type.
    def exitCreate_type(self, ctx:plsqlParser.Create_typeContext):
        pass


    # Enter a parse tree produced by plsqlParser#type_definition.
    def enterType_definition(self, ctx:plsqlParser.Type_definitionContext):
        pass

    # Exit a parse tree produced by plsqlParser#type_definition.
    def exitType_definition(self, ctx:plsqlParser.Type_definitionContext):
        pass


    # Enter a parse tree produced by plsqlParser#object_type_def.
    def enterObject_type_def(self, ctx:plsqlParser.Object_type_defContext):
        pass

    # Exit a parse tree produced by plsqlParser#object_type_def.
    def exitObject_type_def(self, ctx:plsqlParser.Object_type_defContext):
        pass


    # Enter a parse tree produced by plsqlParser#object_as_part.
    def enterObject_as_part(self, ctx:plsqlParser.Object_as_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#object_as_part.
    def exitObject_as_part(self, ctx:plsqlParser.Object_as_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#object_under_part.
    def enterObject_under_part(self, ctx:plsqlParser.Object_under_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#object_under_part.
    def exitObject_under_part(self, ctx:plsqlParser.Object_under_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#nested_table_type_def.
    def enterNested_table_type_def(self, ctx:plsqlParser.Nested_table_type_defContext):
        pass

    # Exit a parse tree produced by plsqlParser#nested_table_type_def.
    def exitNested_table_type_def(self, ctx:plsqlParser.Nested_table_type_defContext):
        pass


    # Enter a parse tree produced by plsqlParser#sqlj_object_type.
    def enterSqlj_object_type(self, ctx:plsqlParser.Sqlj_object_typeContext):
        pass

    # Exit a parse tree produced by plsqlParser#sqlj_object_type.
    def exitSqlj_object_type(self, ctx:plsqlParser.Sqlj_object_typeContext):
        pass


    # Enter a parse tree produced by plsqlParser#type_body.
    def enterType_body(self, ctx:plsqlParser.Type_bodyContext):
        pass

    # Exit a parse tree produced by plsqlParser#type_body.
    def exitType_body(self, ctx:plsqlParser.Type_bodyContext):
        pass


    # Enter a parse tree produced by plsqlParser#type_body_elements.
    def enterType_body_elements(self, ctx:plsqlParser.Type_body_elementsContext):
        pass

    # Exit a parse tree produced by plsqlParser#type_body_elements.
    def exitType_body_elements(self, ctx:plsqlParser.Type_body_elementsContext):
        pass


    # Enter a parse tree produced by plsqlParser#map_order_func_declaration.
    def enterMap_order_func_declaration(self, ctx:plsqlParser.Map_order_func_declarationContext):
        pass

    # Exit a parse tree produced by plsqlParser#map_order_func_declaration.
    def exitMap_order_func_declaration(self, ctx:plsqlParser.Map_order_func_declarationContext):
        pass


    # Enter a parse tree produced by plsqlParser#subprog_decl_in_type.
    def enterSubprog_decl_in_type(self, ctx:plsqlParser.Subprog_decl_in_typeContext):
        pass

    # Exit a parse tree produced by plsqlParser#subprog_decl_in_type.
    def exitSubprog_decl_in_type(self, ctx:plsqlParser.Subprog_decl_in_typeContext):
        pass


    # Enter a parse tree produced by plsqlParser#proc_decl_in_type.
    def enterProc_decl_in_type(self, ctx:plsqlParser.Proc_decl_in_typeContext):
        pass

    # Exit a parse tree produced by plsqlParser#proc_decl_in_type.
    def exitProc_decl_in_type(self, ctx:plsqlParser.Proc_decl_in_typeContext):
        pass


    # Enter a parse tree produced by plsqlParser#func_decl_in_type.
    def enterFunc_decl_in_type(self, ctx:plsqlParser.Func_decl_in_typeContext):
        pass

    # Exit a parse tree produced by plsqlParser#func_decl_in_type.
    def exitFunc_decl_in_type(self, ctx:plsqlParser.Func_decl_in_typeContext):
        pass


    # Enter a parse tree produced by plsqlParser#constructor_declaration.
    def enterConstructor_declaration(self, ctx:plsqlParser.Constructor_declarationContext):
        pass

    # Exit a parse tree produced by plsqlParser#constructor_declaration.
    def exitConstructor_declaration(self, ctx:plsqlParser.Constructor_declarationContext):
        pass


    # Enter a parse tree produced by plsqlParser#modifier_clause.
    def enterModifier_clause(self, ctx:plsqlParser.Modifier_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#modifier_clause.
    def exitModifier_clause(self, ctx:plsqlParser.Modifier_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#object_member_spec.
    def enterObject_member_spec(self, ctx:plsqlParser.Object_member_specContext):
        pass

    # Exit a parse tree produced by plsqlParser#object_member_spec.
    def exitObject_member_spec(self, ctx:plsqlParser.Object_member_specContext):
        pass


    # Enter a parse tree produced by plsqlParser#sqlj_object_type_attr.
    def enterSqlj_object_type_attr(self, ctx:plsqlParser.Sqlj_object_type_attrContext):
        pass

    # Exit a parse tree produced by plsqlParser#sqlj_object_type_attr.
    def exitSqlj_object_type_attr(self, ctx:plsqlParser.Sqlj_object_type_attrContext):
        pass


    # Enter a parse tree produced by plsqlParser#element_spec.
    def enterElement_spec(self, ctx:plsqlParser.Element_specContext):
        pass

    # Exit a parse tree produced by plsqlParser#element_spec.
    def exitElement_spec(self, ctx:plsqlParser.Element_specContext):
        pass


    # Enter a parse tree produced by plsqlParser#element_spec_options.
    def enterElement_spec_options(self, ctx:plsqlParser.Element_spec_optionsContext):
        pass

    # Exit a parse tree produced by plsqlParser#element_spec_options.
    def exitElement_spec_options(self, ctx:plsqlParser.Element_spec_optionsContext):
        pass


    # Enter a parse tree produced by plsqlParser#subprogram_spec.
    def enterSubprogram_spec(self, ctx:plsqlParser.Subprogram_specContext):
        pass

    # Exit a parse tree produced by plsqlParser#subprogram_spec.
    def exitSubprogram_spec(self, ctx:plsqlParser.Subprogram_specContext):
        pass


    # Enter a parse tree produced by plsqlParser#type_procedure_spec.
    def enterType_procedure_spec(self, ctx:plsqlParser.Type_procedure_specContext):
        pass

    # Exit a parse tree produced by plsqlParser#type_procedure_spec.
    def exitType_procedure_spec(self, ctx:plsqlParser.Type_procedure_specContext):
        pass


    # Enter a parse tree produced by plsqlParser#type_function_spec.
    def enterType_function_spec(self, ctx:plsqlParser.Type_function_specContext):
        pass

    # Exit a parse tree produced by plsqlParser#type_function_spec.
    def exitType_function_spec(self, ctx:plsqlParser.Type_function_specContext):
        pass


    # Enter a parse tree produced by plsqlParser#constructor_spec.
    def enterConstructor_spec(self, ctx:plsqlParser.Constructor_specContext):
        pass

    # Exit a parse tree produced by plsqlParser#constructor_spec.
    def exitConstructor_spec(self, ctx:plsqlParser.Constructor_specContext):
        pass


    # Enter a parse tree produced by plsqlParser#map_order_function_spec.
    def enterMap_order_function_spec(self, ctx:plsqlParser.Map_order_function_specContext):
        pass

    # Exit a parse tree produced by plsqlParser#map_order_function_spec.
    def exitMap_order_function_spec(self, ctx:plsqlParser.Map_order_function_specContext):
        pass


    # Enter a parse tree produced by plsqlParser#pragma_clause.
    def enterPragma_clause(self, ctx:plsqlParser.Pragma_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#pragma_clause.
    def exitPragma_clause(self, ctx:plsqlParser.Pragma_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#pragma_elements.
    def enterPragma_elements(self, ctx:plsqlParser.Pragma_elementsContext):
        pass

    # Exit a parse tree produced by plsqlParser#pragma_elements.
    def exitPragma_elements(self, ctx:plsqlParser.Pragma_elementsContext):
        pass


    # Enter a parse tree produced by plsqlParser#type_elements_parameter.
    def enterType_elements_parameter(self, ctx:plsqlParser.Type_elements_parameterContext):
        pass

    # Exit a parse tree produced by plsqlParser#type_elements_parameter.
    def exitType_elements_parameter(self, ctx:plsqlParser.Type_elements_parameterContext):
        pass


    # Enter a parse tree produced by plsqlParser#drop_sequence.
    def enterDrop_sequence(self, ctx:plsqlParser.Drop_sequenceContext):
        pass

    # Exit a parse tree produced by plsqlParser#drop_sequence.
    def exitDrop_sequence(self, ctx:plsqlParser.Drop_sequenceContext):
        pass


    # Enter a parse tree produced by plsqlParser#alter_sequence.
    def enterAlter_sequence(self, ctx:plsqlParser.Alter_sequenceContext):
        pass

    # Exit a parse tree produced by plsqlParser#alter_sequence.
    def exitAlter_sequence(self, ctx:plsqlParser.Alter_sequenceContext):
        pass


    # Enter a parse tree produced by plsqlParser#create_sequence.
    def enterCreate_sequence(self, ctx:plsqlParser.Create_sequenceContext):
        pass

    # Exit a parse tree produced by plsqlParser#create_sequence.
    def exitCreate_sequence(self, ctx:plsqlParser.Create_sequenceContext):
        pass


    # Enter a parse tree produced by plsqlParser#sequence_spec.
    def enterSequence_spec(self, ctx:plsqlParser.Sequence_specContext):
        pass

    # Exit a parse tree produced by plsqlParser#sequence_spec.
    def exitSequence_spec(self, ctx:plsqlParser.Sequence_specContext):
        pass


    # Enter a parse tree produced by plsqlParser#sequence_start_clause.
    def enterSequence_start_clause(self, ctx:plsqlParser.Sequence_start_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#sequence_start_clause.
    def exitSequence_start_clause(self, ctx:plsqlParser.Sequence_start_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#invoker_rights_clause.
    def enterInvoker_rights_clause(self, ctx:plsqlParser.Invoker_rights_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#invoker_rights_clause.
    def exitInvoker_rights_clause(self, ctx:plsqlParser.Invoker_rights_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#compiler_parameters_clause.
    def enterCompiler_parameters_clause(self, ctx:plsqlParser.Compiler_parameters_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#compiler_parameters_clause.
    def exitCompiler_parameters_clause(self, ctx:plsqlParser.Compiler_parameters_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#call_spec.
    def enterCall_spec(self, ctx:plsqlParser.Call_specContext):
        pass

    # Exit a parse tree produced by plsqlParser#call_spec.
    def exitCall_spec(self, ctx:plsqlParser.Call_specContext):
        pass


    # Enter a parse tree produced by plsqlParser#java_spec.
    def enterJava_spec(self, ctx:plsqlParser.Java_specContext):
        pass

    # Exit a parse tree produced by plsqlParser#java_spec.
    def exitJava_spec(self, ctx:plsqlParser.Java_specContext):
        pass


    # Enter a parse tree produced by plsqlParser#c_spec.
    def enterC_spec(self, ctx:plsqlParser.C_specContext):
        pass

    # Exit a parse tree produced by plsqlParser#c_spec.
    def exitC_spec(self, ctx:plsqlParser.C_specContext):
        pass


    # Enter a parse tree produced by plsqlParser#c_agent_in_clause.
    def enterC_agent_in_clause(self, ctx:plsqlParser.C_agent_in_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#c_agent_in_clause.
    def exitC_agent_in_clause(self, ctx:plsqlParser.C_agent_in_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#c_parameters_clause.
    def enterC_parameters_clause(self, ctx:plsqlParser.C_parameters_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#c_parameters_clause.
    def exitC_parameters_clause(self, ctx:plsqlParser.C_parameters_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#parameter.
    def enterParameter(self, ctx:plsqlParser.ParameterContext):
        pass

    # Exit a parse tree produced by plsqlParser#parameter.
    def exitParameter(self, ctx:plsqlParser.ParameterContext):
        pass


    # Enter a parse tree produced by plsqlParser#default_value_part.
    def enterDefault_value_part(self, ctx:plsqlParser.Default_value_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#default_value_part.
    def exitDefault_value_part(self, ctx:plsqlParser.Default_value_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#declare_spec.
    def enterDeclare_spec(self, ctx:plsqlParser.Declare_specContext):
        pass

    # Exit a parse tree produced by plsqlParser#declare_spec.
    def exitDeclare_spec(self, ctx:plsqlParser.Declare_specContext):
        pass


    # Enter a parse tree produced by plsqlParser#variable_declaration.
    def enterVariable_declaration(self, ctx:plsqlParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by plsqlParser#variable_declaration.
    def exitVariable_declaration(self, ctx:plsqlParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by plsqlParser#subtype_declaration.
    def enterSubtype_declaration(self, ctx:plsqlParser.Subtype_declarationContext):
        pass

    # Exit a parse tree produced by plsqlParser#subtype_declaration.
    def exitSubtype_declaration(self, ctx:plsqlParser.Subtype_declarationContext):
        pass


    # Enter a parse tree produced by plsqlParser#cursor_declaration.
    def enterCursor_declaration(self, ctx:plsqlParser.Cursor_declarationContext):
        pass

    # Exit a parse tree produced by plsqlParser#cursor_declaration.
    def exitCursor_declaration(self, ctx:plsqlParser.Cursor_declarationContext):
        pass


    # Enter a parse tree produced by plsqlParser#parameter_spec.
    def enterParameter_spec(self, ctx:plsqlParser.Parameter_specContext):
        pass

    # Exit a parse tree produced by plsqlParser#parameter_spec.
    def exitParameter_spec(self, ctx:plsqlParser.Parameter_specContext):
        pass


    # Enter a parse tree produced by plsqlParser#exception_declaration.
    def enterException_declaration(self, ctx:plsqlParser.Exception_declarationContext):
        pass

    # Exit a parse tree produced by plsqlParser#exception_declaration.
    def exitException_declaration(self, ctx:plsqlParser.Exception_declarationContext):
        pass


    # Enter a parse tree produced by plsqlParser#pragma_declaration.
    def enterPragma_declaration(self, ctx:plsqlParser.Pragma_declarationContext):
        pass

    # Exit a parse tree produced by plsqlParser#pragma_declaration.
    def exitPragma_declaration(self, ctx:plsqlParser.Pragma_declarationContext):
        pass


    # Enter a parse tree produced by plsqlParser#record_declaration.
    def enterRecord_declaration(self, ctx:plsqlParser.Record_declarationContext):
        pass

    # Exit a parse tree produced by plsqlParser#record_declaration.
    def exitRecord_declaration(self, ctx:plsqlParser.Record_declarationContext):
        pass


    # Enter a parse tree produced by plsqlParser#record_type_dec.
    def enterRecord_type_dec(self, ctx:plsqlParser.Record_type_decContext):
        pass

    # Exit a parse tree produced by plsqlParser#record_type_dec.
    def exitRecord_type_dec(self, ctx:plsqlParser.Record_type_decContext):
        pass


    # Enter a parse tree produced by plsqlParser#field_spec.
    def enterField_spec(self, ctx:plsqlParser.Field_specContext):
        pass

    # Exit a parse tree produced by plsqlParser#field_spec.
    def exitField_spec(self, ctx:plsqlParser.Field_specContext):
        pass


    # Enter a parse tree produced by plsqlParser#record_var_dec.
    def enterRecord_var_dec(self, ctx:plsqlParser.Record_var_decContext):
        pass

    # Exit a parse tree produced by plsqlParser#record_var_dec.
    def exitRecord_var_dec(self, ctx:plsqlParser.Record_var_decContext):
        pass


    # Enter a parse tree produced by plsqlParser#table_declaration.
    def enterTable_declaration(self, ctx:plsqlParser.Table_declarationContext):
        pass

    # Exit a parse tree produced by plsqlParser#table_declaration.
    def exitTable_declaration(self, ctx:plsqlParser.Table_declarationContext):
        pass


    # Enter a parse tree produced by plsqlParser#table_type_dec.
    def enterTable_type_dec(self, ctx:plsqlParser.Table_type_decContext):
        pass

    # Exit a parse tree produced by plsqlParser#table_type_dec.
    def exitTable_type_dec(self, ctx:plsqlParser.Table_type_decContext):
        pass


    # Enter a parse tree produced by plsqlParser#table_indexed_by_part.
    def enterTable_indexed_by_part(self, ctx:plsqlParser.Table_indexed_by_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#table_indexed_by_part.
    def exitTable_indexed_by_part(self, ctx:plsqlParser.Table_indexed_by_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#varray_type_def.
    def enterVarray_type_def(self, ctx:plsqlParser.Varray_type_defContext):
        pass

    # Exit a parse tree produced by plsqlParser#varray_type_def.
    def exitVarray_type_def(self, ctx:plsqlParser.Varray_type_defContext):
        pass


    # Enter a parse tree produced by plsqlParser#table_var_dec.
    def enterTable_var_dec(self, ctx:plsqlParser.Table_var_decContext):
        pass

    # Exit a parse tree produced by plsqlParser#table_var_dec.
    def exitTable_var_dec(self, ctx:plsqlParser.Table_var_decContext):
        pass


    # Enter a parse tree produced by plsqlParser#seq_of_statements.
    def enterSeq_of_statements(self, ctx:plsqlParser.Seq_of_statementsContext):
        pass

    # Exit a parse tree produced by plsqlParser#seq_of_statements.
    def exitSeq_of_statements(self, ctx:plsqlParser.Seq_of_statementsContext):
        pass


    # Enter a parse tree produced by plsqlParser#label_declaration.
    def enterLabel_declaration(self, ctx:plsqlParser.Label_declarationContext):
        pass

    # Exit a parse tree produced by plsqlParser#label_declaration.
    def exitLabel_declaration(self, ctx:plsqlParser.Label_declarationContext):
        pass


    # Enter a parse tree produced by plsqlParser#statement.
    def enterStatement(self, ctx:plsqlParser.StatementContext):
        pass

    # Exit a parse tree produced by plsqlParser#statement.
    def exitStatement(self, ctx:plsqlParser.StatementContext):
        pass


    # Enter a parse tree produced by plsqlParser#assignment_statement.
    def enterAssignment_statement(self, ctx:plsqlParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#assignment_statement.
    def exitAssignment_statement(self, ctx:plsqlParser.Assignment_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#continue_statement.
    def enterContinue_statement(self, ctx:plsqlParser.Continue_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#continue_statement.
    def exitContinue_statement(self, ctx:plsqlParser.Continue_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#exit_statement.
    def enterExit_statement(self, ctx:plsqlParser.Exit_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#exit_statement.
    def exitExit_statement(self, ctx:plsqlParser.Exit_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#goto_statement.
    def enterGoto_statement(self, ctx:plsqlParser.Goto_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#goto_statement.
    def exitGoto_statement(self, ctx:plsqlParser.Goto_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#if_statement.
    def enterIf_statement(self, ctx:plsqlParser.If_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#if_statement.
    def exitIf_statement(self, ctx:plsqlParser.If_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#elsif_part.
    def enterElsif_part(self, ctx:plsqlParser.Elsif_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#elsif_part.
    def exitElsif_part(self, ctx:plsqlParser.Elsif_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#else_part.
    def enterElse_part(self, ctx:plsqlParser.Else_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#else_part.
    def exitElse_part(self, ctx:plsqlParser.Else_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#loop_statement.
    def enterLoop_statement(self, ctx:plsqlParser.Loop_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#loop_statement.
    def exitLoop_statement(self, ctx:plsqlParser.Loop_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#cursor_loop_param.
    def enterCursor_loop_param(self, ctx:plsqlParser.Cursor_loop_paramContext):
        pass

    # Exit a parse tree produced by plsqlParser#cursor_loop_param.
    def exitCursor_loop_param(self, ctx:plsqlParser.Cursor_loop_paramContext):
        pass


    # Enter a parse tree produced by plsqlParser#forall_statement.
    def enterForall_statement(self, ctx:plsqlParser.Forall_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#forall_statement.
    def exitForall_statement(self, ctx:plsqlParser.Forall_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#bounds_clause.
    def enterBounds_clause(self, ctx:plsqlParser.Bounds_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#bounds_clause.
    def exitBounds_clause(self, ctx:plsqlParser.Bounds_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#between_bound.
    def enterBetween_bound(self, ctx:plsqlParser.Between_boundContext):
        pass

    # Exit a parse tree produced by plsqlParser#between_bound.
    def exitBetween_bound(self, ctx:plsqlParser.Between_boundContext):
        pass


    # Enter a parse tree produced by plsqlParser#lower_bound.
    def enterLower_bound(self, ctx:plsqlParser.Lower_boundContext):
        pass

    # Exit a parse tree produced by plsqlParser#lower_bound.
    def exitLower_bound(self, ctx:plsqlParser.Lower_boundContext):
        pass


    # Enter a parse tree produced by plsqlParser#upper_bound.
    def enterUpper_bound(self, ctx:plsqlParser.Upper_boundContext):
        pass

    # Exit a parse tree produced by plsqlParser#upper_bound.
    def exitUpper_bound(self, ctx:plsqlParser.Upper_boundContext):
        pass


    # Enter a parse tree produced by plsqlParser#null_statement.
    def enterNull_statement(self, ctx:plsqlParser.Null_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#null_statement.
    def exitNull_statement(self, ctx:plsqlParser.Null_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#raise_statement.
    def enterRaise_statement(self, ctx:plsqlParser.Raise_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#raise_statement.
    def exitRaise_statement(self, ctx:plsqlParser.Raise_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#return_statement.
    def enterReturn_statement(self, ctx:plsqlParser.Return_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#return_statement.
    def exitReturn_statement(self, ctx:plsqlParser.Return_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#function_call.
    def enterFunction_call(self, ctx:plsqlParser.Function_callContext):
        pass

    # Exit a parse tree produced by plsqlParser#function_call.
    def exitFunction_call(self, ctx:plsqlParser.Function_callContext):
        pass


    # Enter a parse tree produced by plsqlParser#body.
    def enterBody(self, ctx:plsqlParser.BodyContext):
        pass

    # Exit a parse tree produced by plsqlParser#body.
    def exitBody(self, ctx:plsqlParser.BodyContext):
        pass


    # Enter a parse tree produced by plsqlParser#exception_handler.
    def enterException_handler(self, ctx:plsqlParser.Exception_handlerContext):
        pass

    # Exit a parse tree produced by plsqlParser#exception_handler.
    def exitException_handler(self, ctx:plsqlParser.Exception_handlerContext):
        pass


    # Enter a parse tree produced by plsqlParser#trigger_block.
    def enterTrigger_block(self, ctx:plsqlParser.Trigger_blockContext):
        pass

    # Exit a parse tree produced by plsqlParser#trigger_block.
    def exitTrigger_block(self, ctx:plsqlParser.Trigger_blockContext):
        pass


    # Enter a parse tree produced by plsqlParser#block.
    def enterBlock(self, ctx:plsqlParser.BlockContext):
        pass

    # Exit a parse tree produced by plsqlParser#block.
    def exitBlock(self, ctx:plsqlParser.BlockContext):
        pass


    # Enter a parse tree produced by plsqlParser#sql_statement.
    def enterSql_statement(self, ctx:plsqlParser.Sql_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#sql_statement.
    def exitSql_statement(self, ctx:plsqlParser.Sql_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#execute_immediate.
    def enterExecute_immediate(self, ctx:plsqlParser.Execute_immediateContext):
        pass

    # Exit a parse tree produced by plsqlParser#execute_immediate.
    def exitExecute_immediate(self, ctx:plsqlParser.Execute_immediateContext):
        pass


    # Enter a parse tree produced by plsqlParser#dynamic_returning_clause.
    def enterDynamic_returning_clause(self, ctx:plsqlParser.Dynamic_returning_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#dynamic_returning_clause.
    def exitDynamic_returning_clause(self, ctx:plsqlParser.Dynamic_returning_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#data_manipulation_language_statements.
    def enterData_manipulation_language_statements(self, ctx:plsqlParser.Data_manipulation_language_statementsContext):
        pass

    # Exit a parse tree produced by plsqlParser#data_manipulation_language_statements.
    def exitData_manipulation_language_statements(self, ctx:plsqlParser.Data_manipulation_language_statementsContext):
        pass


    # Enter a parse tree produced by plsqlParser#cursor_manipulation_statements.
    def enterCursor_manipulation_statements(self, ctx:plsqlParser.Cursor_manipulation_statementsContext):
        pass

    # Exit a parse tree produced by plsqlParser#cursor_manipulation_statements.
    def exitCursor_manipulation_statements(self, ctx:plsqlParser.Cursor_manipulation_statementsContext):
        pass


    # Enter a parse tree produced by plsqlParser#close_statement.
    def enterClose_statement(self, ctx:plsqlParser.Close_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#close_statement.
    def exitClose_statement(self, ctx:plsqlParser.Close_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#open_statement.
    def enterOpen_statement(self, ctx:plsqlParser.Open_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#open_statement.
    def exitOpen_statement(self, ctx:plsqlParser.Open_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#fetch_statement.
    def enterFetch_statement(self, ctx:plsqlParser.Fetch_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#fetch_statement.
    def exitFetch_statement(self, ctx:plsqlParser.Fetch_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#open_for_statement.
    def enterOpen_for_statement(self, ctx:plsqlParser.Open_for_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#open_for_statement.
    def exitOpen_for_statement(self, ctx:plsqlParser.Open_for_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#transaction_control_statements.
    def enterTransaction_control_statements(self, ctx:plsqlParser.Transaction_control_statementsContext):
        pass

    # Exit a parse tree produced by plsqlParser#transaction_control_statements.
    def exitTransaction_control_statements(self, ctx:plsqlParser.Transaction_control_statementsContext):
        pass


    # Enter a parse tree produced by plsqlParser#set_transaction_command.
    def enterSet_transaction_command(self, ctx:plsqlParser.Set_transaction_commandContext):
        pass

    # Exit a parse tree produced by plsqlParser#set_transaction_command.
    def exitSet_transaction_command(self, ctx:plsqlParser.Set_transaction_commandContext):
        pass


    # Enter a parse tree produced by plsqlParser#set_constraint_command.
    def enterSet_constraint_command(self, ctx:plsqlParser.Set_constraint_commandContext):
        pass

    # Exit a parse tree produced by plsqlParser#set_constraint_command.
    def exitSet_constraint_command(self, ctx:plsqlParser.Set_constraint_commandContext):
        pass


    # Enter a parse tree produced by plsqlParser#commit_statement.
    def enterCommit_statement(self, ctx:plsqlParser.Commit_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#commit_statement.
    def exitCommit_statement(self, ctx:plsqlParser.Commit_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#write_clause.
    def enterWrite_clause(self, ctx:plsqlParser.Write_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#write_clause.
    def exitWrite_clause(self, ctx:plsqlParser.Write_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#rollback_statement.
    def enterRollback_statement(self, ctx:plsqlParser.Rollback_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#rollback_statement.
    def exitRollback_statement(self, ctx:plsqlParser.Rollback_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#savepoint_statement.
    def enterSavepoint_statement(self, ctx:plsqlParser.Savepoint_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#savepoint_statement.
    def exitSavepoint_statement(self, ctx:plsqlParser.Savepoint_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#explain_statement.
    def enterExplain_statement(self, ctx:plsqlParser.Explain_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#explain_statement.
    def exitExplain_statement(self, ctx:plsqlParser.Explain_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#select_statement.
    def enterSelect_statement(self, ctx:plsqlParser.Select_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#select_statement.
    def exitSelect_statement(self, ctx:plsqlParser.Select_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#subquery_factoring_clause.
    def enterSubquery_factoring_clause(self, ctx:plsqlParser.Subquery_factoring_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#subquery_factoring_clause.
    def exitSubquery_factoring_clause(self, ctx:plsqlParser.Subquery_factoring_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#factoring_element.
    def enterFactoring_element(self, ctx:plsqlParser.Factoring_elementContext):
        pass

    # Exit a parse tree produced by plsqlParser#factoring_element.
    def exitFactoring_element(self, ctx:plsqlParser.Factoring_elementContext):
        pass


    # Enter a parse tree produced by plsqlParser#search_clause.
    def enterSearch_clause(self, ctx:plsqlParser.Search_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#search_clause.
    def exitSearch_clause(self, ctx:plsqlParser.Search_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#cycle_clause.
    def enterCycle_clause(self, ctx:plsqlParser.Cycle_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#cycle_clause.
    def exitCycle_clause(self, ctx:plsqlParser.Cycle_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#subquery.
    def enterSubquery(self, ctx:plsqlParser.SubqueryContext):
        pass

    # Exit a parse tree produced by plsqlParser#subquery.
    def exitSubquery(self, ctx:plsqlParser.SubqueryContext):
        pass


    # Enter a parse tree produced by plsqlParser#subquery_operation_part.
    def enterSubquery_operation_part(self, ctx:plsqlParser.Subquery_operation_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#subquery_operation_part.
    def exitSubquery_operation_part(self, ctx:plsqlParser.Subquery_operation_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#query_block.
    def enterQuery_block(self, ctx:plsqlParser.Query_blockContext):
        pass

    # Exit a parse tree produced by plsqlParser#query_block.
    def exitQuery_block(self, ctx:plsqlParser.Query_blockContext):
        pass


    # Enter a parse tree produced by plsqlParser#Star1.
    def enterStar1(self, ctx:plsqlParser.Star1Context):
        pass

    # Exit a parse tree produced by plsqlParser#Star1.
    def exitStar1(self, ctx:plsqlParser.Star1Context):
        pass


    # Enter a parse tree produced by plsqlParser#StarTable.
    def enterStarTable(self, ctx:plsqlParser.StarTableContext):
        pass

    # Exit a parse tree produced by plsqlParser#StarTable.
    def exitStarTable(self, ctx:plsqlParser.StarTableContext):
        pass


    # Enter a parse tree produced by plsqlParser#Alias_expr.
    def enterAlias_expr(self, ctx:plsqlParser.Alias_exprContext):
        pass

    # Exit a parse tree produced by plsqlParser#Alias_expr.
    def exitAlias_expr(self, ctx:plsqlParser.Alias_exprContext):
        pass


    # Enter a parse tree produced by plsqlParser#from_clause.
    def enterFrom_clause(self, ctx:plsqlParser.From_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#from_clause.
    def exitFrom_clause(self, ctx:plsqlParser.From_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#table_ref_list.
    def enterTable_ref_list(self, ctx:plsqlParser.Table_ref_listContext):
        pass

    # Exit a parse tree produced by plsqlParser#table_ref_list.
    def exitTable_ref_list(self, ctx:plsqlParser.Table_ref_listContext):
        pass


    # Enter a parse tree produced by plsqlParser#table_ref.
    def enterTable_ref(self, ctx:plsqlParser.Table_refContext):
        pass

    # Exit a parse tree produced by plsqlParser#table_ref.
    def exitTable_ref(self, ctx:plsqlParser.Table_refContext):
        pass


    # Enter a parse tree produced by plsqlParser#table_ref_aux.
    def enterTable_ref_aux(self, ctx:plsqlParser.Table_ref_auxContext):
        pass

    # Exit a parse tree produced by plsqlParser#table_ref_aux.
    def exitTable_ref_aux(self, ctx:plsqlParser.Table_ref_auxContext):
        pass


    # Enter a parse tree produced by plsqlParser#join_clause.
    def enterJoin_clause(self, ctx:plsqlParser.Join_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#join_clause.
    def exitJoin_clause(self, ctx:plsqlParser.Join_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#join_on_part.
    def enterJoin_on_part(self, ctx:plsqlParser.Join_on_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#join_on_part.
    def exitJoin_on_part(self, ctx:plsqlParser.Join_on_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#join_using_part.
    def enterJoin_using_part(self, ctx:plsqlParser.Join_using_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#join_using_part.
    def exitJoin_using_part(self, ctx:plsqlParser.Join_using_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#outer_join_type.
    def enterOuter_join_type(self, ctx:plsqlParser.Outer_join_typeContext):
        pass

    # Exit a parse tree produced by plsqlParser#outer_join_type.
    def exitOuter_join_type(self, ctx:plsqlParser.Outer_join_typeContext):
        pass


    # Enter a parse tree produced by plsqlParser#query_partition_clause.
    def enterQuery_partition_clause(self, ctx:plsqlParser.Query_partition_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#query_partition_clause.
    def exitQuery_partition_clause(self, ctx:plsqlParser.Query_partition_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#flashback_query_clause.
    def enterFlashback_query_clause(self, ctx:plsqlParser.Flashback_query_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#flashback_query_clause.
    def exitFlashback_query_clause(self, ctx:plsqlParser.Flashback_query_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#pivot_clause.
    def enterPivot_clause(self, ctx:plsqlParser.Pivot_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#pivot_clause.
    def exitPivot_clause(self, ctx:plsqlParser.Pivot_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#pivot_element.
    def enterPivot_element(self, ctx:plsqlParser.Pivot_elementContext):
        pass

    # Exit a parse tree produced by plsqlParser#pivot_element.
    def exitPivot_element(self, ctx:plsqlParser.Pivot_elementContext):
        pass


    # Enter a parse tree produced by plsqlParser#pivot_for_clause.
    def enterPivot_for_clause(self, ctx:plsqlParser.Pivot_for_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#pivot_for_clause.
    def exitPivot_for_clause(self, ctx:plsqlParser.Pivot_for_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#pivot_in_clause.
    def enterPivot_in_clause(self, ctx:plsqlParser.Pivot_in_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#pivot_in_clause.
    def exitPivot_in_clause(self, ctx:plsqlParser.Pivot_in_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#pivot_in_clause_element.
    def enterPivot_in_clause_element(self, ctx:plsqlParser.Pivot_in_clause_elementContext):
        pass

    # Exit a parse tree produced by plsqlParser#pivot_in_clause_element.
    def exitPivot_in_clause_element(self, ctx:plsqlParser.Pivot_in_clause_elementContext):
        pass


    # Enter a parse tree produced by plsqlParser#pivot_in_clause_elements.
    def enterPivot_in_clause_elements(self, ctx:plsqlParser.Pivot_in_clause_elementsContext):
        pass

    # Exit a parse tree produced by plsqlParser#pivot_in_clause_elements.
    def exitPivot_in_clause_elements(self, ctx:plsqlParser.Pivot_in_clause_elementsContext):
        pass


    # Enter a parse tree produced by plsqlParser#unpivot_clause.
    def enterUnpivot_clause(self, ctx:plsqlParser.Unpivot_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#unpivot_clause.
    def exitUnpivot_clause(self, ctx:plsqlParser.Unpivot_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#unpivot_in_clause.
    def enterUnpivot_in_clause(self, ctx:plsqlParser.Unpivot_in_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#unpivot_in_clause.
    def exitUnpivot_in_clause(self, ctx:plsqlParser.Unpivot_in_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#unpivot_in_elements.
    def enterUnpivot_in_elements(self, ctx:plsqlParser.Unpivot_in_elementsContext):
        pass

    # Exit a parse tree produced by plsqlParser#unpivot_in_elements.
    def exitUnpivot_in_elements(self, ctx:plsqlParser.Unpivot_in_elementsContext):
        pass


    # Enter a parse tree produced by plsqlParser#hierarchical_query_clause.
    def enterHierarchical_query_clause(self, ctx:plsqlParser.Hierarchical_query_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#hierarchical_query_clause.
    def exitHierarchical_query_clause(self, ctx:plsqlParser.Hierarchical_query_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#start_part.
    def enterStart_part(self, ctx:plsqlParser.Start_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#start_part.
    def exitStart_part(self, ctx:plsqlParser.Start_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#group_by_clause.
    def enterGroup_by_clause(self, ctx:plsqlParser.Group_by_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#group_by_clause.
    def exitGroup_by_clause(self, ctx:plsqlParser.Group_by_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#group_by_elements.
    def enterGroup_by_elements(self, ctx:plsqlParser.Group_by_elementsContext):
        pass

    # Exit a parse tree produced by plsqlParser#group_by_elements.
    def exitGroup_by_elements(self, ctx:plsqlParser.Group_by_elementsContext):
        pass


    # Enter a parse tree produced by plsqlParser#rollup_cube_clause.
    def enterRollup_cube_clause(self, ctx:plsqlParser.Rollup_cube_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#rollup_cube_clause.
    def exitRollup_cube_clause(self, ctx:plsqlParser.Rollup_cube_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#grouping_sets_clause.
    def enterGrouping_sets_clause(self, ctx:plsqlParser.Grouping_sets_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#grouping_sets_clause.
    def exitGrouping_sets_clause(self, ctx:plsqlParser.Grouping_sets_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#grouping_sets_elements.
    def enterGrouping_sets_elements(self, ctx:plsqlParser.Grouping_sets_elementsContext):
        pass

    # Exit a parse tree produced by plsqlParser#grouping_sets_elements.
    def exitGrouping_sets_elements(self, ctx:plsqlParser.Grouping_sets_elementsContext):
        pass


    # Enter a parse tree produced by plsqlParser#having_clause.
    def enterHaving_clause(self, ctx:plsqlParser.Having_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#having_clause.
    def exitHaving_clause(self, ctx:plsqlParser.Having_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#model_clause.
    def enterModel_clause(self, ctx:plsqlParser.Model_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#model_clause.
    def exitModel_clause(self, ctx:plsqlParser.Model_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#cell_reference_options.
    def enterCell_reference_options(self, ctx:plsqlParser.Cell_reference_optionsContext):
        pass

    # Exit a parse tree produced by plsqlParser#cell_reference_options.
    def exitCell_reference_options(self, ctx:plsqlParser.Cell_reference_optionsContext):
        pass


    # Enter a parse tree produced by plsqlParser#return_rows_clause.
    def enterReturn_rows_clause(self, ctx:plsqlParser.Return_rows_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#return_rows_clause.
    def exitReturn_rows_clause(self, ctx:plsqlParser.Return_rows_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#reference_model.
    def enterReference_model(self, ctx:plsqlParser.Reference_modelContext):
        pass

    # Exit a parse tree produced by plsqlParser#reference_model.
    def exitReference_model(self, ctx:plsqlParser.Reference_modelContext):
        pass


    # Enter a parse tree produced by plsqlParser#main_model.
    def enterMain_model(self, ctx:plsqlParser.Main_modelContext):
        pass

    # Exit a parse tree produced by plsqlParser#main_model.
    def exitMain_model(self, ctx:plsqlParser.Main_modelContext):
        pass


    # Enter a parse tree produced by plsqlParser#model_column_clauses.
    def enterModel_column_clauses(self, ctx:plsqlParser.Model_column_clausesContext):
        pass

    # Exit a parse tree produced by plsqlParser#model_column_clauses.
    def exitModel_column_clauses(self, ctx:plsqlParser.Model_column_clausesContext):
        pass


    # Enter a parse tree produced by plsqlParser#model_column_partition_part.
    def enterModel_column_partition_part(self, ctx:plsqlParser.Model_column_partition_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#model_column_partition_part.
    def exitModel_column_partition_part(self, ctx:plsqlParser.Model_column_partition_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#model_column_list.
    def enterModel_column_list(self, ctx:plsqlParser.Model_column_listContext):
        pass

    # Exit a parse tree produced by plsqlParser#model_column_list.
    def exitModel_column_list(self, ctx:plsqlParser.Model_column_listContext):
        pass


    # Enter a parse tree produced by plsqlParser#model_column.
    def enterModel_column(self, ctx:plsqlParser.Model_columnContext):
        pass

    # Exit a parse tree produced by plsqlParser#model_column.
    def exitModel_column(self, ctx:plsqlParser.Model_columnContext):
        pass


    # Enter a parse tree produced by plsqlParser#model_rules_clause.
    def enterModel_rules_clause(self, ctx:plsqlParser.Model_rules_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#model_rules_clause.
    def exitModel_rules_clause(self, ctx:plsqlParser.Model_rules_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#model_rules_part.
    def enterModel_rules_part(self, ctx:plsqlParser.Model_rules_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#model_rules_part.
    def exitModel_rules_part(self, ctx:plsqlParser.Model_rules_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#model_rules_element.
    def enterModel_rules_element(self, ctx:plsqlParser.Model_rules_elementContext):
        pass

    # Exit a parse tree produced by plsqlParser#model_rules_element.
    def exitModel_rules_element(self, ctx:plsqlParser.Model_rules_elementContext):
        pass


    # Enter a parse tree produced by plsqlParser#cell_assignment.
    def enterCell_assignment(self, ctx:plsqlParser.Cell_assignmentContext):
        pass

    # Exit a parse tree produced by plsqlParser#cell_assignment.
    def exitCell_assignment(self, ctx:plsqlParser.Cell_assignmentContext):
        pass


    # Enter a parse tree produced by plsqlParser#model_iterate_clause.
    def enterModel_iterate_clause(self, ctx:plsqlParser.Model_iterate_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#model_iterate_clause.
    def exitModel_iterate_clause(self, ctx:plsqlParser.Model_iterate_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#until_part.
    def enterUntil_part(self, ctx:plsqlParser.Until_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#until_part.
    def exitUntil_part(self, ctx:plsqlParser.Until_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#order_by_clause.
    def enterOrder_by_clause(self, ctx:plsqlParser.Order_by_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#order_by_clause.
    def exitOrder_by_clause(self, ctx:plsqlParser.Order_by_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#order_by_elements.
    def enterOrder_by_elements(self, ctx:plsqlParser.Order_by_elementsContext):
        pass

    # Exit a parse tree produced by plsqlParser#order_by_elements.
    def exitOrder_by_elements(self, ctx:plsqlParser.Order_by_elementsContext):
        pass


    # Enter a parse tree produced by plsqlParser#for_update_clause.
    def enterFor_update_clause(self, ctx:plsqlParser.For_update_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#for_update_clause.
    def exitFor_update_clause(self, ctx:plsqlParser.For_update_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#for_update_of_part.
    def enterFor_update_of_part(self, ctx:plsqlParser.For_update_of_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#for_update_of_part.
    def exitFor_update_of_part(self, ctx:plsqlParser.For_update_of_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#for_update_options.
    def enterFor_update_options(self, ctx:plsqlParser.For_update_optionsContext):
        pass

    # Exit a parse tree produced by plsqlParser#for_update_options.
    def exitFor_update_options(self, ctx:plsqlParser.For_update_optionsContext):
        pass


    # Enter a parse tree produced by plsqlParser#update_statement.
    def enterUpdate_statement(self, ctx:plsqlParser.Update_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#update_statement.
    def exitUpdate_statement(self, ctx:plsqlParser.Update_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#update_set_clause.
    def enterUpdate_set_clause(self, ctx:plsqlParser.Update_set_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#update_set_clause.
    def exitUpdate_set_clause(self, ctx:plsqlParser.Update_set_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#column_based_update_set_clause.
    def enterColumn_based_update_set_clause(self, ctx:plsqlParser.Column_based_update_set_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#column_based_update_set_clause.
    def exitColumn_based_update_set_clause(self, ctx:plsqlParser.Column_based_update_set_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#delete_statement.
    def enterDelete_statement(self, ctx:plsqlParser.Delete_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#delete_statement.
    def exitDelete_statement(self, ctx:plsqlParser.Delete_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#insert_statement.
    def enterInsert_statement(self, ctx:plsqlParser.Insert_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#insert_statement.
    def exitInsert_statement(self, ctx:plsqlParser.Insert_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#single_table_insert.
    def enterSingle_table_insert(self, ctx:plsqlParser.Single_table_insertContext):
        pass

    # Exit a parse tree produced by plsqlParser#single_table_insert.
    def exitSingle_table_insert(self, ctx:plsqlParser.Single_table_insertContext):
        pass


    # Enter a parse tree produced by plsqlParser#multi_table_insert.
    def enterMulti_table_insert(self, ctx:plsqlParser.Multi_table_insertContext):
        pass

    # Exit a parse tree produced by plsqlParser#multi_table_insert.
    def exitMulti_table_insert(self, ctx:plsqlParser.Multi_table_insertContext):
        pass


    # Enter a parse tree produced by plsqlParser#multi_table_element.
    def enterMulti_table_element(self, ctx:plsqlParser.Multi_table_elementContext):
        pass

    # Exit a parse tree produced by plsqlParser#multi_table_element.
    def exitMulti_table_element(self, ctx:plsqlParser.Multi_table_elementContext):
        pass


    # Enter a parse tree produced by plsqlParser#conditional_insert_clause.
    def enterConditional_insert_clause(self, ctx:plsqlParser.Conditional_insert_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#conditional_insert_clause.
    def exitConditional_insert_clause(self, ctx:plsqlParser.Conditional_insert_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#conditional_insert_when_part.
    def enterConditional_insert_when_part(self, ctx:plsqlParser.Conditional_insert_when_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#conditional_insert_when_part.
    def exitConditional_insert_when_part(self, ctx:plsqlParser.Conditional_insert_when_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#conditional_insert_else_part.
    def enterConditional_insert_else_part(self, ctx:plsqlParser.Conditional_insert_else_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#conditional_insert_else_part.
    def exitConditional_insert_else_part(self, ctx:plsqlParser.Conditional_insert_else_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#insert_into_clause.
    def enterInsert_into_clause(self, ctx:plsqlParser.Insert_into_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#insert_into_clause.
    def exitInsert_into_clause(self, ctx:plsqlParser.Insert_into_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#values_clause.
    def enterValues_clause(self, ctx:plsqlParser.Values_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#values_clause.
    def exitValues_clause(self, ctx:plsqlParser.Values_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#merge_statement.
    def enterMerge_statement(self, ctx:plsqlParser.Merge_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#merge_statement.
    def exitMerge_statement(self, ctx:plsqlParser.Merge_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#merge_update_clause.
    def enterMerge_update_clause(self, ctx:plsqlParser.Merge_update_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#merge_update_clause.
    def exitMerge_update_clause(self, ctx:plsqlParser.Merge_update_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#merge_element.
    def enterMerge_element(self, ctx:plsqlParser.Merge_elementContext):
        pass

    # Exit a parse tree produced by plsqlParser#merge_element.
    def exitMerge_element(self, ctx:plsqlParser.Merge_elementContext):
        pass


    # Enter a parse tree produced by plsqlParser#merge_update_delete_part.
    def enterMerge_update_delete_part(self, ctx:plsqlParser.Merge_update_delete_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#merge_update_delete_part.
    def exitMerge_update_delete_part(self, ctx:plsqlParser.Merge_update_delete_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#merge_insert_clause.
    def enterMerge_insert_clause(self, ctx:plsqlParser.Merge_insert_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#merge_insert_clause.
    def exitMerge_insert_clause(self, ctx:plsqlParser.Merge_insert_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#selected_tableview.
    def enterSelected_tableview(self, ctx:plsqlParser.Selected_tableviewContext):
        pass

    # Exit a parse tree produced by plsqlParser#selected_tableview.
    def exitSelected_tableview(self, ctx:plsqlParser.Selected_tableviewContext):
        pass


    # Enter a parse tree produced by plsqlParser#lock_table_statement.
    def enterLock_table_statement(self, ctx:plsqlParser.Lock_table_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#lock_table_statement.
    def exitLock_table_statement(self, ctx:plsqlParser.Lock_table_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#wait_nowait_part.
    def enterWait_nowait_part(self, ctx:plsqlParser.Wait_nowait_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#wait_nowait_part.
    def exitWait_nowait_part(self, ctx:plsqlParser.Wait_nowait_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#lock_table_element.
    def enterLock_table_element(self, ctx:plsqlParser.Lock_table_elementContext):
        pass

    # Exit a parse tree produced by plsqlParser#lock_table_element.
    def exitLock_table_element(self, ctx:plsqlParser.Lock_table_elementContext):
        pass


    # Enter a parse tree produced by plsqlParser#lock_mode.
    def enterLock_mode(self, ctx:plsqlParser.Lock_modeContext):
        pass

    # Exit a parse tree produced by plsqlParser#lock_mode.
    def exitLock_mode(self, ctx:plsqlParser.Lock_modeContext):
        pass


    # Enter a parse tree produced by plsqlParser#general_table_ref.
    def enterGeneral_table_ref(self, ctx:plsqlParser.General_table_refContext):
        pass

    # Exit a parse tree produced by plsqlParser#general_table_ref.
    def exitGeneral_table_ref(self, ctx:plsqlParser.General_table_refContext):
        pass


    # Enter a parse tree produced by plsqlParser#static_returning_clause.
    def enterStatic_returning_clause(self, ctx:plsqlParser.Static_returning_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#static_returning_clause.
    def exitStatic_returning_clause(self, ctx:plsqlParser.Static_returning_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#error_logging_clause.
    def enterError_logging_clause(self, ctx:plsqlParser.Error_logging_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#error_logging_clause.
    def exitError_logging_clause(self, ctx:plsqlParser.Error_logging_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#error_logging_into_part.
    def enterError_logging_into_part(self, ctx:plsqlParser.Error_logging_into_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#error_logging_into_part.
    def exitError_logging_into_part(self, ctx:plsqlParser.Error_logging_into_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#error_logging_reject_part.
    def enterError_logging_reject_part(self, ctx:plsqlParser.Error_logging_reject_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#error_logging_reject_part.
    def exitError_logging_reject_part(self, ctx:plsqlParser.Error_logging_reject_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#dml_table_expression_clause.
    def enterDml_table_expression_clause(self, ctx:plsqlParser.Dml_table_expression_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#dml_table_expression_clause.
    def exitDml_table_expression_clause(self, ctx:plsqlParser.Dml_table_expression_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#table_collection_expression.
    def enterTable_collection_expression(self, ctx:plsqlParser.Table_collection_expressionContext):
        pass

    # Exit a parse tree produced by plsqlParser#table_collection_expression.
    def exitTable_collection_expression(self, ctx:plsqlParser.Table_collection_expressionContext):
        pass


    # Enter a parse tree produced by plsqlParser#subquery_restriction_clause.
    def enterSubquery_restriction_clause(self, ctx:plsqlParser.Subquery_restriction_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#subquery_restriction_clause.
    def exitSubquery_restriction_clause(self, ctx:plsqlParser.Subquery_restriction_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#sample_clause.
    def enterSample_clause(self, ctx:plsqlParser.Sample_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#sample_clause.
    def exitSample_clause(self, ctx:plsqlParser.Sample_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#seed_part.
    def enterSeed_part(self, ctx:plsqlParser.Seed_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#seed_part.
    def exitSeed_part(self, ctx:plsqlParser.Seed_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#cursor_expression.
    def enterCursor_expression(self, ctx:plsqlParser.Cursor_expressionContext):
        pass

    # Exit a parse tree produced by plsqlParser#cursor_expression.
    def exitCursor_expression(self, ctx:plsqlParser.Cursor_expressionContext):
        pass


    # Enter a parse tree produced by plsqlParser#expression_list.
    def enterExpression_list(self, ctx:plsqlParser.Expression_listContext):
        pass

    # Exit a parse tree produced by plsqlParser#expression_list.
    def exitExpression_list(self, ctx:plsqlParser.Expression_listContext):
        pass


    # Enter a parse tree produced by plsqlParser#condition.
    def enterCondition(self, ctx:plsqlParser.ConditionContext):
        pass

    # Exit a parse tree produced by plsqlParser#condition.
    def exitCondition(self, ctx:plsqlParser.ConditionContext):
        pass


    # Enter a parse tree produced by plsqlParser#IgnoreExpr.
    def enterIgnoreExpr(self, ctx:plsqlParser.IgnoreExprContext):
        pass

    # Exit a parse tree produced by plsqlParser#IgnoreExpr.
    def exitIgnoreExpr(self, ctx:plsqlParser.IgnoreExprContext):
        pass


    # Enter a parse tree produced by plsqlParser#NotExpr.
    def enterNotExpr(self, ctx:plsqlParser.NotExprContext):
        pass

    # Exit a parse tree produced by plsqlParser#NotExpr.
    def exitNotExpr(self, ctx:plsqlParser.NotExprContext):
        pass


    # Enter a parse tree produced by plsqlParser#IsExpr.
    def enterIsExpr(self, ctx:plsqlParser.IsExprContext):
        pass

    # Exit a parse tree produced by plsqlParser#IsExpr.
    def exitIsExpr(self, ctx:plsqlParser.IsExprContext):
        pass


    # Enter a parse tree produced by plsqlParser#OrExpr.
    def enterOrExpr(self, ctx:plsqlParser.OrExprContext):
        pass

    # Exit a parse tree produced by plsqlParser#OrExpr.
    def exitOrExpr(self, ctx:plsqlParser.OrExprContext):
        pass


    # Enter a parse tree produced by plsqlParser#AndExpr.
    def enterAndExpr(self, ctx:plsqlParser.AndExprContext):
        pass

    # Exit a parse tree produced by plsqlParser#AndExpr.
    def exitAndExpr(self, ctx:plsqlParser.AndExprContext):
        pass


    # Enter a parse tree produced by plsqlParser#ParenExpr.
    def enterParenExpr(self, ctx:plsqlParser.ParenExprContext):
        pass

    # Exit a parse tree produced by plsqlParser#ParenExpr.
    def exitParenExpr(self, ctx:plsqlParser.ParenExprContext):
        pass


    # Enter a parse tree produced by plsqlParser#MemberExpr.
    def enterMemberExpr(self, ctx:plsqlParser.MemberExprContext):
        pass

    # Exit a parse tree produced by plsqlParser#MemberExpr.
    def exitMemberExpr(self, ctx:plsqlParser.MemberExprContext):
        pass


    # Enter a parse tree produced by plsqlParser#InExpr.
    def enterInExpr(self, ctx:plsqlParser.InExprContext):
        pass

    # Exit a parse tree produced by plsqlParser#InExpr.
    def exitInExpr(self, ctx:plsqlParser.InExprContext):
        pass


    # Enter a parse tree produced by plsqlParser#RelExpr.
    def enterRelExpr(self, ctx:plsqlParser.RelExprContext):
        pass

    # Exit a parse tree produced by plsqlParser#RelExpr.
    def exitRelExpr(self, ctx:plsqlParser.RelExprContext):
        pass


    # Enter a parse tree produced by plsqlParser#CursorExpr.
    def enterCursorExpr(self, ctx:plsqlParser.CursorExprContext):
        pass

    # Exit a parse tree produced by plsqlParser#CursorExpr.
    def exitCursorExpr(self, ctx:plsqlParser.CursorExprContext):
        pass


    # Enter a parse tree produced by plsqlParser#is_part.
    def enterIs_part(self, ctx:plsqlParser.Is_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#is_part.
    def exitIs_part(self, ctx:plsqlParser.Is_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#in_part.
    def enterIn_part(self, ctx:plsqlParser.In_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#in_part.
    def exitIn_part(self, ctx:plsqlParser.In_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#cursor_part.
    def enterCursor_part(self, ctx:plsqlParser.Cursor_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#cursor_part.
    def exitCursor_part(self, ctx:plsqlParser.Cursor_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#multiset_type.
    def enterMultiset_type(self, ctx:plsqlParser.Multiset_typeContext):
        pass

    # Exit a parse tree produced by plsqlParser#multiset_type.
    def exitMultiset_type(self, ctx:plsqlParser.Multiset_typeContext):
        pass


    # Enter a parse tree produced by plsqlParser#relational_operator.
    def enterRelational_operator(self, ctx:plsqlParser.Relational_operatorContext):
        pass

    # Exit a parse tree produced by plsqlParser#relational_operator.
    def exitRelational_operator(self, ctx:plsqlParser.Relational_operatorContext):
        pass


    # Enter a parse tree produced by plsqlParser#like_type.
    def enterLike_type(self, ctx:plsqlParser.Like_typeContext):
        pass

    # Exit a parse tree produced by plsqlParser#like_type.
    def exitLike_type(self, ctx:plsqlParser.Like_typeContext):
        pass


    # Enter a parse tree produced by plsqlParser#like_escape_part.
    def enterLike_escape_part(self, ctx:plsqlParser.Like_escape_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#like_escape_part.
    def exitLike_escape_part(self, ctx:plsqlParser.Like_escape_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#in_elements.
    def enterIn_elements(self, ctx:plsqlParser.In_elementsContext):
        pass

    # Exit a parse tree produced by plsqlParser#in_elements.
    def exitIn_elements(self, ctx:plsqlParser.In_elementsContext):
        pass


    # Enter a parse tree produced by plsqlParser#between_elements.
    def enterBetween_elements(self, ctx:plsqlParser.Between_elementsContext):
        pass

    # Exit a parse tree produced by plsqlParser#between_elements.
    def exitBetween_elements(self, ctx:plsqlParser.Between_elementsContext):
        pass


    # Enter a parse tree produced by plsqlParser#concatenation.
    def enterConcatenation(self, ctx:plsqlParser.ConcatenationContext):
        pass

    # Exit a parse tree produced by plsqlParser#concatenation.
    def exitConcatenation(self, ctx:plsqlParser.ConcatenationContext):
        pass


    # Enter a parse tree produced by plsqlParser#BinaryExpr.
    def enterBinaryExpr(self, ctx:plsqlParser.BinaryExprContext):
        pass

    # Exit a parse tree produced by plsqlParser#BinaryExpr.
    def exitBinaryExpr(self, ctx:plsqlParser.BinaryExprContext):
        pass


    # Enter a parse tree produced by plsqlParser#ParenBinaryExpr.
    def enterParenBinaryExpr(self, ctx:plsqlParser.ParenBinaryExprContext):
        pass

    # Exit a parse tree produced by plsqlParser#ParenBinaryExpr.
    def exitParenBinaryExpr(self, ctx:plsqlParser.ParenBinaryExprContext):
        pass


    # Enter a parse tree produced by plsqlParser#IgnoreBinaryExpr.
    def enterIgnoreBinaryExpr(self, ctx:plsqlParser.IgnoreBinaryExprContext):
        pass

    # Exit a parse tree produced by plsqlParser#IgnoreBinaryExpr.
    def exitIgnoreBinaryExpr(self, ctx:plsqlParser.IgnoreBinaryExprContext):
        pass


    # Enter a parse tree produced by plsqlParser#interval_expression.
    def enterInterval_expression(self, ctx:plsqlParser.Interval_expressionContext):
        pass

    # Exit a parse tree produced by plsqlParser#interval_expression.
    def exitInterval_expression(self, ctx:plsqlParser.Interval_expressionContext):
        pass


    # Enter a parse tree produced by plsqlParser#model_expression.
    def enterModel_expression(self, ctx:plsqlParser.Model_expressionContext):
        pass

    # Exit a parse tree produced by plsqlParser#model_expression.
    def exitModel_expression(self, ctx:plsqlParser.Model_expressionContext):
        pass


    # Enter a parse tree produced by plsqlParser#model_expression_element.
    def enterModel_expression_element(self, ctx:plsqlParser.Model_expression_elementContext):
        pass

    # Exit a parse tree produced by plsqlParser#model_expression_element.
    def exitModel_expression_element(self, ctx:plsqlParser.Model_expression_elementContext):
        pass


    # Enter a parse tree produced by plsqlParser#single_column_for_loop.
    def enterSingle_column_for_loop(self, ctx:plsqlParser.Single_column_for_loopContext):
        pass

    # Exit a parse tree produced by plsqlParser#single_column_for_loop.
    def exitSingle_column_for_loop(self, ctx:plsqlParser.Single_column_for_loopContext):
        pass


    # Enter a parse tree produced by plsqlParser#for_like_part.
    def enterFor_like_part(self, ctx:plsqlParser.For_like_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#for_like_part.
    def exitFor_like_part(self, ctx:plsqlParser.For_like_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#for_increment_decrement_type.
    def enterFor_increment_decrement_type(self, ctx:plsqlParser.For_increment_decrement_typeContext):
        pass

    # Exit a parse tree produced by plsqlParser#for_increment_decrement_type.
    def exitFor_increment_decrement_type(self, ctx:plsqlParser.For_increment_decrement_typeContext):
        pass


    # Enter a parse tree produced by plsqlParser#multi_column_for_loop.
    def enterMulti_column_for_loop(self, ctx:plsqlParser.Multi_column_for_loopContext):
        pass

    # Exit a parse tree produced by plsqlParser#multi_column_for_loop.
    def exitMulti_column_for_loop(self, ctx:plsqlParser.Multi_column_for_loopContext):
        pass


    # Enter a parse tree produced by plsqlParser#UnaryExpr.
    def enterUnaryExpr(self, ctx:plsqlParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by plsqlParser#UnaryExpr.
    def exitUnaryExpr(self, ctx:plsqlParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by plsqlParser#IgnoreUnaryExpr.
    def enterIgnoreUnaryExpr(self, ctx:plsqlParser.IgnoreUnaryExprContext):
        pass

    # Exit a parse tree produced by plsqlParser#IgnoreUnaryExpr.
    def exitIgnoreUnaryExpr(self, ctx:plsqlParser.IgnoreUnaryExprContext):
        pass


    # Enter a parse tree produced by plsqlParser#case_statement.
    def enterCase_statement(self, ctx:plsqlParser.Case_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#case_statement.
    def exitCase_statement(self, ctx:plsqlParser.Case_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#simple_case_statement.
    def enterSimple_case_statement(self, ctx:plsqlParser.Simple_case_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#simple_case_statement.
    def exitSimple_case_statement(self, ctx:plsqlParser.Simple_case_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#simple_case_when_part.
    def enterSimple_case_when_part(self, ctx:plsqlParser.Simple_case_when_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#simple_case_when_part.
    def exitSimple_case_when_part(self, ctx:plsqlParser.Simple_case_when_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#searched_case_statement.
    def enterSearched_case_statement(self, ctx:plsqlParser.Searched_case_statementContext):
        pass

    # Exit a parse tree produced by plsqlParser#searched_case_statement.
    def exitSearched_case_statement(self, ctx:plsqlParser.Searched_case_statementContext):
        pass


    # Enter a parse tree produced by plsqlParser#searched_case_when_part.
    def enterSearched_case_when_part(self, ctx:plsqlParser.Searched_case_when_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#searched_case_when_part.
    def exitSearched_case_when_part(self, ctx:plsqlParser.Searched_case_when_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#case_else_part.
    def enterCase_else_part(self, ctx:plsqlParser.Case_else_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#case_else_part.
    def exitCase_else_part(self, ctx:plsqlParser.Case_else_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#atom.
    def enterAtom(self, ctx:plsqlParser.AtomContext):
        pass

    # Exit a parse tree produced by plsqlParser#atom.
    def exitAtom(self, ctx:plsqlParser.AtomContext):
        pass


    # Enter a parse tree produced by plsqlParser#expression_or_vector.
    def enterExpression_or_vector(self, ctx:plsqlParser.Expression_or_vectorContext):
        pass

    # Exit a parse tree produced by plsqlParser#expression_or_vector.
    def exitExpression_or_vector(self, ctx:plsqlParser.Expression_or_vectorContext):
        pass


    # Enter a parse tree produced by plsqlParser#vector_expr.
    def enterVector_expr(self, ctx:plsqlParser.Vector_exprContext):
        pass

    # Exit a parse tree produced by plsqlParser#vector_expr.
    def exitVector_expr(self, ctx:plsqlParser.Vector_exprContext):
        pass


    # Enter a parse tree produced by plsqlParser#quantified_expression.
    def enterQuantified_expression(self, ctx:plsqlParser.Quantified_expressionContext):
        pass

    # Exit a parse tree produced by plsqlParser#quantified_expression.
    def exitQuantified_expression(self, ctx:plsqlParser.Quantified_expressionContext):
        pass


    # Enter a parse tree produced by plsqlParser#standard_function.
    def enterStandard_function(self, ctx:plsqlParser.Standard_functionContext):
        pass

    # Exit a parse tree produced by plsqlParser#standard_function.
    def exitStandard_function(self, ctx:plsqlParser.Standard_functionContext):
        pass


    # Enter a parse tree produced by plsqlParser#over_clause_keyword.
    def enterOver_clause_keyword(self, ctx:plsqlParser.Over_clause_keywordContext):
        pass

    # Exit a parse tree produced by plsqlParser#over_clause_keyword.
    def exitOver_clause_keyword(self, ctx:plsqlParser.Over_clause_keywordContext):
        pass


    # Enter a parse tree produced by plsqlParser#within_or_over_clause_keyword.
    def enterWithin_or_over_clause_keyword(self, ctx:plsqlParser.Within_or_over_clause_keywordContext):
        pass

    # Exit a parse tree produced by plsqlParser#within_or_over_clause_keyword.
    def exitWithin_or_over_clause_keyword(self, ctx:plsqlParser.Within_or_over_clause_keywordContext):
        pass


    # Enter a parse tree produced by plsqlParser#standard_prediction_function_keyword.
    def enterStandard_prediction_function_keyword(self, ctx:plsqlParser.Standard_prediction_function_keywordContext):
        pass

    # Exit a parse tree produced by plsqlParser#standard_prediction_function_keyword.
    def exitStandard_prediction_function_keyword(self, ctx:plsqlParser.Standard_prediction_function_keywordContext):
        pass


    # Enter a parse tree produced by plsqlParser#over_clause.
    def enterOver_clause(self, ctx:plsqlParser.Over_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#over_clause.
    def exitOver_clause(self, ctx:plsqlParser.Over_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#windowing_clause.
    def enterWindowing_clause(self, ctx:plsqlParser.Windowing_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#windowing_clause.
    def exitWindowing_clause(self, ctx:plsqlParser.Windowing_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#windowing_type.
    def enterWindowing_type(self, ctx:plsqlParser.Windowing_typeContext):
        pass

    # Exit a parse tree produced by plsqlParser#windowing_type.
    def exitWindowing_type(self, ctx:plsqlParser.Windowing_typeContext):
        pass


    # Enter a parse tree produced by plsqlParser#windowing_elements.
    def enterWindowing_elements(self, ctx:plsqlParser.Windowing_elementsContext):
        pass

    # Exit a parse tree produced by plsqlParser#windowing_elements.
    def exitWindowing_elements(self, ctx:plsqlParser.Windowing_elementsContext):
        pass


    # Enter a parse tree produced by plsqlParser#using_clause.
    def enterUsing_clause(self, ctx:plsqlParser.Using_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#using_clause.
    def exitUsing_clause(self, ctx:plsqlParser.Using_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#using_element.
    def enterUsing_element(self, ctx:plsqlParser.Using_elementContext):
        pass

    # Exit a parse tree produced by plsqlParser#using_element.
    def exitUsing_element(self, ctx:plsqlParser.Using_elementContext):
        pass


    # Enter a parse tree produced by plsqlParser#collect_order_by_part.
    def enterCollect_order_by_part(self, ctx:plsqlParser.Collect_order_by_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#collect_order_by_part.
    def exitCollect_order_by_part(self, ctx:plsqlParser.Collect_order_by_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#within_or_over_part.
    def enterWithin_or_over_part(self, ctx:plsqlParser.Within_or_over_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#within_or_over_part.
    def exitWithin_or_over_part(self, ctx:plsqlParser.Within_or_over_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#cost_matrix_clause.
    def enterCost_matrix_clause(self, ctx:plsqlParser.Cost_matrix_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#cost_matrix_clause.
    def exitCost_matrix_clause(self, ctx:plsqlParser.Cost_matrix_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#xml_passing_clause.
    def enterXml_passing_clause(self, ctx:plsqlParser.Xml_passing_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#xml_passing_clause.
    def exitXml_passing_clause(self, ctx:plsqlParser.Xml_passing_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#xml_attributes_clause.
    def enterXml_attributes_clause(self, ctx:plsqlParser.Xml_attributes_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#xml_attributes_clause.
    def exitXml_attributes_clause(self, ctx:plsqlParser.Xml_attributes_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#xml_namespaces_clause.
    def enterXml_namespaces_clause(self, ctx:plsqlParser.Xml_namespaces_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#xml_namespaces_clause.
    def exitXml_namespaces_clause(self, ctx:plsqlParser.Xml_namespaces_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#xml_table_column.
    def enterXml_table_column(self, ctx:plsqlParser.Xml_table_columnContext):
        pass

    # Exit a parse tree produced by plsqlParser#xml_table_column.
    def exitXml_table_column(self, ctx:plsqlParser.Xml_table_columnContext):
        pass


    # Enter a parse tree produced by plsqlParser#xml_general_default_part.
    def enterXml_general_default_part(self, ctx:plsqlParser.Xml_general_default_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#xml_general_default_part.
    def exitXml_general_default_part(self, ctx:plsqlParser.Xml_general_default_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#xml_multiuse_expression_element.
    def enterXml_multiuse_expression_element(self, ctx:plsqlParser.Xml_multiuse_expression_elementContext):
        pass

    # Exit a parse tree produced by plsqlParser#xml_multiuse_expression_element.
    def exitXml_multiuse_expression_element(self, ctx:plsqlParser.Xml_multiuse_expression_elementContext):
        pass


    # Enter a parse tree produced by plsqlParser#xmlroot_param_version_part.
    def enterXmlroot_param_version_part(self, ctx:plsqlParser.Xmlroot_param_version_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#xmlroot_param_version_part.
    def exitXmlroot_param_version_part(self, ctx:plsqlParser.Xmlroot_param_version_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#xmlroot_param_standalone_part.
    def enterXmlroot_param_standalone_part(self, ctx:plsqlParser.Xmlroot_param_standalone_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#xmlroot_param_standalone_part.
    def exitXmlroot_param_standalone_part(self, ctx:plsqlParser.Xmlroot_param_standalone_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#xmlserialize_param_enconding_part.
    def enterXmlserialize_param_enconding_part(self, ctx:plsqlParser.Xmlserialize_param_enconding_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#xmlserialize_param_enconding_part.
    def exitXmlserialize_param_enconding_part(self, ctx:plsqlParser.Xmlserialize_param_enconding_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#xmlserialize_param_version_part.
    def enterXmlserialize_param_version_part(self, ctx:plsqlParser.Xmlserialize_param_version_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#xmlserialize_param_version_part.
    def exitXmlserialize_param_version_part(self, ctx:plsqlParser.Xmlserialize_param_version_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#xmlserialize_param_ident_part.
    def enterXmlserialize_param_ident_part(self, ctx:plsqlParser.Xmlserialize_param_ident_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#xmlserialize_param_ident_part.
    def exitXmlserialize_param_ident_part(self, ctx:plsqlParser.Xmlserialize_param_ident_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#sql_plus_command.
    def enterSql_plus_command(self, ctx:plsqlParser.Sql_plus_commandContext):
        pass

    # Exit a parse tree produced by plsqlParser#sql_plus_command.
    def exitSql_plus_command(self, ctx:plsqlParser.Sql_plus_commandContext):
        pass


    # Enter a parse tree produced by plsqlParser#whenever_command.
    def enterWhenever_command(self, ctx:plsqlParser.Whenever_commandContext):
        pass

    # Exit a parse tree produced by plsqlParser#whenever_command.
    def exitWhenever_command(self, ctx:plsqlParser.Whenever_commandContext):
        pass


    # Enter a parse tree produced by plsqlParser#set_command.
    def enterSet_command(self, ctx:plsqlParser.Set_commandContext):
        pass

    # Exit a parse tree produced by plsqlParser#set_command.
    def exitSet_command(self, ctx:plsqlParser.Set_commandContext):
        pass


    # Enter a parse tree produced by plsqlParser#exit_command.
    def enterExit_command(self, ctx:plsqlParser.Exit_commandContext):
        pass

    # Exit a parse tree produced by plsqlParser#exit_command.
    def exitExit_command(self, ctx:plsqlParser.Exit_commandContext):
        pass


    # Enter a parse tree produced by plsqlParser#prompt_command.
    def enterPrompt_command(self, ctx:plsqlParser.Prompt_commandContext):
        pass

    # Exit a parse tree produced by plsqlParser#prompt_command.
    def exitPrompt_command(self, ctx:plsqlParser.Prompt_commandContext):
        pass


    # Enter a parse tree produced by plsqlParser#show_errors_command.
    def enterShow_errors_command(self, ctx:plsqlParser.Show_errors_commandContext):
        pass

    # Exit a parse tree produced by plsqlParser#show_errors_command.
    def exitShow_errors_command(self, ctx:plsqlParser.Show_errors_commandContext):
        pass


    # Enter a parse tree produced by plsqlParser#partition_extension_clause.
    def enterPartition_extension_clause(self, ctx:plsqlParser.Partition_extension_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#partition_extension_clause.
    def exitPartition_extension_clause(self, ctx:plsqlParser.Partition_extension_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#column_alias.
    def enterColumn_alias(self, ctx:plsqlParser.Column_aliasContext):
        pass

    # Exit a parse tree produced by plsqlParser#column_alias.
    def exitColumn_alias(self, ctx:plsqlParser.Column_aliasContext):
        pass


    # Enter a parse tree produced by plsqlParser#table_alias.
    def enterTable_alias(self, ctx:plsqlParser.Table_aliasContext):
        pass

    # Exit a parse tree produced by plsqlParser#table_alias.
    def exitTable_alias(self, ctx:plsqlParser.Table_aliasContext):
        pass


    # Enter a parse tree produced by plsqlParser#alias_quoted_string.
    def enterAlias_quoted_string(self, ctx:plsqlParser.Alias_quoted_stringContext):
        pass

    # Exit a parse tree produced by plsqlParser#alias_quoted_string.
    def exitAlias_quoted_string(self, ctx:plsqlParser.Alias_quoted_stringContext):
        pass


    # Enter a parse tree produced by plsqlParser#where_clause.
    def enterWhere_clause(self, ctx:plsqlParser.Where_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#where_clause.
    def exitWhere_clause(self, ctx:plsqlParser.Where_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#current_of_clause.
    def enterCurrent_of_clause(self, ctx:plsqlParser.Current_of_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#current_of_clause.
    def exitCurrent_of_clause(self, ctx:plsqlParser.Current_of_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#into_clause.
    def enterInto_clause(self, ctx:plsqlParser.Into_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#into_clause.
    def exitInto_clause(self, ctx:plsqlParser.Into_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#xml_column_name.
    def enterXml_column_name(self, ctx:plsqlParser.Xml_column_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#xml_column_name.
    def exitXml_column_name(self, ctx:plsqlParser.Xml_column_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#cost_class_name.
    def enterCost_class_name(self, ctx:plsqlParser.Cost_class_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#cost_class_name.
    def exitCost_class_name(self, ctx:plsqlParser.Cost_class_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#attribute_name.
    def enterAttribute_name(self, ctx:plsqlParser.Attribute_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#attribute_name.
    def exitAttribute_name(self, ctx:plsqlParser.Attribute_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#savepoint_name.
    def enterSavepoint_name(self, ctx:plsqlParser.Savepoint_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#savepoint_name.
    def exitSavepoint_name(self, ctx:plsqlParser.Savepoint_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#rollback_segment_name.
    def enterRollback_segment_name(self, ctx:plsqlParser.Rollback_segment_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#rollback_segment_name.
    def exitRollback_segment_name(self, ctx:plsqlParser.Rollback_segment_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#table_var_name.
    def enterTable_var_name(self, ctx:plsqlParser.Table_var_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#table_var_name.
    def exitTable_var_name(self, ctx:plsqlParser.Table_var_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#schema_name.
    def enterSchema_name(self, ctx:plsqlParser.Schema_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#schema_name.
    def exitSchema_name(self, ctx:plsqlParser.Schema_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#routine_name.
    def enterRoutine_name(self, ctx:plsqlParser.Routine_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#routine_name.
    def exitRoutine_name(self, ctx:plsqlParser.Routine_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#package_name.
    def enterPackage_name(self, ctx:plsqlParser.Package_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#package_name.
    def exitPackage_name(self, ctx:plsqlParser.Package_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#implementation_type_name.
    def enterImplementation_type_name(self, ctx:plsqlParser.Implementation_type_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#implementation_type_name.
    def exitImplementation_type_name(self, ctx:plsqlParser.Implementation_type_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#parameter_name.
    def enterParameter_name(self, ctx:plsqlParser.Parameter_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#parameter_name.
    def exitParameter_name(self, ctx:plsqlParser.Parameter_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#reference_model_name.
    def enterReference_model_name(self, ctx:plsqlParser.Reference_model_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#reference_model_name.
    def exitReference_model_name(self, ctx:plsqlParser.Reference_model_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#main_model_name.
    def enterMain_model_name(self, ctx:plsqlParser.Main_model_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#main_model_name.
    def exitMain_model_name(self, ctx:plsqlParser.Main_model_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#aggregate_function_name.
    def enterAggregate_function_name(self, ctx:plsqlParser.Aggregate_function_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#aggregate_function_name.
    def exitAggregate_function_name(self, ctx:plsqlParser.Aggregate_function_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#query_name.
    def enterQuery_name(self, ctx:plsqlParser.Query_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#query_name.
    def exitQuery_name(self, ctx:plsqlParser.Query_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#constraint_name.
    def enterConstraint_name(self, ctx:plsqlParser.Constraint_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#constraint_name.
    def exitConstraint_name(self, ctx:plsqlParser.Constraint_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#label_name.
    def enterLabel_name(self, ctx:plsqlParser.Label_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#label_name.
    def exitLabel_name(self, ctx:plsqlParser.Label_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#type_name.
    def enterType_name(self, ctx:plsqlParser.Type_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#type_name.
    def exitType_name(self, ctx:plsqlParser.Type_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#sequence_name.
    def enterSequence_name(self, ctx:plsqlParser.Sequence_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#sequence_name.
    def exitSequence_name(self, ctx:plsqlParser.Sequence_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#exception_name.
    def enterException_name(self, ctx:plsqlParser.Exception_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#exception_name.
    def exitException_name(self, ctx:plsqlParser.Exception_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#function_name.
    def enterFunction_name(self, ctx:plsqlParser.Function_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#function_name.
    def exitFunction_name(self, ctx:plsqlParser.Function_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#procedure_name.
    def enterProcedure_name(self, ctx:plsqlParser.Procedure_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#procedure_name.
    def exitProcedure_name(self, ctx:plsqlParser.Procedure_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#trigger_name.
    def enterTrigger_name(self, ctx:plsqlParser.Trigger_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#trigger_name.
    def exitTrigger_name(self, ctx:plsqlParser.Trigger_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#variable_name.
    def enterVariable_name(self, ctx:plsqlParser.Variable_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#variable_name.
    def exitVariable_name(self, ctx:plsqlParser.Variable_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#index_name.
    def enterIndex_name(self, ctx:plsqlParser.Index_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#index_name.
    def exitIndex_name(self, ctx:plsqlParser.Index_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#cursor_name.
    def enterCursor_name(self, ctx:plsqlParser.Cursor_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#cursor_name.
    def exitCursor_name(self, ctx:plsqlParser.Cursor_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#record_name.
    def enterRecord_name(self, ctx:plsqlParser.Record_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#record_name.
    def exitRecord_name(self, ctx:plsqlParser.Record_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#collection_name.
    def enterCollection_name(self, ctx:plsqlParser.Collection_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#collection_name.
    def exitCollection_name(self, ctx:plsqlParser.Collection_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#link_name.
    def enterLink_name(self, ctx:plsqlParser.Link_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#link_name.
    def exitLink_name(self, ctx:plsqlParser.Link_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#column_name.
    def enterColumn_name(self, ctx:plsqlParser.Column_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#column_name.
    def exitColumn_name(self, ctx:plsqlParser.Column_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#tableview_name.
    def enterTableview_name(self, ctx:plsqlParser.Tableview_nameContext):
        pass

    # Exit a parse tree produced by plsqlParser#tableview_name.
    def exitTableview_name(self, ctx:plsqlParser.Tableview_nameContext):
        pass


    # Enter a parse tree produced by plsqlParser#dot_id.
    def enterDot_id(self, ctx:plsqlParser.Dot_idContext):
        pass

    # Exit a parse tree produced by plsqlParser#dot_id.
    def exitDot_id(self, ctx:plsqlParser.Dot_idContext):
        pass


    # Enter a parse tree produced by plsqlParser#star.
    def enterStar(self, ctx:plsqlParser.StarContext):
        pass

    # Exit a parse tree produced by plsqlParser#star.
    def exitStar(self, ctx:plsqlParser.StarContext):
        pass


    # Enter a parse tree produced by plsqlParser#keep_clause.
    def enterKeep_clause(self, ctx:plsqlParser.Keep_clauseContext):
        pass

    # Exit a parse tree produced by plsqlParser#keep_clause.
    def exitKeep_clause(self, ctx:plsqlParser.Keep_clauseContext):
        pass


    # Enter a parse tree produced by plsqlParser#function_argument.
    def enterFunction_argument(self, ctx:plsqlParser.Function_argumentContext):
        pass

    # Exit a parse tree produced by plsqlParser#function_argument.
    def exitFunction_argument(self, ctx:plsqlParser.Function_argumentContext):
        pass


    # Enter a parse tree produced by plsqlParser#function_argument_analytic.
    def enterFunction_argument_analytic(self, ctx:plsqlParser.Function_argument_analyticContext):
        pass

    # Exit a parse tree produced by plsqlParser#function_argument_analytic.
    def exitFunction_argument_analytic(self, ctx:plsqlParser.Function_argument_analyticContext):
        pass


    # Enter a parse tree produced by plsqlParser#function_argument_modeling.
    def enterFunction_argument_modeling(self, ctx:plsqlParser.Function_argument_modelingContext):
        pass

    # Exit a parse tree produced by plsqlParser#function_argument_modeling.
    def exitFunction_argument_modeling(self, ctx:plsqlParser.Function_argument_modelingContext):
        pass


    # Enter a parse tree produced by plsqlParser#respect_or_ignore_nulls.
    def enterRespect_or_ignore_nulls(self, ctx:plsqlParser.Respect_or_ignore_nullsContext):
        pass

    # Exit a parse tree produced by plsqlParser#respect_or_ignore_nulls.
    def exitRespect_or_ignore_nulls(self, ctx:plsqlParser.Respect_or_ignore_nullsContext):
        pass


    # Enter a parse tree produced by plsqlParser#argument.
    def enterArgument(self, ctx:plsqlParser.ArgumentContext):
        pass

    # Exit a parse tree produced by plsqlParser#argument.
    def exitArgument(self, ctx:plsqlParser.ArgumentContext):
        pass


    # Enter a parse tree produced by plsqlParser#type_spec.
    def enterType_spec(self, ctx:plsqlParser.Type_specContext):
        pass

    # Exit a parse tree produced by plsqlParser#type_spec.
    def exitType_spec(self, ctx:plsqlParser.Type_specContext):
        pass


    # Enter a parse tree produced by plsqlParser#datatype.
    def enterDatatype(self, ctx:plsqlParser.DatatypeContext):
        pass

    # Exit a parse tree produced by plsqlParser#datatype.
    def exitDatatype(self, ctx:plsqlParser.DatatypeContext):
        pass


    # Enter a parse tree produced by plsqlParser#precision_part.
    def enterPrecision_part(self, ctx:plsqlParser.Precision_partContext):
        pass

    # Exit a parse tree produced by plsqlParser#precision_part.
    def exitPrecision_part(self, ctx:plsqlParser.Precision_partContext):
        pass


    # Enter a parse tree produced by plsqlParser#native_datatype_element.
    def enterNative_datatype_element(self, ctx:plsqlParser.Native_datatype_elementContext):
        pass

    # Exit a parse tree produced by plsqlParser#native_datatype_element.
    def exitNative_datatype_element(self, ctx:plsqlParser.Native_datatype_elementContext):
        pass


    # Enter a parse tree produced by plsqlParser#bind_variable.
    def enterBind_variable(self, ctx:plsqlParser.Bind_variableContext):
        pass

    # Exit a parse tree produced by plsqlParser#bind_variable.
    def exitBind_variable(self, ctx:plsqlParser.Bind_variableContext):
        pass


    # Enter a parse tree produced by plsqlParser#FuncCall.
    def enterFuncCall(self, ctx:plsqlParser.FuncCallContext):
        pass

    # Exit a parse tree produced by plsqlParser#FuncCall.
    def exitFuncCall(self, ctx:plsqlParser.FuncCallContext):
        pass


    # Enter a parse tree produced by plsqlParser#Identifier.
    def enterIdentifier(self, ctx:plsqlParser.IdentifierContext):
        pass

    # Exit a parse tree produced by plsqlParser#Identifier.
    def exitIdentifier(self, ctx:plsqlParser.IdentifierContext):
        pass


    # Enter a parse tree produced by plsqlParser#table_element.
    def enterTable_element(self, ctx:plsqlParser.Table_elementContext):
        pass

    # Exit a parse tree produced by plsqlParser#table_element.
    def exitTable_element(self, ctx:plsqlParser.Table_elementContext):
        pass


    # Enter a parse tree produced by plsqlParser#constant.
    def enterConstant(self, ctx:plsqlParser.ConstantContext):
        pass

    # Exit a parse tree produced by plsqlParser#constant.
    def exitConstant(self, ctx:plsqlParser.ConstantContext):
        pass


    # Enter a parse tree produced by plsqlParser#numeric.
    def enterNumeric(self, ctx:plsqlParser.NumericContext):
        pass

    # Exit a parse tree produced by plsqlParser#numeric.
    def exitNumeric(self, ctx:plsqlParser.NumericContext):
        pass


    # Enter a parse tree produced by plsqlParser#numeric_negative.
    def enterNumeric_negative(self, ctx:plsqlParser.Numeric_negativeContext):
        pass

    # Exit a parse tree produced by plsqlParser#numeric_negative.
    def exitNumeric_negative(self, ctx:plsqlParser.Numeric_negativeContext):
        pass


    # Enter a parse tree produced by plsqlParser#quoted_string.
    def enterQuoted_string(self, ctx:plsqlParser.Quoted_stringContext):
        pass

    # Exit a parse tree produced by plsqlParser#quoted_string.
    def exitQuoted_string(self, ctx:plsqlParser.Quoted_stringContext):
        pass


    # Enter a parse tree produced by plsqlParser#r_id.
    def enterR_id(self, ctx:plsqlParser.R_idContext):
        pass

    # Exit a parse tree produced by plsqlParser#r_id.
    def exitR_id(self, ctx:plsqlParser.R_idContext):
        pass


    # Enter a parse tree produced by plsqlParser#id_expression.
    def enterId_expression(self, ctx:plsqlParser.Id_expressionContext):
        pass

    # Exit a parse tree produced by plsqlParser#id_expression.
    def exitId_expression(self, ctx:plsqlParser.Id_expressionContext):
        pass


    # Enter a parse tree produced by plsqlParser#not_equal_op.
    def enterNot_equal_op(self, ctx:plsqlParser.Not_equal_opContext):
        pass

    # Exit a parse tree produced by plsqlParser#not_equal_op.
    def exitNot_equal_op(self, ctx:plsqlParser.Not_equal_opContext):
        pass


    # Enter a parse tree produced by plsqlParser#greater_than_or_equals_op.
    def enterGreater_than_or_equals_op(self, ctx:plsqlParser.Greater_than_or_equals_opContext):
        pass

    # Exit a parse tree produced by plsqlParser#greater_than_or_equals_op.
    def exitGreater_than_or_equals_op(self, ctx:plsqlParser.Greater_than_or_equals_opContext):
        pass


    # Enter a parse tree produced by plsqlParser#less_than_or_equals_op.
    def enterLess_than_or_equals_op(self, ctx:plsqlParser.Less_than_or_equals_opContext):
        pass

    # Exit a parse tree produced by plsqlParser#less_than_or_equals_op.
    def exitLess_than_or_equals_op(self, ctx:plsqlParser.Less_than_or_equals_opContext):
        pass


    # Enter a parse tree produced by plsqlParser#concatenation_op.
    def enterConcatenation_op(self, ctx:plsqlParser.Concatenation_opContext):
        pass

    # Exit a parse tree produced by plsqlParser#concatenation_op.
    def exitConcatenation_op(self, ctx:plsqlParser.Concatenation_opContext):
        pass


    # Enter a parse tree produced by plsqlParser#outer_join_sign.
    def enterOuter_join_sign(self, ctx:plsqlParser.Outer_join_signContext):
        pass

    # Exit a parse tree produced by plsqlParser#outer_join_sign.
    def exitOuter_join_sign(self, ctx:plsqlParser.Outer_join_signContext):
        pass


    # Enter a parse tree produced by plsqlParser#regular_id.
    def enterRegular_id(self, ctx:plsqlParser.Regular_idContext):
        pass

    # Exit a parse tree produced by plsqlParser#regular_id.
    def exitRegular_id(self, ctx:plsqlParser.Regular_idContext):
        pass


