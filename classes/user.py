import classes.shared_funtions_helper
from classes.shopping_list import ShoppingList


class User(object):
    def __init__(self, username, password, firstname, lastname):
        self.username = username
        self.password_hash = password
        self.firstname = firstname
        self.lastname = lastname
        self.shopping_lists = []
        self.id = classes.shared_funtions_helper.get_random_id()

    def create_shopping_list(self, title):
        if title is None or len(title) < 1:
            return "shopping list must have a title"

        if not isinstance(title, str):
            return "shopping list title must be a string"

        for shopping_list in self.shopping_lists:
            if shopping_list.title == title:
                return "Shopping list " + title + " already exists"

        new_list = ShoppingList(title)
        self.shopping_lists.append(new_list)

        return new_list.id

    def remove_shopping_list(self, shopping_list_id):
        if not isinstance(shopping_list_id, int):
            return "Shopping list id should be an Integer"

        for shopping_list in self.shopping_lists:
            if shopping_list.id == shopping_list_id:
                del shopping_list
                return True

        return "Shopping list does not exist"

    def list_shopping_lists(self):
        list_names = []
        for shopping_list in self.shopping_lists:
            list_names.append(shopping_list.title)

        return list_names
