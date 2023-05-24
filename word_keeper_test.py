import unittest
from word_keeper import Word_Keeper, _0_the_score_of

class UnitTestNames(unittest.TestCase):
    def test_creation(self):
        SMALL_DICTIONARY = ["ABCDE","ABCDI","BCDEI", "EFGHI"] 
        wk = Word_Keeper(SMALL_DICTIONARY) # All
        self.assertEqual(list(wk.candidates),SMALL_DICTIONARY)

    def test_filter(self):
        SMALL_DICTIONARY = ["ABCDE","ABCDI","BCDEI", "EFGHI"] 
        wk = Word_Keeper(SMALL_DICTIONARY) # All
        wk.if_in_position("A", 0) 
        self.assertEqual(set(wk.candidates),set(['ABCDE', "ABCDI"]))

    def test_improved_guess(self):
        SMALL_DICTIONARY = ["ABCDE","ABCDI","BCDEI", "EFGHI"] 
        wk = Word_Keeper(SMALL_DICTIONARY) # All
        wk.if_in_position("A", 0) 
        _dc, bcdei = wk.best_guess() 
        self.assertEqual(bcdei, "BCDEI")

    def test_right_add(self):
        SMALL_DICTIONARY = ["ABCDE","ABCDI","BCDEI", "EFGHI"] 
        wk = Word_Keeper(SMALL_DICTIONARY) # All
        wk.right_add("aebcde")
        self.assertEqual(wk.right, set(['a','b','c','d','e']))
    
    def test_0_score(self):
        score = {'a':10, 'b': 1}
        word = set('asim')
        sc = _0_the_score_of(score, word)
        self.assertEqual(sc['a'], 0)

    def test_0_score_of_undef(self):
        score = {'a' :10, 'b': 1}
        word = set('s')
        sc = _0_the_score_of(score, word)
        self.assertEqual(sc['a'], 10)
        self.assertEqual(sc['b'], 1)
        self.assertEqual(sc['s'], 0)
   
    def test_undo_working(self):
        SMALL_DICTIONARY = ["a",'b']
        wk = Word_Keeper(SMALL_DICTIONARY)
        wk.if_in_position("A", 0)
        import copy
        right_before = copy.deepcopy(wk.right)
        wk.if_in_position("B", 1)
        wk.undo()
        self.assertEqual(right_before, wk.right)

    def test_it_correctly_changes_right(self):
        SMALL_DICTIONARY = ["a",'b']
        wk = Word_Keeper(SMALL_DICTIONARY)
        wk.if_in_position("A", 0)
        wk.if_in_position("B", 1)
        self.assertEqual(set(["A","B"]), wk.right)


if __name__ == '__main__':
    unittest.main()

