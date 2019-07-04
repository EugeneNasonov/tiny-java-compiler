from .record import Record


class MethodRecord(Record):
    def __init__(self, id, type):
        Record.__init__(self, id, type)
        self.param_number = 0
        self.parameters = dict()

    def add_parameter(self, parameter):
        self.parameters[self.param_number] = parameter
        self.param_number += 1

    def get_local_variables(self):
        locals = list()
        for key, val in self.parameters.items():
            locals.append(val.id)
        return locals

    def contains_parameter(self, param_num, parameter):
        if parameter is None or param_num not in self.parameters:
            return False

        return self.parameters[param_num].type == parameter.type

    def __len__(self):
        return self.param_number
