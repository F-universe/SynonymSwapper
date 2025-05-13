#!/usr/bin/env python3
"""
synonym_swapping.py: replace words in a sentence with synonyms using NLTK WordNet.
"""
import random
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Number of words to replace per sentence\ nMAX_REPLACEMENTS = 3
# Map NLTK POS tags to WordNet POS categories\ nPOS_MAPPING = {
    'NN': wordnet.NOUN,
    'NNS': wordnet.NOUN,
    'VB': wordnet.VERB,
    'VBD': wordnet.VERB,
    'VBG': wordnet.VERB,
    'VBN': wordnet.VERB,
    'VBP': wordnet.VERB,
    'VBZ': wordnet.VERB,
    'JJ': wordnet.ADJ,
    'JJR': wordnet.ADJ,
    'JJS': wordnet.ADJ,
    'RB': wordnet.ADV,
    'RBR': wordnet.ADV,
    'RBS': wordnet.ADV
}

def get_synonyms(word, pos):
    synsets = wordnet.synsets(word, pos=pos)
    lemmas = set(chain.from_iterable([syn.lemma_names() for syn in synsets]))
    lemmas.discard(word)
    return list(lemmas)


def synonym_swap(sentence, max_replacements=MAX_REPLACEMENTS):
    tokens = word_tokenize(sentence)
    tagged = pos_tag(tokens)
    indices = [i for i, (_, tag) in enumerate(tagged) if tag in POS_MAPPING]
    random.shuffle(indices)
    replaced = 0
    for idx in indices:
        word, tag = tagged[idx]
        wn_pos = POS_MAPPING[tag]
        syns = get_synonyms(word, wn_pos)
        if syns:
            replacement = random.choice(syns).replace('_', ' ')
            tokens[idx] = replacement
            replaced += 1
            if replaced >= max_replacements:
                break
    return ' '.join(tokens)


def main():
    sentence = input("Enter an English sentence: ")
    paraphrased = synonym_swap(sentence)
    print("Paraphrased sentence:", paraphrased)


if __name__ == '__main__':
    main()
