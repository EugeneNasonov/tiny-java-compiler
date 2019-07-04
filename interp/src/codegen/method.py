class Variable:
    def __init__(self, code, id, value):
        self.code = code
        self.id = id
        self.value = value


class Method:
    def __init__(self):
        self.var_count = 0
        self.variables = list()
        self.variable_table = list()
        self.name2index = dict()
        self.instructions = list()
        self.instruction_counter = 0
        self.program_counter = 0

    def restart(self):
        self.program_counter = 0

    def print(self):
        for i in range(len(self.variables)):
            print(f'#{i} = {self.variables[i]} ', end='')
        if len(self.variables) > 0:
            print()
        for i in range(len(self.instructions)):
            print(f'{i:<8}{self.instructions[i]}')

    def next_instruction(self):
        res = None
        if self.program_counter < len(self.instructions):
            res = self.instructions[self.program_counter]
            self.program_counter += 1
        return res

    def jump_instruction(self, num):
        self.program_counter = num

    def getPC(self):
        return self.program_counter

    def get_index_of(self, var):
        temp = 0
        if var not in self.variables:
            self.variables.append(var)
        if var not in self.name2index:
            temp = self.var_count
            self.name2index[var] = temp
            self.var_count += 1
        else:
            temp = self.name2index[var]
        return temp

    def add_variable(self, vname):
        self.variables.append(vname)

    def add_instruction(self, ins):
        self.instructions.append(ins)
        self.instruction_counter += 1

    def get_instruction(self, index):
        return self.instructions[index]

    def get_index(self):
        return self.instruction_counter

    def get_variable_value(self, vnumber):
        return self.variable_table[vnumber].value

    def store_variable(self, index, value):
        if len(self.variable_table) > 0:
            if index >= len(self.variable_table):
                self.variable_table.append(Variable(index, "newVar", value))
            else:
                self.variable_table[index].value = value
        else:
            self.variable_table.append(Variable(index, "newVar", value))
