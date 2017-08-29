import time


class Item(object):
    def __init__(self, name):
        self.name = name
        # generate a random id for this item
        epoch_time = time.time()
        self.id = round(float(str(epoch_time)[8:]) * 10000000)

    def update(self, name):
        if name is None or len(name) < 1:
            return "Item must have a name"

        if not isinstance(name, str):
            return "Item name must be a string"

        self.name = name
