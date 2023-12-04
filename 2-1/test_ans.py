import unittest
import ans

class Testing(unittest.TestCase):
    def test_getcubes(self):
        self.assertEqual(ans.getcubes('Game 1: 2 blue, 4 green; 7 blue, 1 red, 14 green; 5 blue, 13 green, 1 red; 1 red, 7 blue, 11 green '),  [{'blue': 2, 'green': 4}, {'blue': 7, 'green': 14, 'red': 1}, {'blue': 5, 'green': 13, 'red': 1}, {'blue': 7, 'green': 11, 'red': 1}])

    def test_check(self):
        "Game 1: 2 blue, 4 green; 7 blue, 1 red, 14 green; 5 blue, 13 green, 1 red; 1 red, 7 blue, 11 green"
        self.assertEqual(ans.checksub({'blue': 2, 'green': 4}), True)

if __name__ == '__main__':
    unittest.main()
