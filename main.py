# TODO: make this read a custom file later
import lang_def
from feature import *
from word import Word
import jsonpickle
# TODO: make UI faster using keystrokes instead of input()
from pynput import keyboard


# features = create_features(lang_def.features)
# write_features(features)
# features = load_features()


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

def update_weights(word, features):
    res = input(str(word)+': ')
    if res == '2':
        for feature in word.features:
            features[feature].current_weight += features[feature].change_rate
    if res == '1':
        for feature in word.features:
            # Prevent weight from going below 1, so it always has representation
            features[feature].current_weight = max(1, features[feature].current_weight- features[feature].change_rate)
    if res == '3':
        return True
    return False


def main():
    # TODO have options on how to get features

    features = load_features()
    is_done = False
    while not is_done:
        is_done = update_weights(gen_word(features), features)

    write_features(features)
    pass

main()