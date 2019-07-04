from .record import Record


class ClassRecord(Record):

    def __init__(self, id, type):
        Record.__init__(self, id, type)
        self.methods = dict()
        self.fields = dict()

    def add_method(self, name, rec):
        self.methods[name] = rec

    def add_field(self, name, rec):
        self.fields[name] = rec

    def get_method(self, name):
        if name not in self.methods:
            return None
        else:
            return self.methods[name]

    def get_field(self, name):
        if name not in self.fields:
            return None
        else:
            return self.fields[name]
