from unittest import TestCase
import app


class TestApp(TestCase):
    def setUp(self):
        self.app = app
        self.username = "newuser"
        self.pword = "password123"

    def tearDown(self):
        self.app = None

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

    def test_login(self):
        self.app.create_user_account(self.username, self.pword)
        self.assertTrue(self.app.login(self.username, self.pword))

    def test_login_set_session(self):
        self.app.create_user_account(self.username, self.pword)
        self.app.login(self.username, self.pword)

        self.assertTrue(self.app.user_logged_in is not None)

    def test_signout(self):
        self.app.create_user_account(self.username, self.pword)
        self.app.login(self.username, self.pword)
        self.app.signout()
        self.assertTrue(self.app.user_logged_in is None)
