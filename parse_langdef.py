from utils.mongo_interface import setup_mongo
from utils.helpers import rand


def generate_word(langdef, x):
    word = ''
    features = {
        'num_syllables': 0,
        'structures': [],
        'morphemes': []
    }

    num_syllables = rand(langdef['num_syllables'])
    features['num_syllables'] = num_syllables
    for _ in range(int(num_syllables)):
        structure = rand(langdef['structures'])
        features['structures'].append(structure)
        for mtype in structure:
            morpheme = rand(langdef['mappings'][mtype])
            word += morpheme
            features['morphemes'].append(f'{mtype}.{morpheme}')

    return word, features


def update_features(langdef, features, change):
    # TODO we can do smarter learning than just adding 1
    langdef['num_syllables'][features['num_syllables']] += change
    for structure in features['structures']:
        langdef['structures'][structure] += change
    for morpheme in features['morphemes']:
        mtype, morpheme = morpheme.split('.')
        v = langdef['mappings'][mtype][morpheme]
        # Keep above zero so it can still be chosen
        langdef['mappings'][mtype][morpheme] = max(v + change, 1)


def main():
    collection = setup_mongo()
    langdef = collection.find_one()
    for i in range(1):
        word, features = generate_word(langdef, 0)
        print(word)
        update_features(langdef, features, 1)


main()
