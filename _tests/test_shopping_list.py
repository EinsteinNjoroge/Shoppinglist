from unittest import TestCase
from classes.shopping_list import ShoppingList


class TestShoppingList(TestCase):
    def setUp(self):
        self.shopping_list = ShoppingList("title")

    def tearDown(self):
        self.shopping_list = None

    def test_shopping_list_id_is_int(self):
        self.assertIsInstance(self.shopping_list.id, int)

    def test_shopping_title_is_str(self):
        self.assertIsInstance(self.shopping_list.title, str)

    def test_shopping_list_items_is_list(self):
        self.assertIsInstance(self.shopping_list.items, list)

    def test_add_item_without_name(self):
        self.assertTrue(self.shopping_list.add_item(None), "Item must have a name")

    def test_add_item_with_invalid_name(self):
        self.assertTrue(self.shopping_list.add_item(["name"]), "Item name must be a string")

    def test_add_item(self):
        # attempt to create a shopping list item
        item_name = "School shoes"
        self.shopping_list.add_item(item_name)

        self.assertEqual(
            self.shopping_list.items[0].name,
            item_name,
            msg="Method add_item should add a Item object to items"
        )

    def test_add_item(self):
        # attempt to create a shopping list item
        item_name = "School shoes"
        self.shopping_list.add_item(item_name)

        self.assertEqual(
            self.shopping_list.items[0].name,
            item_name,
            msg="Method add_item should add a Item object to items"
        )

    def test_add_item_returns_int(self):
        # add item to shopping list
        item_name = "school bag"

        self.assertIsInstance(
            self.shopping_list.add_item(item_name),
            int,
            msg="Method add_item should return id of the items added"
        )

    def test_add_duplicate_item(self):
        # add item to shopping list
        item_name = "school bag"
        self.shopping_list.add_item(item_name)

        self.assertEqual(
            self.shopping_list.add_item(item_name),
            "Item `" + item_name + "` already added"
        )

    def test_update_list_without_title(self):
        self.assertTrue(self.shopping_list.update(None), "Shopping list must have a title")

    def test_update_list_with_invalid_title(self):
        self.assertTrue(self.shopping_list.update(["new"]), "Shopping list title must be a string")

    def test_update_list(self):
        self.shopping_list.update("new shopping list")

        self.assertEqual(
            self.shopping_list.title,
            "new shopping list",
            msg="Method update should update the shopping lists title"
        )

    def test_list_shopping_list_returns_list(self):
        self.assertIsInstance(self.shopping_list.list_items(), list)

    def test_list_items(self):
        # add multiple items
        self.shopping_list.add_item("Test")
        self.shopping_list.add_item("Test 2")

        expected_list = ["Test", "Test 2"]
        self.assertTrue(set(self.shopping_list.list_items()) == set(expected_list))

    def test_remove_item_invalid_argument(self):
        self.assertEqual(
            self.shopping_list.remove_item([]), "Item id must be an Integer"
        )

    def test_remove_item_that_do_not_exist(self):
        non_existent_id = 10
        self.assertEqual(
            self.shopping_list.remove_item(non_existent_id),
            "Item does not exist"
        )

    def test_remove_item(self):
        # add multiple items
        self.shopping_list.add_item("Test")
        item_to_be_removed = self.shopping_list.add_item("Test 10")

        self.assertTrue(
            self.shopping_list.remove_item(item_to_be_removed),
            msg="Method remove_item should return True on successful completion"
        )
