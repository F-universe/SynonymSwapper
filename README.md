SynonymSwapper

A CLI tool that reads an English sentence and outputs a variant where key words are replaced with synonyms, preserving meaning.

Requirements

Python 3.7+

nltk library (for word tokenization and WordNet synsets)

Installation

pip install nltk
python -m nltk.downloader wordnet punkt

Usage

python synonym_swapping.py

Enter a sentence at the prompt; the script will print a paraphrased version with synonyms replaced.

Customization

Adjust MAX_REPLACEMENTS to control how many words are swapped per sentence.

Modify POS_MAPPING in the script to fine-tune which part-of-speech tags are eligible for swapping.
