def has_n_letters(n):
    return (lambda w: len(w) == n)

def load_words(n):
    with open('words_alpha.txt') as word_file:
        all_words = word_file.read().split()
        five_letters = filter(has_n_letters(n), all_words)
    return five_letters

def save_words(to, words):
    with open(to, "wt") as word_file:
        for i in words:
            word_file.write(i + '\n')


from sys import argv
if len(argv) < 3:
    n = int(input("Number of Letters"))
    to = input("Select file to save to") 
else:
    n = int(argv[1])
    to = argv[2]

to_wordle = load_words(n)        
save_words(to, to_wordle)

