import random


def rand(d):
    return random.choices(list(d.keys()), d.values())[0]
