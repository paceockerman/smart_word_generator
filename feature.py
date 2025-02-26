import jsonpickle

class Feature:
    def __init__(self, value, ftype, start_weight=10, change_rate=1, current_weight=10):
        self.value = value
        self.ftype = ftype
        self.start_weight = start_weight
        self.change_rate = change_rate
        self.current_weight = current_weight
    def __str__(self):
        return f'({self.value}-{self.current_weight})'


def load_features(file="data.json"):
    with open(file, "r") as f:
        return jsonpickle.decode(f.read())

# TODO: make this not like this (langdeffeatures)
def create_features(langdeffeatures):
    # Save features as a dict of value, Feature
    # TODO: make a better way to define features
    return dict([(value, Feature(value, ftype)) for (value, ftype) in langdeffeatures])

def write_features(features, file="data.json"):
    with open(file, "w") as f:
        f.write(jsonpickle.encode(features, indent=2))
