import sys
import pickle
import os
from antlr4 import *
from src.autogen.gmarLexer import gmarLexer
from src.autogen.gmarParser import gmarParser
from src.codegen.codegen_visitor import CodeGenerationVisitor
from src.symbol_table.checkVisitor import TypeCheckVisitor
from src.symbol_table.symbol_table import SymbolTable
from src.symbol_listener import SymbolListener

def main(argv):
    argv[1] = os.path.abspath(argv[1])
    fname = argv[1].split('.')[0]
    input_stream = FileStream(argv[1])
    lexer = gmarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = gmarParser(stream)
    tree = parser.program()
    # print(tree.toStringTree())
    sym_table = SymbolTable()
    walker = ParseTreeWalker()
    symbol_listener = SymbolListener(sym_table)
    walker.walk(symbol_listener, tree)

    # sym_table.reset_table()
    # typeChecker = TypeCheckVisitor(sym_table)
    # typeChecker.visit(tree)

    sym_table.reset_table()
    visitor = CodeGenerationVisitor(sym_table)
    visitor.visit(tree)
    visitor.class_file.print()
    with open(fname + '.tjc', 'wb') as f:
        pickle.dump(visitor.class_file, f)



main(sys.argv)

