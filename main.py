import random

from sympy.stats.rv import probability

import lang_def
import prefs
from pynput import keyboard

# Setup language
# TODO: Have these import/export to/from a json file
feature_weights = dict([(feature, prefs.start_weight) for feature in lang_def.features])

# Setup user
class UserPrefs:
    def __init__(self, feature_weights):
        self.feature_weights = feature_weights
    def update(self, feature_weights):
        self.feature_weights = feature_weights
    def get_grapheme_weight(self, grapheme):
        return self.feature_weights[grapheme]
    def get_syllable_structure_weight(self, syllable_structure):
        return self.feature_weights[syllable_structure]
    def weighted_grapheme_choice(self, graphemes):
        probabilities = [self.feature_weights[grapheme] for grapheme in graphemes]
        return random.choices(graphemes, probabilities)[0]
    def weighted_syllable_structure_choice(self, syllable_structures):
        probabilities = [self.feature_weights[syllable_structure] for syllable_structure in syllable_structures]
        return random.choices(syllable_structures, probabilities)[0]

user = UserPrefs(feature_weights)




# * -> Word()
def gen_word(feature_weights):
    syllable_count = random.randint(1, 4)
    word = Word("", [])
    for _ in range(syllable_count):
        syllable_structure = user.weighted_syllable_structure_choice(['CV', 'V'])
        if syllable_structure == 'CV':
            consonant = user.weighted_grapheme_choice(lang_def.consonants + lang_def.initials)
            vowel = user.weighted_grapheme_choice(lang_def.vowels)
            word.append(consonant + vowel)
            word.add_features(['CV', consonant, vowel])
        if syllable_structure == 'V':
            vowel = user.weighted_grapheme_choice(lang_def.vowels)
            word.append(vowel)
            word.add_features(['V', vowel])
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

def update_weights(word):
    print(word.features)
    res = input(str(word)+': ')
    if res == '2':
        for feature in word.features:
            feature_weights[feature] += prefs.change_rate
    if res == '1':
        for feature in word.features:
            # Prevent weight from going below 1, so it always has representation
            feature_weights[feature] = max(1, feature_weights[feature]-prefs.change_rate)



# Loop to learn
while True:
    print(feature_weights)
    update_weights(gen_word(feature_weights))