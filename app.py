from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from classes.user import User
from classes.shopping_list import ShoppingList


user_accounts = {}
user_logged_in = None
flask_app = Flask('ShoppingList', template_folder="Designs", static_folder='Designs/assets')


def create_user_account(username=None, password=None, firstname="", lastname=""):

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

    global user_accounts
    new_user_account = User(username, password, firstname, lastname)
    user_accounts[username] = new_user_account


def login(username, password):

    if password is None:
        return 'Password must be provided'

    if username is None:
        return 'Username must be provided'

    global user_accounts
    if username in user_accounts.keys():
        user_account = user_accounts[username]

        if user_account.password_hash == password:
            global user_logged_in
            user_logged_in = user_account.username
            return True

    return 'Wrong credentials combination'


def signout():
    global user_logged_in
    user_logged_in = None


def current_user_has_shopping_lists():
    return len(user_accounts[user_logged_in].shopping_lists) > 0


""" Flask application endpoints """


@flask_app.route('/', methods=['GET'])
def index():
    if user_logged_in is None:
        return redirect('/login')
    else:
        return redirect('/shopping-list')


@flask_app.route('/signup', methods=['POST', 'GET'])
def create_user():
    global user_logged_in
    if user_logged_in is not None:
        return redirect('/shopping-list')

    data = {'host_url': request.host_url}

    if request.method == 'GET':
        return render_template('create_account.html', data=data)

    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        password = request.form['password']
        username = request.form['username']

        error = create_user_account(username, password, firstname, lastname)

        if error is not None:
            data['error'] = "*" + str(error) + "*"
            return render_template('create_account.html', data=data)

        else:
            # log this user in
            login(username, password)
            return redirect('/shopping-list')


@flask_app.route('/login', methods=['POST', 'GET'])
def authenticate_user():
    global user_logged_in
    if user_logged_in is not None:
        return redirect('/shopping-list')

    data = {'host_url': request.host_url}

    if request.method == 'GET':
        return render_template('login.html', data=data)

    if request.method == 'POST':

        password = request.form['password']
        username = request.form['username']

        error = login(username, password)

        if error is not True:
            data['error'] = "*" + str(error) + "*"
            return render_template('login.html', data=data)

        else:
            return redirect('/shopping-list')


@flask_app.route('/logout', methods=['GET'])
def end_session():
    signout()
    return redirect('/login')


@flask_app.route('/create/shoppinglist', methods=['POST'])
def create_shoppinglist():
    shoppinglist = request.form['shoppinglist']
    new_shoppinglist = ShoppingList(shoppinglist)

    # add new shoppinglist to collection of shoppinglists owned by current user
    user_accounts[user_logged_in].shopping_lists.append(new_shoppinglist)

    return redirect('/shopping-list')


@flask_app.route('/shopping-list', methods=['GET'])
def view_shopping_list():

    # assert user is logged in
    global user_logged_in
    if user_logged_in is None:
        return redirect('/login')

    data = dict()
    data['host_url'] = request.host_url
    data['current_users_shopping_lists'] = []

    # check if current user has any shopping_lists
    if current_user_has_shopping_lists():
        # get shopping_lists owned by current user
        current_users_shopping_list_objects = user_accounts[user_logged_in].shopping_lists

        count = 1
        current_users_shopping_lists = []
        for shopping_list in current_users_shopping_list_objects:
            shopping_list_data = dict()
            shopping_list_data["title"] = shopping_list.title
            shopping_list_data["priority"] = count
            shopping_list_data["id"] = shopping_list.id

            current_users_shopping_lists.append(shopping_list_data)
            count += 1

        data['current_users_shopping_lists'] = current_users_shopping_lists

    return render_template('shopping-list.html', data=data)


@flask_app.route('/shopping-list/<shoppinglist_id>', methods=['GET'])
def view_shoppinglist_items(shoppinglist_id):
    data = dict()
    data['host_url'] = request.host_url
    data['current_shoppinglist'] = shoppinglist_id
    data['my_shoppinglists'] = []

    # check if current user has any shoppinglists
    if current_user_has_shopping_lists():
        # get shoppinglists owned by current user
        my_shoppinglists = user_accounts[user_logged_in].shopping_lists
        data['my_shoppinglists'] = my_shoppinglists

    # get items in selected shopping_lists
    for shoppinglist in my_shoppinglists:
        if str(shoppinglist.id) == shoppinglist_id:
            data['my_shoppinglist_items'] = shoppinglist.items
            break

    return render_template('shoppinglist_items.html', data=data)


if __name__ == "__main__":
    flask_app.run(debug=True)
