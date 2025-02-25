vowels = list('iuūeēâōaā')
consonants = list('ptkmnswrl') + ['sh']
initials = ['ps', 'pr', 'pl', 'ts', 'tsh', 'tl', 'ks', 'ksh']
graphemes = vowels + consonants + initials

syllable_structures = ['CV', 'V']


# REQUIRED
features = graphemes + syllable_structures
