#!/usr/bin/python3

"""
This module contains the entry
point of the command interpreter
"""


# importing libraries and modules
import cmd
import models
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
    classes = {
        'BaseModel': BaseModel,
        'Amenity': Amenity,
        'Place': Place,
        'User': User,
        'State': State,
        'Review': Review,
        'City': City
    }

    def do_create(self, argv):
        """
        Creates a new instance of BaseModel,
        saves it to JSON file and prints
        its id
        """
        args = argv.split()
        # check if no argument is passed e.g create
        if argv == "":
            print("** class name missing **")

        # if classname doesn't exist
        if args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, argv):
        """
        Prints string representation of an instance
        based on class name
        """
        # splits arguments
        args = argv.split()

        # check if no argument is passed
        if argv == "":
            print("** class name missing **")

        # check if class is available
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        # check if id is input after classname
        if len(args) < 2:
            print("** instance id missing **")
            return

        objects = storage.all()
        # stores user input
        object_key = "{}.{}".format(args[0], args[1])
        # loops through checking if user input is in file.json
        if object_key in objects:
            print(objects[object_key])
        else:
            print("** no instance found **")

    def do_destroy(self, argv):
        """
        Deletes an instance based on class name
        and id. Then saves changes to JSON file
        """
        # refer to comments in show for reference
        if not argv:
            print("** class name missing **")
            return

        args = argv.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objects = storage.all()
        object_key = "{}.{}".format(args[0], args[1])
        if object_key in objects:
            del objects[object_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, argv):
        """
        Prints a string representation of all instances
        based or not on the class name
        """
        objects = storage.all()
        args = argv.split()

        # if argv:
        #    output = []
        #    for key, value in objects.items():
        #        output.append(str(value))
        #    print(output)

        if not argv or args[0] in self.classes:
            output = []
            if not argv:
                for key, value in objects.items():
                    output.append(str(value))
                # print(output)
            else:
                class_name = args[0]
                for key, value in objects.items():
                    if value.__class__.__name__ == class_name:
                        output.append(str(value))
                print(output)
        else:
            print("** class doesn't exist **")

    def do_update(self, argv):
        """
        Updates an instance based on the class name
        then saves changes to JSON file
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = argv.split()
        if not argv:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** id instance missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        attribute_name = args[2]
        attribute_value = args[3].strip('"')

        object_key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()
        object_dict = objects[object_key].__dict__
        if attribute_name in object_dict:
            object_dict[attribute_name] = type(object_dict[attribute_name]
                                               )(attribute_value)
        else:
            object_dict[attribute_name] = attribute_value

        storage.save()

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


# def run_commands(commands):
    # """
    # Read commands from a file
    # and run them in non-interactive mode
    # """
    # hbnb_command = HBNBCommand()
    # disables need for raw user command input
    # hbnb_command.use_rawinput = False
    # hbnb_command.stdout = sys.stdout
    # hbnb_command.stdin = sys.stdin
    # appends command elements to end of cmd queue
    # hbnb_command.cmdqueue.extend(commands)
    # hbnb_command.cmdloop()


if __name__ == "__main__":
    # check of cl arguments
    # if len(sys.argv) > 1:
    # Non-interactive mode entry
    # with open(sys.argv[1]) as file:
    # commands = file.read().splitlines()
    # run_commands(commands)
    # else:
    # Interactive mode entry
    HBNBCommand().cmdloop()
