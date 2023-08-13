#!/usr/bin/env python3

"""
This module contains the entry point of the command interpreter for the AirBnB clone project.
"""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    This class contains the entry point of the command interpreter for the AirBnB clone project.
    """

    prompt = "(hbnb) "
    __classes = ["BaseModel"]

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF works like quit.
        """
        return True

    def emptyline(self):
        """
        This method is called when an empty line is entered in response to the prompt.
        It's to make sure that an empty line + ENTER doesn't execute the last entered command.
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        """
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()


if __name__ == "__main__":
    """
    This is to make sure that the program doesn't run when imported.
    """
    HBNBCommand().cmdloop()
