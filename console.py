#!/usr/bin/python3

"""
This module contains the entry
point of the command interpreter
"""


# importing libraries and modules
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Child class of cmd.Cmd
    """
    # Creates a custom prompt
    prompt = "(hbnb) "
    # Creates a welcome message
    # intro = "Welcome to AirBnB Console"
    classes = ["BaseModel", "Amenity", "City",
               "Place", "Review", "State",
               "User"]

    def do_create(self, argv):
        """
        Creates a new instance of BaseModel,
        saves it to JSON file and prints
        its id
        """
        # if no argument is passed e.g create
        if not argv:
            print("** class name missing **")
            return

        class_name = argv.strip()
        # if classname doesn't exist
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            new_instance = eval(argv)()
            new_instance.save()
            print(new_instance.id)

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
