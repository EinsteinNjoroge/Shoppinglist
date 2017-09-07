from unittest import TestCase
from classes.user import User


class TestUser(TestCase):
    def setUp(self):
        self.user = User("username", "password_hash", "firstname", "lastname")

    def tearDown(self):
        self.user = None

    def test_user_id_is_int(self):
        self.assertIsInstance(self.user.id, int)

    def test_username_is_str(self):
        self.assertIsInstance(self.user.username, str)

    def test_user_firstname_is_str(self):
        self.assertIsInstance(self.user.firstname, str)

    def test_user_lastname_is_str(self):
        self.assertIsInstance(self.user.lastname, str)

    def test_user_password_hash_is_str(self):
        self.assertIsInstance(self.user.password_hash, str)

    def test_user_shopping_list_is_dict(self):
        self.assertIsInstance(self.user.shopping_lists, dict)

    def test_create_shopping_list_without_title(self):
        self.assertTrue(self.user.create_shopping_list(None), "shopping list must have a title")

    def test_create_shopping_list_with_invalid_title(self):
        self.assertTrue(
            self.user.create_shopping_list(["12", "23"]),
            "shopping list title must be a string"
        )

    def test_create_shopping_list(self):
        # attempt to create a shopping list
        shopping_list_title = "back to school"
        self.user.create_shopping_list(shopping_list_title)

        self.assertTrue(
            len(self.user.shopping_lists) == 1,
            msg="Method create_shopping_list should add a ShoppingList object to shopping_lists"
        )

    def test_create_shopping_list_with_duplicate_title(self):
        # Create a shopping list
        shopping_list_title = "back to school"
        self.user.create_shopping_list(shopping_list_title)

        self.assertEqual(
            self.user.create_shopping_list(shopping_list_title),
            "Shopping list `" + shopping_list_title + "` already exists"
        )

    def test_list_shopping_list_returns_list(self):
        self.assertIsInstance(self.user.list_shopping_lists(), list)

    def test_list_shopping_lists(self):
        # Create multiple shopping lists
        self.user.create_shopping_list("Test shopping list")
        self.user.create_shopping_list("Test shopping list 2")
        self.user.create_shopping_list("Test shopping list 3")

        expected_list = ["Test shopping list", "Test shopping list 2", "Test shopping list 3"]

        self.assertTrue(
            set(self.user.list_shopping_lists()) == set(expected_list)
        )

    def test_remove_shopping_list_invalid_argument(self):
        self.assertEqual(
            self.user.remove_shopping_list([]), "Shopping list id should be an Integer"
        )

    def test_remove_shopping_list_that_do_not_exist(self):
        non_existent_id = 10
        self.assertEqual(
            self.user.remove_shopping_list(non_existent_id),
            "Shopping list does not exist"
        )

    def test_remove_shopping_list(self):
        # Create multiple shopping lists
        self.user.create_shopping_list("Test shopping list")
        shopping_list_to_be_removed = self.user.create_shopping_list("Test shopping list 10")

        self.assertTrue(
            self.user.remove_shopping_list(shopping_list_to_be_removed),
            msg="Method remove_shopping_list should return True on successful completion"
        )
