def load_words(f):
    with open(f) as word_file:
        words = set(word_file.read().split())
    return words

def unload_words(words):
    with open(WORDLE_FILENAME+".update.txt", 'w') as word_file:
        word_file.write(' '.join(list(words)))


