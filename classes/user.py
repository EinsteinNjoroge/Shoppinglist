import global_functions
from classes.shopping_list import ShoppingList


class User(object):

    def __init__(self, username, password, firstname, lastname):

        """
            Attributes:
                username (str): A unique name to identify user.
                password (str): A secret phrase to authenticate a user.
                firstname (str): The user's first name.
                lastname (str): The user's last name.

            Methods:
                create_shopping_list
                remove_shopping_list
                list_shopping_lists

            Args:
                username (str): A unique name to identify user.
                password (str): A secret phrase to authenticate a user.
                firstname (str): The user's first name.
                lastname (str): The user's last name.

            """

        self.username = username
        self.password_hash = password
        self.firstname = firstname
        self.lastname = lastname
        self.shopping_lists = dict()
        self.id = global_functions.get_random_id()

    def create_shopping_list(self, title):
        """ Creates a new ShoppingList object

            Args:
                title: The caption of the  shoppinglist

            Returns:
                str: id of the new shoppinglist that has been created

        """
        if title is None or len(title) < 1:
            return "shopping list must have a title"

        if not isinstance(title, str):
            return "shopping list title must be a string"

        for shoppinglist in self.shopping_lists.values():
            if title.lower() == shoppinglist.title.lower():
                return "Shopping list " + title + " already exists"

        new_list = ShoppingList(title)

        # add the new shopping list object to the list of shoppinglists owned by current user
        self.shopping_lists[str(new_list.id)] = new_list

        return str(new_list.id)

    def remove_shopping_list(self, shopping_list_id):
        """ Deletes the selected shoppinglist object from memory

            Args:
                shopping_list_id (str): The caption of the  shoppinglist

            Returns:
                True if the shoppinglist has been deleted successfully, otherwise return
                error message

        """

        if not isinstance(shopping_list_id, int):
            return "Shopping list id should be an Integer"

        for shopping_list in self.shopping_lists:
            if str(shopping_list.id) == str(shopping_list_id):
                del shopping_list
                return True

        return "Shopping list does not exist"

    def list_shopping_lists(self):
        """
            Returns:
                list: Returns a list of all the shoppinglists owned by current user

        """
        list_names = []
        for shoppinglist in self.shopping_lists.values():
            list_names.append(shoppinglist.title)

        return list_names
