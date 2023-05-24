WORDLE_FILENAME = "wordle_words5.txt"
WORDLE_SIZE = 5

from file_utils import load_words, unload_words 
from word_keeper import Word_Keeper

#UI
from menu import stdMenu, run, menu_message, read_prompt, prompt_for

MASK = "Fill with the letter max, use underline where not relevant as\n"+\
        "radio\n"+\
        "_a_i_\n"

COMPLETE_MASK = "Complete the mask like jxoxx, where o is the right letter, x is letter not in solution, j is in solution but out of place\n_____\n"
LETTER = "Letters :"
WORD = "Word: "

def not_blank(e):
    i, letter = e
    return letter != '_'

def prompt_mask():
    mask = prompt_for(MASK, WORDLE_SIZE)
    return filter(not_blank, enumerate(mask))

#Menu Functions
def right(keep):
    for pos, letter in prompt_mask():
        keep.if_in_position(letter, pos)
    return keep, True

def out_of_place(keep):
    for pos, letter in prompt_mask():
        keep.if_not_in_position(letter, pos)
    return keep, True

def wrong(keep):
    letter = read_prompt(LETTER)
    keep.if_not_contain(letter)
    return keep, True

def undo(keep):
    keep.undo()
    return keep, True

def delete(keep):
    w = prompt_for(WORD, WORDLE_SIZE)
    keep.remove_word(w)
    return keep, True

def guess(keep):
    print(f"Random: {keep.guess()}")
    right, nright = keep.best_guess()
    print(f"Best Guess: {right} Can't win:{nright}")
    return keep, True

def two_times(keep):
    w = prompt_for(WORD, WORDLE_SIZE)
    fix = prompt_for(COMPLETE_MASK, WORDLE_SIZE)
    wrong = []
    for pos, letter in enumerate(fix): 
        if letter == 'o':
            keep.if_in_position(w[pos], pos)
        elif letter == 'x':
            wrong += w[pos] 
        elif letter == 'j':
            keep.if_not_in_position(w[pos], pos)
    if len(wrong) > 0:
        keep.if_not_contain(wrong) 
    return keep, True

menu = stdMenu()
menu['r'] = (right, "right place letters")
menu['o'] = (out_of_place, "ut of place letters")
menu['w'] = (wrong, "wrong letters, not even in the word letters")
menu['u'] = (undo, "undo last change")
menu['g'] = (guess, "guess a word")
menu['d'] = (delete, "delete a word")
menu['k'] = (two_times, "input the last guess and x for wrong, o for right, j for out of place")

MENU_MSG = menu_message(menu)

keep = Word_Keeper(load_words(WORDLE_FILENAME))
loop = True
while(loop):
    choice = prompt_for(MENU_MSG, 1)
    keep, loop = run(menu, keep, choice)
    if loop and keep.update:
        print(keep)

print("Congrats\n")




