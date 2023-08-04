import unittest
from src.functions import calculate_winnings


class CalculateWinnings_Should(unittest.TestCase):
    def test_return_correct_winnings_one_odd(self):
        winnings = calculate_winnings(10, [1.5])
        self.assertEqual(5.0, winnings)

    def test_return_correct_winnings_multiple_odds(self):
        winnings = calculate_winnings(10, [1.5, 1.5])
        self.assertEqual(12.5, winnings)

    def test_return_no_winnings_when_no_winning_odds(self):
        winnings = calculate_winnings(10, [])
        self.assertEqual(0, winnings)

    def test_return_no_winnings_when_invalid_stake(self):
        self.assertEqual(0, calculate_winnings(0, [1.5, 1.5]))
        self.assertEqual(0, calculate_winnings(-5, [1.5, 1.5]))
