#!/usr/bin/python3

"""
The entry point of the command interpreter
"""

import cmd

class Hbnb(cmd.Cmd):
    """Command lines for the command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """exit the interpreter"""
        return True

    def do_EOF(self, line):
        """exit the interpreter"""
        return True


if __name__ == "__main__":
    Hbnb().cmdloop()


