import unittest

from bowling import BowlingGame

class BowlingGameTests(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()
    
    def roll_twenty_times(self, pins):
        for _ in range(20):
            self.game.roll(pins)

    def test_can_create_BowlingGame(self):
        pass

    def test_when_all_throws_in_gutter_then_score_should_be_zero(self):
        self.roll_twenty_times(0)
        self.assertEqual(self.game.score(), 0)

    def test_when_no_bonus_points_then_score_should_be_sum_of_rolls(self):
        self.roll_twenty_times(1)
        self.assertEqual(self.game.score(), 20)

    def test_when_spare_then_bonus_for_next_roll(self):
        self.game.roll(5)
        self.game.roll(5)
        for _ in range(18):
            self.game.roll(1)
        self.assertEqual(self.game.score(), 11 + 18)
