import copy
import pickle

from src.codegen.instruction import Instruction
from src.codegen.method import Method
from src.codegen.config import *


class StackMachine:
    def __init__(self, programName):
        with open(programName, 'rb') as f:
            self.classfile = pickle.load(f)
        # self.class_rep.classfile.print()
        self.data_stack = list()
        self.activation_stack = list()
        self.current_activation: Method = None
        self.code = 0
        self.instruction: Instruction = None
        self.activation = 0

    def execute(self):
        self.current_activation = self.classfile.get_method('main')
        self.current_activation.restart()
        while self.code != STOP:
            self.instruction = self.current_activation.next_instruction()
            self.code = self.instruction.code
            arg = self.instruction.argument
            if self.code == ILOAD:
                v1 = self.current_activation.get_variable_value(int(arg))
                self.data_stack.append(v1)
            elif self.code == ICONST:
                self.data_stack.append(int(arg))
            elif self.code == ISTORE:
                v1 = self.data_stack.pop()
                self.current_activation.store_variable(int(arg), v1)
            elif self.code == IADD:
                v1 = self.data_stack.pop()
                v2 = self.data_stack.pop()
                self.data_stack.append(v1 + v2)
            elif self.code == ISUB:
                v1 = self.data_stack.pop()
                v2 = self.data_stack.pop()
                self.data_stack.append(v2 - v1)
            elif self.code == IMUL:
                v1 = self.data_stack.pop()
                v2 = self.data_stack.pop()
                self.data_stack.append(v1 * v2)
            elif self.code == IDIV:
                v1 = self.data_stack.pop()
                v2 = self.data_stack.pop()
                self.data_stack.append(v2 // v1)
            elif self.code == ILT:
                v1 = self.data_stack.pop()
                v2 = self.data_stack.pop()
                if v2 < v1:
                    self.data_stack.append(1)
                else:
                    self.data_stack.append(0)
            elif self.code == IEQ:
                v1 = self.data_stack.pop()
                v2 = self.data_stack.pop()
                if v1 == v2:
                    self.data_stack.append(1)
                else:
                    self.data_stack.append(0)
            elif self.code == IAND:
                v1 = self.data_stack.pop()
                v2 = self.data_stack.pop()
                if v1 * v2 != 0:
                    self.data_stack.append(1)
                else:
                    self.data_stack.append(0)
            elif self.code == IOR:
                v1 = self.data_stack.pop()
                v2 = self.data_stack.pop()
                if v1 + v2 != 0:
                    self.data_stack.append(1)
                else:
                    self.data_stack.append(0)
            elif self.code == INOT:
                v1 = self.data_stack.pop()
                if v1 == 0:
                    self.data_stack.append(1)
                else:
                    self.data_stack.append(0)
            elif self.code == GOTO:
                v1 = int(arg)
                self.current_activation.jump_instruction(v1)
            elif self.code == IF_FALSE:
                v1 = self.data_stack.pop()
                if v1 == 0:
                    self.current_activation.jump_instruction(int(arg))
            elif self.code == INVOKEVIRTUAL:
                self.activation += 1
                self.activation_stack.append(copy.deepcopy(self.current_activation))
                self.current_activation = self.classfile.get_method(str(arg))
                self.current_activation.restart()
            elif self.code == IRETURN:
                self.activation -= 1
                self.current_activation = self.activation_stack.pop()
            elif self.code == PRINT:
                print(self.data_stack.pop())
            elif self.code == STOP:
                pass
            elif self.code == IGE:
                v1 = self.data_stack.pop()
                v2 = self.data_stack.pop()
                if v2 >= v1:
                    self.data_stack.append(1)
                else:
                    self.data_stack.append(0)
            elif self.code == ILE:
                v1 = self.data_stack.pop()
                v2 = self.data_stack.pop()
                if v2 <= v1:
                    self.data_stack.append(1)
                else:
                    self.data_stack.append(0)

