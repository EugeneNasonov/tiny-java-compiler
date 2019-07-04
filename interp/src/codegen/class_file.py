class ClassFile:
    def __init__(self):
        self.methods = dict()

    def print(self):
        for key, val in self.methods.items():
            print(f'\nMethod: {key}')
            val.print()

    def add_method(self, mname, me):
        self.methods[mname] = me

    def get_method(self, name):
        if name == 'main':
            return next(iter(self.methods.items()))[1]
        return self.methods[name]

    def contains_method(self, mname):
        return mname in self.methods