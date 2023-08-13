#!/usr/bin/python3
"""A file that bears a test cases for class FileStorage for file
file_storage.py from models/engine/

Unittest classes:
    TestClassFileStorage_instantiation
    TestClassFileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestClassFileStorage_instantiation(unittest.TestCase):
    """Test cases for testing instantiation of class FileStorage."""

    def test_instantiation_no_args(self):
        """A function to test no args to class FileStorage."""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_instantiation_with_arg(self):
        """A function to test args to class FileStorage."""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_private_str_file_path(self):
        """A function to test private string to class FileStorage."""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_private_dict_objects(self):
        """A function to test private objects(dict) to class FileStorage."""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializer(self):
        """A function to test storage models type to class FileStorage."""
        self.assertEqual(type(models.storage), FileStorage)


class TestClassFileStorage_methods(unittest.TestCase):
    """Test cases for testing methods of class FileStorage."""

    @classmethod
    def setUp(self):
        """A function to test renaming of a file."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """A function to test removal or renaming of a file."""
        try:
            """Trying to remove json file."""
            os.remove("file.json")
        except IOError:
            pass
        try:
            """Trying to rename file to json file."""
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """A function to test all with no args."""
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        """A function to test all with args."""
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        """A function to test classes."""
        bm = BaseModel()
        us = User()
        st = State()
        cy = City()
        am = Amenity()
        pl = Place()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(pl)
        models.storage.new(rv)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("City." + cy.id, models.storage.all().keys())
        self.assertIn(cy, models.storage.all().values())
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn(am, models.storage.all().values())
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        self.assertIn("Review." + rv.id, models.storage.all().keys())
        self.assertIn(rv, models.storage.all().values())

    def test_new_with_args(self):
        """A function to test new with args."""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        """A function to test new with None."""
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        """A function for testing save function to all classes."""
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + cy.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + rv.id, save_text)

    def test_save_with_arg(self):
        """Testing savevfunction with None."""
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        """A function for testing reload function to all classes."""
        bm = BaseModel()
        us = User()
        st = State()
        cy = City()
        am = Amenity()
        pl = Place()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(pl)
        models.storage.new(rv)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("City." + cy.id, objs)
        self.assertIn("Amenity." + am.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("Review." + rv.id, objs)

    def test_reload_no_file(self):
        """A function to test reload with no file."""
        with self.assertRaises(FileNotFoundError):
            models.storage.reload()

    def test_reload_with_arg(self):
        """A function to test reload with a file."""
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
