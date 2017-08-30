from unittest import TestCase
from classes.item import Item


class TestItem(TestCase):
    def setUp(self):
        self.item = Item("name")

    def tearDown(self):
        self.item = None

    def test_item_id_is_int(self):
        self.assertIsInstance(self.item.id, int)

    def test_item_name_is_str(self):
        self.assertIsInstance(self.item.name, str)

    def test_update_item_without_name(self):
        self.assertTrue(self.item.update(None), "Item must have a name")

    def test_update_item_with_invalid_name(self):
        self.assertTrue(self.item.update(["name"]), "Item name must be a string")

    def test_update_item(self):
        self.item.update("new name")

        self.assertEqual(
            self.item.name,
            "new name",
            msg="Method update should update the items name"
        )
