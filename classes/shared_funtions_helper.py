import random


def get_random_id():
    # generate a random unique integer
    random_id = random.randrange(1, 100000000)
    return random_id


def get_attributes_from_class(instance_of_class):
    members = [attr for attr in dir(instance_of_class) if
               not callable(getattr(instance_of_class, attr)) and not attr.startswith("__")]

    attributes_dict = dict()
    for member in members:
        attributes_dict[member] = getattr(instance_of_class, member)

    return attributes_dict
