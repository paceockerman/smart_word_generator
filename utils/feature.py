import jsonpickle
import random

class Feature:
    def __init__(self, value, ftype, start_weight=10, change_rate=1, current_weight=10):
        self.value = value
        self.ftype = ftype
        self.start_weight = start_weight
        self.change_rate = change_rate
        self.current_weight = current_weight
    def __str__(self):
        return f'({self.value}-{self.current_weight})'


def load_features(langdeffeatures, file="data.json", empty=False):
    # TODO this should create features for all graphemes & structures by default
    if empty:
        return dict([(value, Feature(value, ftype)) for (value, ftype) in langdeffeatures])
    with open(file, "r") as f:
        return jsonpickle.decode(f.read())

def write_features(features, file="data.json"):
    with open(file, "w") as f:
        f.write(jsonpickle.encode(features, indent=2))

def random_feature(choices, features):
    probabilities = [features[choice].current_weight for choice in choices]
    return random.choices(choices, probabilities)[0]