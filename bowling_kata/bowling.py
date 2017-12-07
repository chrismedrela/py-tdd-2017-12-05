# 1. Red: Napisz najprostszy test, który nie przechodzi
# 2. Green: Napisz minimalną ilość kodu zaliczającą ten test
# 3. Refaktor: Zrefaktoryzuj, zarówno testy jak i implementację

FRAMES_IN_GAME = 10
NUMBER_OF_PINS = 10


class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        total = 0
        frame_start_index = 0
        for frame_no in range(FRAMES_IN_GAME):
            first_roll = self.rolls[frame_start_index]
            is_strike = first_roll == NUMBER_OF_PINS
            if is_strike:
                rolls_in_frame = 1
                frame_sum = first_roll
                next_roll = self.rolls[frame_start_index+1]
                next_next_roll = self.rolls[frame_start_index+2]
                bonus = next_roll + next_next_roll
                # frame_sum, bonus, rolls_in_frame = self.score_strike(frame_start_index)
            else:
                second_roll = self.rolls[frame_start_index+1]
                rolls_in_frame = 2
                frame_sum = first_roll + second_roll
                is_spare = frame_sum == NUMBER_OF_PINS
                if is_spare:
                    next_roll = self.rolls[frame_start_index+2]
                    bonus = next_roll
                else:
                    bonus = 0

            total += frame_sum + bonus
            frame_start_index += rolls_in_frame
        return total
