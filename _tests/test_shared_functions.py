from unittest import TestCase
import classes.shared_funtions_helper

test_case = TestCase()


def test_get_attributes_from_class_returns_dict():
    test_case.assertIsInstance(
        classes.shared_funtions_helper.get_attributes_from_class(""),
        dict,
        msg="Function `get_attributes_from_class` should return a dictionary"
    )
