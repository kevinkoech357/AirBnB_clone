#!/usr/bin/python3

"""
This module contains the entry
point of the command interpreter
"""


# importing cmd library
import cmd
import sys


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

    def emptyline(self):
        """
        Empty line cannot be executed
        """
        pass

    # test for non-interactive mode
    # def do_greet(self, line):
    #    print(f"hello {line}")


def run_commands(commands):
    """
    Read commands from a file
    and run them in non-interactive mode
    """
    hbnb_command = HBNBCommand()
    # disables need for raw user command input
    hbnb_command.use_rawinput = False
    hbnb_command.stdout = sys.stdout
    hbnb_command.stdin = sys.stdin
    # appends command elements to end of cmd queue
    hbnb_command.cmdqueue.extend(commands)
    hbnb_command.cmdloop()


if __name__ == "__main__":
    # check of cl arguments
    if len(sys.argv) > 1:
        # Non-interactive mode entry
        with open(sys.argv[1]) as file:
            commands = file.read().splitlines()
            run_commands(commands)
    else:
        # Interactive mode entry
        HBNBCommand().cmdloop()
