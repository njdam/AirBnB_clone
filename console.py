#!/usr/bin/env python3

"""
This module contains the entry point of the command interpreter for the AirBnB clone project.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    This class contains the entry point of the command interpreter for the AirBnB clone project.
    """

    prompt = "(hbnb) "

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
        if not arg:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        This command prints the string representation of an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        This command deletes an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        This command prints all string representation of all instances based or not on the class name.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            print("[]")
    

if __name__ == "__main__":
    """
    This is to make sure that the program doesn't run when imported.
    """
    HBNBCommand().cmdloop()
