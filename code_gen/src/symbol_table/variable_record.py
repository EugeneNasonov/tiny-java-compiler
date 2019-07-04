from .record import Record

class VariableRecord(Record):
    def __init__(self, id, type):
        Record.__init__(self, id, type)
