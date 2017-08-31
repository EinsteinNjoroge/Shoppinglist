import time


def get_random_id():
    # generate a random unique integer
    epoch_time = time.time()
    random_id = round(float(str(epoch_time)[8:]) * 10000000)
    return random_id
