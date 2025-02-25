import random
import lang_def
import prefs
from pynput import keyboard

# Pushing to git



# Setup language
grapheme_weights = dict([(grapheme, prefs.start_weight) for grapheme in lang_def.graphemes])


# helper
def grapheme_choice(graphemes, grapheme_weights):
    probabilities = []
    for grapheme in graphemes:
        probabilities.append(grapheme_weights[grapheme])
    return random.choices(graphemes, probabilities)[0]

# * -> Word()
def gen_word(weights):
    syllable_count = random.randint(1, 4)
    word = ''
    grapheme_list = []
    for _ in range(syllable_count):
        consonant = grapheme_choice(lang_def.consonants + lang_def.initials, weights)
        vowel = grapheme_choice(lang_def.vowels, weights)
        word += consonant + vowel
        grapheme_list.extend([consonant, vowel])
    return Word(word, grapheme_list)




# Definition of a word: text, list of graphemes
class Word:
    def __init__(self, text, grapheme_list):
        self.text = text
        self.grapheme_list = grapheme_list
    def __str__(self):
        return self.text

def update_weights(word):
    res = input(str(word)+': ')
    if res == '2':
        for grapheme in word.grapheme_list:
            grapheme_weights[grapheme] += prefs.change_rate
    if res == '1':
        for grapheme in word.grapheme_list:
            # Prevent weight from going below 1, so it always has representation
            grapheme_weights[grapheme] = max(1, grapheme_weights[grapheme]-prefs.change_rate)



# Loop to learn
while True:
    print(grapheme_weights)
    update_weights(gen_word(grapheme_weights))