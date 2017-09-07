from unittest import TestCase
import global_functions
import app
from app import flask_app


class TestApp(TestCase):
    def setUp(self):
        self.app = app
        self.username = "newuser"
        self.pword = "password123"
        self.test_client_app = flask_app.test_client()
        self.test_client_app.testing = True

    def tearDown(self):
        self.app = None
        self.username = None
        self.pword = None
        self.test_client_app = None

    def test_user_accounts_is_dict(self):
        self.assertIsInstance(self.app.user_accounts, dict)

    def test_create_user_account_without_username(self):
        self.assertEqual(
            self.app.create_user_account("", "pword"),
            "User must provide a username"
        )

    def test_create_user_account_with_invalid_username(self):
        self.assertEqual(
            self.app.create_user_account([], "pword"),
            "Username must be string"
        )

    def test_create_user_account_with_invalid_username_characters(self):
        self.assertEqual(
            self.app.create_user_account("@#^&&", "pword"),
            "Username should only contain letters and numbers"
        )

    def test_create_user_account_without_password(self):
        self.assertEqual(
            self.app.create_user_account("username", ""),
            "User must provide a pword"
        )

    def test_create_user_account_with_invalid_password(self):
        self.assertEqual(
            self.app.create_user_account("username", 12546),
            "Password provided must be a string"
        )

    def test_create_user_account_with_short_password(self):
        self.assertEqual(
            self.app.create_user_account("username", "123"),
            "Password should have at-least 6 characters"
        )

    def test_create_user_account(self):
        self.app.create_user_account("username", "1234567")
        self.assertTrue(len(self.app.user_accounts) == 1)

    def test_create_user_account_password_is_hashed(self):
        self.app.create_user_account(self.username, self.pword)
        stored_password = self.app.user_accounts[self.username].password_hash

        self.assertEqual(
            stored_password,
            global_functions.sha1_hash(self.pword),
            msg="Stored passwords should be Hashed"
        )

    def test_create_user_with_duplicate_username(self):
        self.app.create_user_account("username", "1234567")
        self.assertEqual(
            self.app.create_user_account("username", "1234567"),
            "Username username is already taken. Use a unique username"
        )

    def test_login_without_password(self):
        self.assertEqual(
            self.app.login("username", None),
            "Password must be provided"
        )

    def test_login_with_invalid_password(self):
        self.assertEqual(
            self.app.login("username", "asdasdsds"),
            "Wrong credentials combination"
        )

    def test_login_without_username(self):
        self.assertEqual(
            self.app.login(None, "asdasdsds"),
            "Username must be provided"
        )

    def test_login_with_invalid_username(self):
        self.assertEqual(
            self.app.login("non-existent-username", "asdasdsds"),
            "Wrong credentials combination"
        )
