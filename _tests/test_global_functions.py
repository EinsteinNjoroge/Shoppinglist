from unittest import TestCase

import global_functions

case = TestCase()


def test_get_attributes_from_class_returns_dict():
    case.assertIsInstance(
        global_functions.get_attributes_from_class(""), dict)
