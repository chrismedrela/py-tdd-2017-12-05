# 1. Red: Napisz najprostszy test, który nie przechodzi
# 2. Green: Napisz minimalną ilość kodu zaliczającą ten test
# 3. Refaktor: Zrefaktoryzuj, zarówno testy jak i implementację

class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        total = 0
        frame_start_index = 0
        for frame_no in range(10):
            first_roll = self.rolls[frame_start_index]
            second_roll = self.rolls[frame_start_index+1]
            if first_roll + second_roll == 10:
                next_roll = self.rolls[frame_start_index+2]
                total += next_roll
            total += first_roll + second_roll
            frame_start_index += 2
        return total
