# TODO: make this read a custom file later
import lang_def
from feature import *
from word import Word
# TODO: make UI faster using keystrokes instead of input()
from pynput import keyboard


# * -> Word()
def gen_word(features, extant_words):
    # TODO: have features be derived from the words given to the program
    #   every time a new feature is gotten from a word, add it to the feature list
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

    # Generate a new one if this one has already been made
    if word.text in extant_words:
        return gen_word(features, extant_words)
    # Consider making the features a *set* that that structures don't jump it a bunch?
    #   ie there are 3 'CV' tags in a CVCVCV word, which may or may not be a good feature
    return word

def update_weights(word, features, word_file):
    res = input(str(word)+': ')
    if res == '2':
        for feature in word.features:
            features[feature].current_weight += features[feature].change_rate
        word_file.write(str(word) + "\n")
    if res == '1':
        for feature in word.features:
            # Prevent weight from going below 1, so it always has representation
            features[feature].current_weight = max(1, features[feature].current_weight- features[feature].change_rate)
    if res == '3':
        return True
    return False


def main():
    # TODO have options on how to get features
    # features = load_features()
    features = create_features(lang_def.features)
    # TODO: make this file name customizable
    word_file = open('good_words.txt', 'a', encoding='utf-8')
    extant_words = []
    with open('good_words.txt', 'r', encoding='utf-8') as f:
        for line in f:
            extant_words.append(line.strip())
    print(extant_words)
    is_done = False
    while not is_done:
        is_done = update_weights(gen_word(features, extant_words), features, word_file)

    write_features(features)

main()