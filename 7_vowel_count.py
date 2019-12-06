import unittest


# Time: 789ms Passed: 5 Failed: 0
def get_count(inputStr):
    num_vowels = 0
    vowels = 'aeiou'

    for letter in inputStr:
        if letter in vowels:
            num_vowels += 1

    return num_vowels


# best practice
# def get_count(inputStr):
#     return sum(1 for c in inputStr if c in 'aeiou')


class Tests(unittest.TestCase):
    def test_accum(self):
        self.assertEqual(get_count('abracadabra'), 5)


if __name__ == '__main__':
    unittest.main()