#!/usr/bin/python3
""" Unit tests Review Class """
from models.base_model import BaseModel
from models.review import Review
from models.user import User
from models.place import Place
import unittest
from datetime import datetime as dt


class TestReview(unittest.TestCase):
    """ Unit tests Review Class """

    def setUp(self):
        """ Initialization """
        self.place = Place()
        self.user = User()
        self.rev_1 = Review()
        self.rev_1.place_id = self.place.id
        self.rev_1.user_id = self.user.id
        self.rev_1.text = "Nice"
        self.rev_2 = Place()

    def test_Review_attributes(self):
        """Test that Review class has place_id, user_id and text
            attributes."""
        new_review = Review()
        place_id = getattr(new_review, "place_id")
        user_id = getattr(new_review, "user_id")
        text = getattr(new_review, "text")
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)

    def test_attr_base(self):
        """ Test attribut BaseModel """
        self.assertIsNotNone(self.rev_1.id)
        self.assertIsNotNone(self.rev_1.created_at)
        self.assertIsNotNone(self.rev_1.updated_at)

    def test_type_attr_base(self):
        """ Test type attribut BaseModel """
        self.assertEqual(type(self.rev_1.id), str)
        self.assertEqual(type(self.rev_1.created_at), dt)
        self.assertEqual(type(self.rev_1.updated_at), dt)

    def test_attr(self):
        """ Test attribut Review class """
        self.assertEqual(self.rev_1.text, "Nice")
        self.assertEqual(self.rev_1.place_id, self.place.id)
        self.assertEqual(self.rev_1.user_id, self.user.id)

    def test_no_arg(self):
        """ Test Review class with no attribut """
        self.assertEqual(self.rev_2.name, "")

    def test_type_args(self):
        """ Test type attribut Review """
        self.assertEqual(type(self.rev_2.name), str)

if __name__ == '__main__':
    unittest.main()
