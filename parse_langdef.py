import random
from pymongo import MongoClient
import json

with open('langdef.json', 'r') as f:
    langdef = json.load(f)

client = MongoClient('localhost', 27017)
db = client['main_db']
collection = db['langs']
# lang_id = collection.insert_one(langdef).inserted_id
# print(lang_id)
print(collection.find_one())


def rand(d):
    return random.choices(list(d.keys()), d.values())[0]


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
        langdef['mappings'][mtype][morpheme] += change


l = langdef
for i in range(1):
    word, features = generate_word(l, 0)
    update_features(l, features, 1)
print(l['num_syllables'].values())
