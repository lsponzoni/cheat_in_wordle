from file_utils import load_words
from word_keeper import Word_Keeper, contains_letter
from string import ascii_lowercase
#import pyperclip

center_letter = input('Center: ')[0].lower()
allow = set(input("Can contain: ").lower())
allow.add(center_letter)
disallowed = set(filter((lambda k: k not in allow), 'abcdefghijklmnopqrstuvwxyz'))

words = load_words("words_bee.txt")
words = set(filter( lambda k: center_letter in k, words))
wk = Word_Keeper(words)
wk.if_not_contain(disallowed)
print(wk) 

to_delete = []
t = True 
while t:
    print(wk.candidates)
    w = wk.guess()
    print('Added to clipboard\n' + w)
    #pyperclip.copy(w)
    b = input('how was guess? q to quit, w to remove a word that is not there').lower()
    wk.remove_word(w)
    if b == 'w':
       to_delete.append(w)
    t = (b != 'q') and (len(wk.candidates) > 0)

print(to_delete)
o = input("\nonly 5 letters")
print(set(filter((lambda k: len(k) == 5),to_delete)))

