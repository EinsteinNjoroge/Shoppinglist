from unittest import TestCase
import classes.shared_funtions_helper

case = TestCase()


def test_get_attributes_from_class_returns_dict():
    case.assertIsInstance(
        classes.shared_funtions_helper.get_attributes_from_class(""), dict)
