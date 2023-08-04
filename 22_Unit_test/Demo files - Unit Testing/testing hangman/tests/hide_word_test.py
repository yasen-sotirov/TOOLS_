from src.hangman import hide_word
import unittest

class HideWord_Should(unittest.TestCase):
    def test_returnsUnchangedWord_allPositionsAreTrue(self):
        self.assertEqual('testword', hide_word('testword', [True] * 8))

    def test_returnsWordWithSomeHiddenLetters_somePositionsAreFalse(self):
        self.assertEqual('w-rd', hide_word('word', [True, False, True, True]))
        self.assertEqual('w-r-', hide_word('word', [True, False, True, False]))
        self.assertEqual('--rd', hide_word('word', [False, False, True, True]))

    def test_returnsCompletelyHiddenWord_allPositionsAreFalse(self):
        self.assertEqual('--------', hide_word('testword', [False] * 8))
