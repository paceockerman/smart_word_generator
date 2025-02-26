import random
import lang_def
from feature import *
import jsonpickle
# TODO: make UI faster using keystrokes instead of input()
from pynput import keyboard



features = create_features(lang_def.features)
write_features(features)
features = load_features()




# TODO: wrap everything into a program



def random_feature(choices, features):
    probabilities = [features[choice].current_weight for choice in choices]
    return random.choices(choices, probabilities)[0]


# * -> Word()
def gen_word(features):
    syllable_count = random.randint(1, 4)
    word = Word("", [])
    for _ in range(syllable_count):
        syllable_structure = random_feature(['CV', 'V'], features)
        if syllable_structure == 'CV':
            consonant = random_feature(lang_def.consonants + lang_def.initials, features)
            vowel = random_feature(lang_def.vowels, features)
            word.append(consonant + vowel)
            word.add_features(['CV', consonant, vowel])
        if syllable_structure == 'V':
            vowel = random_feature(lang_def.vowels, features)
            word.append(vowel)
            word.add_features(['V', vowel])
    # TODO: consider making the features a *set* that that structures dont jump it a bunch?
    return word




# Definition of a word: text, list of graphemes
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

def update_weights(word, features):
    res = input(str(word)+': ')
    if res == '2':
        for feature in word.features:
            features[feature].current_weight += features[feature].change_rate
    if res == '1':
        for feature in word.features:
            # Prevent weight from going below 1, so it always has representation
            features[feature].current_weight = max(1, features[feature].current_weight- features[feature].change_rate)


# Loop to learn
while True:
    f_chain = ''
    for feature in features:
        f_chain += str(features[feature]) + " "
    print(f_chain)
    update_weights(gen_word(features), features)