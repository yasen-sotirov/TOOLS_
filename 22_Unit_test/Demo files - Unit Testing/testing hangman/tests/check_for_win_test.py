from src.hangman import check_for_win
import unittest

class CheckForWin_Should(unittest.TestCase):
    def test_returnFalse_listContainsAtLeastOneFalseValue(self):
        self.assertEqual(False, check_for_win([True, False, True]))

    def test_returnTrue_listContainsOnlyTrueValues(self):
        self.assertEqual(True, check_for_win([True, True, True]))