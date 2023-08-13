#!/usr/bin/python3
# A file that bear a test file for BaseModel class.

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestClassBaseModel(unittest.TestCase):
    """
    A test cases for BaseModel Class.
    """

    def test_attributes_existance(self):
        """Testing the existance of atttributes."""
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_generate_id(self):
        """Testing the generating ids."""
        my_model1 = BaseModel()
        my_model2 = BaseModel()
        self.assertNotEqual(my_model1.id, my_model2.id)

    def test_created_at(self):
        """Testing to get created at which time."""
        my_model = BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)

    def test_updated_at(self):
        """Testing to get updated at which time."""
        my_model = BaseModel()
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_method_str(self):
        """Testing str method."""
        my_model = BaseModel()
        str_representation = "[BaseModel] ({})".format(my_model.id)
        str_representation += " {}".format(my_model.__dict__)
        self.assertEqual(str(my_model), str_representation)

    def test_method_str(self):
        """Testing save method in BaseModal class"""
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(original_updated_at, my_model.updated_at)

    def test_method_to_dict(self):
        """Testing to_dict function for BaseModel class."""
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(my_model_dict['created_at'], str)
        self.assertIsInstance(my_model_dict['updated_at'], str)
        self.assertEqual(my_model_dict['id'], my_model.id)

    def test_to_dict_with_kwargs(self):
        """Testing to_dict with kwargs for BaseModel class."""

        kwargs = {
            'id': 'My-id',
            'created_at': '2023-08-08T12:00:00.000000',
            'updated_at': '2023-08-08T12:30:00.000000',
            'name': 'Welcome'
        }
        my_model = BaseModel(**kwargs)
        my_dict = my_model.to_dict()
        self.assertEqual(my_dict['__class__'], 'BaseModel')
        self.assertEqual(my_dict['id'], 'My-id')
        self.assertEqual(my_dict['created_at'], '2023-08-08T12:00:00.000000')
        self.assertEqual(my_dict['updated_at'], '2023-08-08T12:30:00.000000')
        self.assertEqual(my_dict['name'], 'Welcome')


if __name__ == '__main__':
    unittest.main()
