import sys
import os

from stack_machine import StackMachine


def main(argv):
    argv[1] = os.path.abspath(argv[1])
    sm = StackMachine(argv[1])
    sm.execute()
    pass

main(sys.argv)