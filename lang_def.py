vowels = list('iuūeēâōaā')
consonants = list('ptkmnswrl') + ['sh']
initials = ['ps', 'pr', 'pl', 'ts', 'tsh', 'tl', 'ks', 'ksh']
graphemes = vowels + consonants + initials

syllable_structures = ['CV', 'V']


# REQUIRED
features = ([(grapheme, "grapheme") for grapheme in graphemes]
            + [(syllable_structure, "syllable_structure") for syllable_structure in syllable_structures])
