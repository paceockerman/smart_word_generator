import random


def rand(d: dict[str, int]):
    return random.choices(list(d.keys()), list(d.values()))[0]
