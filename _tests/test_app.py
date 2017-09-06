from unittest import TestCase
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

        # def test_login(self):
        #     self.app.create_user_account(self.username, self.pword)
        #     self.assertTrue(self.app.login(self.username, self.pword))
        #
        # def test_login_set_session(self):
        #     self.app.create_user_account(self.username, self.pword)
        #     self.app.login(self.username, self.pword)
        #     self.assertTrue(self.app.user_logged_in is not None)
        #
        # def test_signout(self):
        #     self.app.create_user_account(self.username, self.pword)
        #     self.app.login(self.username, self.pword)
        #     self.app.signout()
        #     with self.app.app_context():
        #         self.assertTrue("user_logged_in" not in self.app.session.keys())
        #
        # def test_index_endpoint_exist(self):
        #     # test default endpoint '/'
        #     response = self.test_client_app.get('/', content_type='html/text')
        #     self.assertEqual(response.status_code, 302)
        #
        # def test_login_endpoint_exist(self):
        #     response = self.test_client_app.get('/login', content_type='html/text')
        #     self.assertEqual(response.status_code, 302)
        #
        # def test_logout_endpoint_exist(self):
        #     response = self.test_client_app.get('/logout', content_type='html/text')
        #     self.assertEqual(response.status_code, 302)
        #
        # def test_shopping_list_endpoint_exist(self):
        #     response = self.test_client_app.get('/shopping-list', content_type='html/text')
        #     self.assertEqual(response.status_code, 302)
