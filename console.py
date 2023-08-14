#!/usr/bin/env python3
"""
This module contains the entry point of the command interpreter
for the AirBnB clone project.
"""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    This class contains the entry point of the command interpreter
    for the AirBnB clone project.
    """

    prompt = "(hbnb) "
    __classes = ["BaseModel", "User", "State", "City", "Amenity"]
    __classes += ["Place", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF works like quit.
        """
        return True

    def emptyline(self):
        """
        This method is called when an empty line is entered in response
        to the prompt.

        It's to make sure that an empty line + ENTER doesn't execute
        the last entered command.
        """
        pass

    def do_create(self, arg):
        """
        This command creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.

        Usage: create <class>
        """
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        This command prints the string representation of an instance
        based on the class name and id.

        Usage: show <class> <id>
        """
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        This command deletes an instance based on the class name and
        id (save the change into the JSON file).

        Usage: destroy <class> <id>
        """
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        This command prints all string representation of all instances
        based or not on the class name.

        Usage: all <class> or all
        """
        args = split(arg)
        if len(args) == 0:
            print([str(value) for value in storage.all().values()])
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            result = [
                    str(value) for key, value in storage.all().items()
                    if key.startswith(args[0])
                    ]
            print(result)
            """
            print([str(value) for key,
                value in storage.all().items() if key.startswith(args[0])])
            """

    def do_update(self, arg):
        """
        This command updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file).

        Usage: update <class> <id> <attribute name> "<attribute value>"
        """
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            setattr(storage.all()[key], args[2], args[3].strip("\""))
            storage.save()


if __name__ == "__main__":
    """
    This is to make sure that the program doesn't run when imported.
    """
    HBNBCommand().cmdloop()
