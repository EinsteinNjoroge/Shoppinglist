import random
import hashlib


def get_random_id():
    """generates a random integer value between 1 and 100000000
    :return
        (int): randomly generated integer
    """
    # generate a random unique integer
    random_id = random.randrange(1, 100000000)
    return random_id


def get_attributes_from_class(instance_of_class):
    """Get attributes from a class objects and returns a dictionary containing
    the attribute name as (key) and the attribute value as (value)

        :arg
            instance_of_class: An object

        :return
            (dict): Attribute name as (key) and the attribute value as (value)

    """
    # get a list of member attributes of class
    members = [attr for attr in
               dir(instance_of_class) if not
               callable(getattr(instance_of_class, attr)) and not
               attr.startswith("__")
               ]

    # loop through members array
    # add the member values to the attributes dictionary
    attributes_dict = dict()
    for member in members:
        attributes_dict[member] = getattr(instance_of_class, member)

    return attributes_dict


def sha1_hash(value):
    """Calculates the SHA1 has of a string

            :arg:
                value (str): String to be hashed

            :return
                (str): SHA1 hash
        """
    # convert string to bytes
    value = str.encode(value)

    # calculate a SHA1 hash
    hash_object = hashlib.sha1(value)
    hashed_value = hash_object.hexdigest()
    return hashed_value
