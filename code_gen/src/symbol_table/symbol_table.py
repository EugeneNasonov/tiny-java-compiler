from .scope import Scope


class SymbolTable:
    def __init__(self):
        self.root = Scope(None)
        self.current = self.root

    def get_current_class_name(self):
        return self.current.containing_class.id

    def get_current_scope_name(self):
        return self.current.scope_name

    def get_current_scope_type(self):
        return self.current.scope_type

    def set_current_scope_name_and_type(self, name, type):
        return self.current.set_scope_name_and_type(name, type)

    def enter_scope(self):
        self.current = self.current.next_child()

    def set_current_scope_class(self, containing_class):
        self.current.set_containing_class(containing_class)

    def exit_scope(self):
        self.current = self.current.parent

    def put(self, key, item):
        self.current.put(key, item)

    def lookup(self, key):
        return self.current.lookup(key)

    def lookup_local(self, key):
        return self.current.lookup_local(key)

    def reset_table(self):
        self.root.reset_scope()



