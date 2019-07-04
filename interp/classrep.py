import pickle

class ClassRepository:
    def __init__(self, f):
        self.f = f
        with open(f, 'rb') as fs:
            self.classfile = pickle.load(fs)
    def get_method(self, name):
        meth = self.classfile.get_method(name)
        meth.restart()
        return meth


