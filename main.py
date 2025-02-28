# TODO: make this read a custom file later
from utils import lang_def
from utils.feature import *
from utils.word import Word
# TODO: make UI faster using keystrokes instead of input()


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

def update_weights(word, features, extant_words):
    res = input(str(word)+': ')
    if res == '2':
        for feature in word.features:
            features[feature].current_weight += features[feature].change_rate
        extant_words.append(str(word))
    if res == '1':
        for feature in word.features:
            # Prevent weight from going below 1, so it always has representation
            features[feature].current_weight = max(1, features[feature].current_weight- features[feature].change_rate)
    if res == '3':
        return True
    return False


def main():
    # TODO move this and other stuff to a config somewhere
    good_words_filename = "user_data/good_words.txt"

    # TODO have options on how to get features
    # features = load_features()
    features = create_features(lang_def.features)
    with open(good_words_filename, 'r', encoding='utf-8') as f:
        extant_words = [line.strip() for line in f]
    print(extant_words)
    is_done = False
    while not is_done:
        is_done = update_weights(gen_word(features, extant_words), features, extant_words)

    # Save features and found words
    with open(good_words_filename, 'w', encoding='utf-8') as f:
        f.writelines(word + '\n' for word in extant_words)
    write_features(features)

main()