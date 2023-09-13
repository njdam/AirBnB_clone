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
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def parser(arg):
    cur_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)

    if cur_braces is None:
        if brackets is None:
            return [j.strip(",") for j in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            ret_list = [j.strip(",") for j in lexer]
            ret_list.append(brackets.group())
            return (ret_list)
    else:
        lexer = split(arg[:cur_braces.span()[0]])
        ret_list = [j.strip(",") for j in lexer]
        ret_list.append(cur_braces.group())
        return (ret_list)


class HBNBCommand(cmd.Cmd):
    """This class contains the entry point of the command interpreter
       for the AirBnB clone project.

       Attributes:
           prompt (str): is a command prompt.
    """

    prompt = "(hbnb) "
    __classes = ["BaseModel", "User", "State", "City", "Amenity"]
    __classes += ["Place", "Review"]

    def default(self, arg):
        """Default behavior when input is invalid for cmd behavior"""
        arg_dict = {
                "show": self.do_show,
                "create": self.do_create,
                "destroy": self.do_destroy,
                "update": self.do_update,
                "all": self.do_all,
                "count": self.do_count,
                }

        matched = re.search(r"\.", arg)
        if matched is not None:
            args = [arg[:matched.span()[0]], arg[matched.span()[1]:]]
            matched = re.search(r"\((.*?)\)", args[1])
            if matched is not None:
                cmds = [args[1][:matched.span()[0]], matched.group()[1:-1]]
                if cmds[0] in arg_dict.keys():
                    call = "{} {}".format(args[0], cmds[1])
                    return (arg_dict[cmds[0]](call))

        print("*** Unknown synthax: {}".format(arg))
        return (False)

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF works like quit.
        """
        return True

    def emptyline(self):
        """This method is called when an empty line is entered in response
           to the prompt.

           It's to make sure that an empty line + ENTER doesn't execute
           the last entered command.
        """
        pass

    def do_create(self, arg):
        """This command creates a new instance of BaseModel, saves it
           (to the JSON file) and prints the id.

           Usage: create <class>
        """
        args = parser(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_count(self, arg):
        """Retrieving a number of instances of a given class.

           Usage: count <class> or <class>.count()
        """
        args = parser(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            count = 0
            for obj in storage.all().values():
                if args[0] == obj.__class__.__name__:
                    count += 1
            print(count)

    def do_show(self, arg):
        """This command prints the string representation of an instance
           based on the class name and id.

           Usage: show <class> <id> or <class>.show(<id>)
        """
        args = parser(arg)
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """This command deletes an instance based on the class name and
           id (save the change into the JSON file).

           Usage: destroy <class> <id> or <class>.destroy(<id>)
        """
        args = parser(arg)
        obj_dict = starage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """This command prints all string representation of all instances
           based or not on the class name.

           Usage: all <class> or all or <class>.all()
        """
        args = parser(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(args) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(self, arg):
        """This command updates an instance based on class name and id by
           adding or updating attribute (save the change into the JSON file)

           Usage: update <class> <id> <attribute name> "<attribute value>"
        """
        args = parser(arg)
        obj_dict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return (False)
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return (False)
        if len(args) == 1:
            print("** instance id missing **")
            return (False)
        if args[0] + "." + args[1] not in obj_dict.keys():
            print("** no instance found **")
            return (False)
        if len(args) == 2:
            print("** attribute name missing **")
            return (False)
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return (False)

        if len(args) == 4:
            obj = obj_dict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                vartype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = vartype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]

        elif type(eval(args[2])) == dict:
            obj = obj_dict["{}.{}".format(args[0], args[1])]
            for k, v in eval(args[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    vartype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = vartype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    """This is to make sure that the program doesn't run when imported.
    """
    HBNBCommand().cmdloop()
