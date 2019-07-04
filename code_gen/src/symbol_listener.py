from src.autogen.gmarListener import gmarListener
from src.autogen.gmarParser import gmarParser
from src.symbol_table.class_record import ClassRecord
from src.symbol_table.method_record import MethodRecord
from src.symbol_table.variable_record import VariableRecord

PROGRAM = "PROGRAM"
CLASS = "CLASS"
METHOD = "METHOD"


class SymbolListener(gmarListener):
    def __init__(self, stable):
        self.symbol_table = stable
        self.current_class = None
        self.current_method = None


    # Enter a parse tree produced by gmarParser#program.
    def enterProgram(self, ctx:gmarParser.ProgramContext):
        self.symbol_table.set_current_scope_name_and_type("prog", PROGRAM)



    # Enter a parse tree produced by gmarParser#mainClass.
    def enterMainClass(self, ctx:gmarParser.MainClassContext):
        type = str(ctx.getChild(0))
        id = str(ctx.getChild(1).getChild(0))

        self.current_class = ClassRecord(id, type)

        self.symbol_table.put(id, self.current_class)

        self.symbol_table.enter_scope()

        self.symbol_table.set_current_scope_name_and_type(id, CLASS)

        self.symbol_table.set_current_scope_class(self.current_class)

    # Exit a parse tree produced by gmarParser#mainClass.
    def exitMainClass(self, ctx:gmarParser.MainClassContext):
        self.symbol_table.exit_scope()


    # Enter a parse tree produced by gmarParser#mainMethod.
    def enterMainMethod(self, ctx:gmarParser.MainMethodContext):
       type = str(ctx.getChild(0))
       id = str(ctx.getChild(3))

       method = MethodRecord(id, type)

       self.symbol_table.put(id, method)

       self.symbol_table.enter_scope()

       self.symbol_table.set_current_scope_name_and_type(id, METHOD)

       self.current_class.add_method(id, method)

       self.symbol_table.set_current_scope_class(self.current_class)

    # Exit a parse tree produced by gmarParser#mainMethod.
    def exitMainMethod(self, ctx:gmarParser.MainMethodContext):
        self.symbol_table.exit_scope()




    # Enter a parse tree produced by gmarParser#classDecl.
    def enterClassDecl(self, ctx:gmarParser.ClassDeclContext):
        type = str(ctx.getChild(0))
        id = str(ctx.getChild(1))

        self.current_class = ClassRecord(id, type)

        if self.symbol_table.lookup(id) is not None:
            print(f"duplicated class name [{id}]")
            exit(0)

        self.symbol_table.put(id, self.current_class)

        self.symbol_table.enter_scope()

        self.symbol_table.set_current_scope_name_and_type(id, CLASS)

        self.symbol_table.set_current_scope_class(self.current_class)

    # Exit a parse tree produced by gmarParser#classDecl.
    def exitClassDecl(self, ctx:gmarParser.ClassDeclContext):
        self.symbol_table.exit_scope()


    # Enter a parse tree produced by gmarParser#methodDecl.
    def enterMethodDecl(self, ctx:gmarParser.MethodDeclContext):
        type = str(ctx.getChild(0).getChild(0).getChild(0))

        id = str(ctx.getChild(1).getChild(0))

        if self.current_class.get_method(id) is not None:
            print(f"Method [{id}] duplicated")
            exit(0)

        self.current_method = MethodRecord(id, type)
        self.symbol_table.put(id, self.current_method)

        self.symbol_table.enter_scope()
        self.symbol_table.set_current_scope_name_and_type(id, METHOD)
        self.current_class.add_method(id, self.current_method)
        self.symbol_table.set_current_scope_class(self.current_class)

    # Exit a parse tree produced by gmarParser#methodDecl.
    def exitMethodDecl(self, ctx:gmarParser.MethodDeclContext):
        self.symbol_table.exit_scope()


    # Enter a parse tree produced by gmarParser#fieldDecl.
    def enterFieldDecl(self, ctx:gmarParser.FieldDeclContext):
        type = str(ctx.getChild(0).getChild(0).getChild(0))

        if len(ctx.getChild(0).getChild(0).children) > 1 and ctx.getChild(0).getChild(0).getChild(1) is not None:
            type = "int_array"

        id = str(ctx.getChild(1).getChild(0))

        if self.symbol_table.lookup_local(id) is not None:
            print(f"Duplicate identifier [{id}]")
            exit(0)

        nf = VariableRecord(id, type)
        self.current_class.add_field(id, nf)
        self.symbol_table.set_current_scope_class(self.current_class)
        self.symbol_table.put(id, nf)





    # Enter a parse tree produced by gmarParser#parameter.
    def enterParameter(self, ctx:gmarParser.ParameterContext):
        type = str(ctx.getChild(0).getChild(0).getChild(0))
        id = str(ctx.getChild(1).getChild(0))

        parameter = VariableRecord(id, type)

        self.current_method.add_parameter(parameter)
        self.symbol_table.put(id, parameter)
