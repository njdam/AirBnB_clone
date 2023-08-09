#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    A test cases for BaseModel Class.
    """

    def test_attributes_existence(self):
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_id_generation(self):
        my_model1 = BaseModel()
        my_model2 = BaseModel()
        self.assertNotEqual(my_model1.id, my_model2.id)

    def test_created_at(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)

    def test_updated_at(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str_method(self):
        my_model = BaseModel()
        str_representation = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), str_representation)

    def test_save_method(self):
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(original_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(my_model_dict['created_at'], str)
        self.assertIsInstance(my_model_dict['updated_at'], str)
        self.assertEqual(my_model_dict['id'], my_model.id)

    def test_to_dict_with_kwargs(self):
        kwargs = {
            'id': 'test-id',
            'created_at': '2023-08-08T12:00:00.000000',
            'updated_at': '2023-08-08T12:30:00.000000',
            'name': 'Test Model'
        }
        my_model = BaseModel(**kwargs)
        my_model_dict = my_model.to_dict()
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertEqual(my_model_dict['id'], 'test-id')
        self.assertEqual(my_model_dict['created_at'], '2023-08-08T12:00:00.000000')
        self.assertEqual(my_model_dict['updated_at'], '2023-08-08T12:30:00.000000')
        self.assertEqual(my_model_dict['name'], 'Test Model')


if __name__ == '__main__':
    unittest.main()
