import random
from constants import WORDS, MASK_SYMBOL


class WordControllers:
    def get_random_word(self):
        return random.choice(WORDS)

    def mask_word_without_symbols(self, word, symbols):
        return ''.join([s if s in symbols else MASK_SYMBOL for s in word])
