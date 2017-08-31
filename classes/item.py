import classes.shared_funtions_helper


class Item(object):
    def __init__(self, name):
        self.name = name
        self.id = classes.shared_funtions_helper.get_random_id()

    def update(self, name):
        if name is None or len(name) < 1:
            return "Item must have a name"

        if not isinstance(name, str):
            return "Item name must be a string"

        self.name = name
