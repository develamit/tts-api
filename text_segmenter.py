# -*- coding: utf-8 -*-
from nltk import word_tokenize
from re import match


def get_segments(text):
    segments = []
    tokens = word_tokenize(text)
    segment = ''
    added = False
    for token in tokens:
        if len(segment + token) < 99:
            if match(r"[^\w\s]", token) is None and token != "n't":
                segment += ' '
            segment += token
            added = False
        else:
            added = True
            segments.append(segment)
            segment = ''
    if not added:
        segments.append(segment)

    return segments


if __name__ == '__main__':
    text = '''John Winston Ono Lennon, MBE was an English musician and \
singer-songwriter who rose to worldwide fame as one of the founder \
members of The Beatles, one of the most commercially successful and \
critically acclaimed acts in the history of popular music.
    '''
    for i in get_segments(text):
        print i