import random


def get_random_from_list(list):
    random_index = random.randint(0, len(list)-1)

    return list[random_index]