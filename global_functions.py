import random
import hashlib


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


def sha1_hash(value):
    # convert string to bytes
    value = str.encode(value)

    # calculate a SHA1 hash
    hash_object = hashlib.sha1(value)
    hashed_value = hash_object.hexdigest()
    return hashed_value
