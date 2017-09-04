import classes.shared_funtions_helper
from classes.shopping_list import ShoppingList


class User(object):
    def __init__(self, username, password, firstname, lastname):
        self.username = username
        self.password_hash = password
        self.firstname = firstname
        self.lastname = lastname
        self.shopping_lists = dict()
        self.id = classes.shared_funtions_helper.get_random_id()

    def create_shopping_list(self, title):
        if title is None or len(title) < 1:
            return "shopping list must have a title"

        if not isinstance(title, str):
            return "shopping list title must be a string"

        for shoppinglist in self.shopping_lists.values():
            if title.lower() == shoppinglist.title.lower():
                return "Shopping list " + title + " already exists"

        new_list = ShoppingList(title)

        self.shopping_lists[str(new_list.id)] = new_list

        return str(new_list.id)

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

        for shoppinglist in self.shopping_lists.values():
            list_names.append(shoppinglist.title)

        return list_names
