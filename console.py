#!/usr/bin/python3
""" Entry point for the HBNB command interpreter """
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class_names = ['BaseModel', 'User', 'State', 'City', 'Place', 'Amenity', 'Review']

class HBNBCommand(cmd.Cmd):
    """ Command interpreter for the HBNB project """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ Quit the command interpreter """
        return True

    def do_EOF(self, arg):
        """ Exit the command interpreter using EOF (Ctrl+D) """
        print()
        return True

    def emptyline(self):
        """ Do nothing on empty input line """
        pass

    def precmd(self, line):
        """ Preprocess command to handle <class>.command() syntax """
        if '.' in line:
            parts = line.split('.')
            cls_name = parts[0]
            cmd_part = parts[1].split('(')
            command = cmd_part[0]
            args = cmd_part[1].strip(')')
            if args:
                args = args.replace('"', '').replace(',', '')
                line = f"{command} {cls_name} {args}"
            else:
                line = f"{command} {cls_name}"
        return cmd.Cmd.precmd(self, line)

    def do_create(self, arg):
        """ Create a new instance of a class """
        if not arg:
            print("** class name missing **")
            return
        if arg not in class_names:
            print("** class doesn't exist **")
            return
        new_instance = eval(arg)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """ Show an instance of a class by id """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in class_names:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, arg):
        """ Delete an instance of a class by id """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in class_names:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """ Show all instances of a class, or all instances
        if no class is specified """
        if arg and arg not in class_names:
            print("** class doesn't exist **")
            return
        instances = storage.all()
        if arg:
            objs = [str(obj) for key, obj in instances.items()
                    if key.startswith(arg)]
        else:
            objs = [str(obj) for obj in instances.values()]
        print(objs)

    def do_update(self, arg):
        """ Update an instance of a class by id """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in class_names:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return
        setattr(obj, args[2], args[3])
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

