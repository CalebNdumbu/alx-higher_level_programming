# !/usr/bin/python3 
"""unittests for base.py"""

import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.base import Base



class TestBase_init(unittest.TestCase):
    """Define tests for initialization of Base class"""

    def test_no_args(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, obj2.id - 1)

    def test_None(self):
        obj1 = Base(None)
        obj2 = Base(None)
        self.assertEqual(obj1.id, obj2.id -1)

    def test_unique(self):
        obj = Base(12)
        self.assertEqual(12, obj.id)

    def test_instances_after_unique(self):
        obj1 = Base()
        obj2 = Base(12)
        obj3 = Base()
        self.assertEqual(obj1.id, obj3.id - 1)

    def test_public(self):
        obj = Base(20)
        obj.id = 34
        self.assertEqual(34, obj.id)

    def test_private(self):
        with self.assertRaises(AttributeError):
            print(Base(34).__nb_objects)

    def test_str_id(self):
        self.assertEqual("world", Base("world").id)

if __name__ == "__main__":
    unittest.main()