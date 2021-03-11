import unittest

import BowlingGame

class BowlingGameTest(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def test_gutter_game(self):
        self.roll_input(0, 20)
        self.assertEqual(0, self.game.score())

    def test_all_ones(self):
        self.roll_input(1, 20)
        self.assertEqual(20, self.game.score())

    def test_one_spare(self):
        self.roll_spare()
        self.game.single_roll(3)
        self.roll_input(0, 17)
        self.assertEqual(16, self.game.score())

    def test_one_strike(self):
        self.game.single_roll(10)
        self.game.single_roll(3)
        self.game.single_roll(4)
        self.roll_input(0, 16)
        self.assertEqual(24, self.game.score())

    def test_perfect_game(self):
        self.roll_input(10, 12)
        self.assertEqual(300, self.game.score())

    def test_simple_game(self):
        for pins in ['X', '7', '/', '9', '-', 'X', '-', '8', '8', '/', '-', '6', 'X', 'X', 'X', '8', '1']:
            self.game.single_roll(pins)
        self.assertEqual(167, self.game.score())
        
    def test_simple_game1(self):
        for pins in ['X', 'X', '1', '/', '-', '/', '-', '8', '8', '/', '-', '6', '3', '-', '2', '/', '1', '7']:
            self.game.single_roll(pins)
        self.assertEqual(107, self.game.score())

    def roll_input(self, pins, num):
        for i in range(num):
            self.game.single_roll(pins)

    def roll_spare(self):
        self.game.single_roll(5)
        self.game.single_roll(5)
        
if __name__ == '__main__':
    unittest.main()