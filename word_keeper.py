from collections import defaultdict

def def_val():
    return 0

def contains_letter(word, letters):
    for l in letters: #complexity here  o(|w| * |l|)
        if l in word:
            return True
    return False

def contains_at_position(word, letter, position):
    return word[position] == letter

def _0_the_score_of(score, word):
    for letter in word:
        score[letter] = 0
    return score

def calculate_letter_score(wordlist):
    letter_score = defaultdict(def_val)
    for word in wordlist:
        unique_letters = set()
        for letter in word:
            if letter not in unique_letters:
                unique_letters.add(letter)
                letter_score[letter] = 1 + letter_score.get(letter, 0)
    return letter_score

def max_word_score(word_list, letter_score):
    max_score, max_word = 0, ""
    for word in word_list:
        word_score = 0
        unique_letters = set()
        for l in word:
            if l not in unique_letters:
                unique_letters.add(l)
                word_score += letter_score[l]
        if word_score > max_score:
            max_score, max_word = word_score, word

    return max_word


class Word_Keeper:
    def __init__(self, words):
        self.word_bank = words
        self.candidates = words
        self.previous_state = words
        self.right = set() 
        self.update = False

    def __record(self):
        self.update = True
        self.previous_state = (self.word_bank, self.candidates, self.right.copy())

    def __filter(self, f):
        self.__record()
        self.candidates = set(filter(f, self.candidates))

    def remove_word(self, word):
        self.__record()
        self.candidates.discard(word)
        self.word_bank.discard(word) 

    def right_add(self, letters):
        for l in letters:
            self.right.add(l)

    def if_not_contain(self, letters):
        self.__filter(lambda w: not contains_letter(w, letters))
        
    def if_not_in_position(self, letters, pos):
        self.__filter(lambda w: not contains_at_position(w, letters, pos) and
                contains_letter(w, letters))
        self.right_add(letters)

    def if_in_position(self, letters, pos):
        self.__filter(lambda w: contains_at_position(w, letters, pos))
        self.right_add(letters)

    def undo(self):
        tmp_copy = (self.word_bank, self.candidates, self.right)
        self.word_bank, self.candidates, self.right = self.previous_state
        self.previous_state = tmp_copy
        self.update = True

    def current_size(self):
        return len(self.candidates)

    def __str__(self):
        return str(self.candidates) +'\n'+ str(self.current_size())

    def guess(self):
        self.update = False
        from random import choice
        g = choice(list(self.candidates))
        return g
    
    def best_guess(self):
        self.update = False
        letter_score = calculate_letter_score(self.candidates)
        mw = max_word_score(self.candidates, letter_score)
        
        #remove from letter_score if has right letters
        unique_score = _0_the_score_of(letter_score, self.right) 
        cw = max_word_score(self.word_bank, unique_score)
        return mw, cw
    
    

