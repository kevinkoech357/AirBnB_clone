#!/usr/bin/python3

"""
This module contains the entry
point of the command interpreter
"""


# importing cmd library
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Child class of cmd.Cmd
    """
    # Creates a custom prompt
    prompt = "(hbnb) "
    # Creates a welcome message
    # intro = "Welcome to AirBnB Console"
    
    def do_quit(self, arg):
        """
        Quits the console
        """
        return True

    def do_EOF(self, arg):
        """
        Handles End of File input
        to exit the console
        """
        print()
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
