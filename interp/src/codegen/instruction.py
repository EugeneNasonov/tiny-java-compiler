from .config import *


class Instruction:
    def __init__(self, code, arg):
        self.code = code
        self.argument = arg

    @staticmethod
    def get_icode_string(code):
        return code_dict[code]

    def __str__(self):
        res = f'{self.get_icode_string(self.code):<16}'
        if self.argument is not None:
            if self.code == ISTORE or \
                    self.code == ILOAD:
                res += f'#{self.argument}'
            else:
                res += f'{self.argument}'
        return res

