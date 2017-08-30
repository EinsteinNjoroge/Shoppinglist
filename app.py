from classes.user import User
import time


user_accounts = {}
user_logged_in = None


def create_user_account(username=None, password=None, firstname="", lastname=""):
    global user_accounts

    if not isinstance(password, str):
        return 'Password provided must be a string'

    if not isinstance(username, str):
        return 'Username must be string'

    if len(password) < 1:
        return 'User must provide a pword'

    if len(username) < 1:
        return 'User must provide a username'

    if not username.isalnum():
        return 'Username should only contain letters and numbers'

    if len(password) < 6:
        return 'Password should have at-least 6 characters'

    new_user_account = User(username, password, firstname, lastname)
    user_accounts[username] = new_user_account


def login(username, password):
    global user_logged_in
    global user_accounts

    if password is None:
        return 'Password must be provided'

    if username is None:
        return 'Username must be provided'

    if username in user_accounts.keys():
        user_account = user_accounts[username]

        if user_account.password_hash == password:
            user_logged_in = user_account.id
            return True

    return 'Wrong credentials combination'


def signout():
    global user_logged_in
    user_logged_in = None


def get_random_id():
    # generate a random id for this item
    epoch_time = time.time()
    random_id = round(float(str(epoch_time)[8:]) * 10000000)
    return random_id
