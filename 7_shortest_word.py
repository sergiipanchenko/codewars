import unittest


# Time: 761ms Passed: 45 Failed: 0
def find_short(s):
    words = s.split()
    shortest = len(words[0])
    
    for word in words:
        if len(word) < shortest:
            shortest = len(word)
    
    return shortest


class Tests(unittest.TestCase):
    def test_find_short(self):
        self.assertEqual(find_short('lets talk about javascript the best language'), 3)
        self.assertEqual(find_short('i want to travel the world writing code one day'), 1)
        self.assertEqual(find_short('Lets all go on holiday somewhere very cold'), 2)


if __name__ == '__main__':
    unittest.main()
