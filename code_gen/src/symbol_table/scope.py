from .class_record import ClassRecord

class Scope:

    def __init__(self, parent):
        self.parent = parent
        self.scope_name = ""
        self.scope_type = ""
        self.next = 0
        self.children = list()
        self.records = dict()
        self.containing_class = ClassRecord("prog", "program")


    def set_scope_name_and_type(self, scope_name, scope_type):
        self.scope_name = scope_name
        self.scope_type = scope_type


    def set_containing_class(self, containing_class):
        self.containing_class = containing_class

    def get_method(self, method_name):
        return self.containing_class.get_method(method_name)

    def print_scope(self):
        pass

    def put(self, key, item):
        self.records[key] = item

    def next_child(self):
        next_child = None

        if self.next >= len(self.children):
            next_child = Scope(self)
            self.children.append(next_child)
        else:
            next_child = self.children[self.next]

        self.next += 1

        return next_child

    def lookup(self, key):
        if key == "this":
            return self.containing_class
        if key in self.records:
            return self.records[key]
        else:
            if self.parent is None:
                return None
            else:
                return self.parent.lookup(key)

    def lookup_local(self, key):
        if key == "this":
            return self.containing_class
        if key in self.records:
            return self.records[key]
        else:
            return None

    def reset_scope(self):
        self.next = 0
        for i in range(len(self.children)):
            self.children[i].reset_scope()


