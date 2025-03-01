class Word:
    def __init__(self, text, features):
        self.text = text
        self.features = features
    def __str__(self):
        return self.text
    def append(self, text):
        self.text += text
    def add_features(self, features):
        self.features.extend(features)