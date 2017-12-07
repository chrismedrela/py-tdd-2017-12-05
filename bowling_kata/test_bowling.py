import unittest

from bowling import BowlingGame

class BowlingGameTests(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()
    
    def roll_many_times(self, pins, rolls):
        for _ in range(rolls):
            self.game.roll(pins)

    def roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)

    def roll_strike(self):
        self.game.roll(10)

    def test_can_create_BowlingGame(self):
        pass

    def test_when_all_throws_in_gutter_then_score_should_be_zero(self):
        self.roll_many_times(pins=0, rolls=20)
        self.assertEqual(self.game.score(), 0)

    def test_when_no_bonus_points_then_score_should_be_sum_of_rolls(self):
        self.roll_many_times(pins=1, rolls=20)
        self.assertEqual(self.game.score(), 20)

    def test_when_spare_then_bonus_for_next_roll(self):
        self.roll_spare()
        self.roll_many_times(pins=1, rolls=18)
        self.assertEqual(self.game.score(), 11 + 18)

    def test_when_strike_then_bonus_for_two_next_rolls(self):
        self.roll_strike()
        self.roll_many_times(pins=1, rolls=18)
        self.assertEqual(self.game.score(), 12 + 18)

    def test_when_perfect_game_then_score_should_be_300(self):
        self.roll_many_times(pins=10, rolls=12)
        self.assertEqual(self.game.score(), 300)