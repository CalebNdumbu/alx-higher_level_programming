#!/usr/bin/python3 
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

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)



if __name__ == "__main__":
    unittest.main()