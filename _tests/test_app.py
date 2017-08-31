from unittest import TestCase
import app


class TestApp(TestCase):
    def setUp(self):
        self.app = app
        self.username = "newuser"
        self.pword = "password123"
        self.test_client = app.flask_app.test_client(self)

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

    ''' Tests for flasks endpoints  '''

    def test_index_endpoint_exist(self):
        # test default endpoint '/'
        response = self.test_client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 302, "Endpoint `/` should be accessible")

    def test_signup_endpoint_exist(self):
        # test signup endpoint
        response = self.test_client.get('/signup', content_type='html/text')
        self.assertTrue(response.status_code,
                        "Endpoint `/signup` should be accessible")

    def test_login_endpoint_exist(self):
        # test login endpoint
        response = self.test_client.get('/login', content_type='html/text')
        self.assertTrue(response.status_code,
                        "Endpoint `/login` should be accessible")

    def test_logout_endpoint_exist(self):
        # test login endpoint
        response = self.test_client.get('/signout', content_type='html/text')
        self.assertTrue(response.status_code,
                        "Endpoint `/signout` should be accessible")

    def test_shopping_list_endpoint_exist(self):
        # test shopping-list redirects if user is not logged in
        response = self.test_client.get('/shopping-list',
                                        content_type='html/text')
        self.assertTrue(response.status_code,
                        "Endpoint `/shopping-list` should be redirect if user" +
                        " is not logged in")
