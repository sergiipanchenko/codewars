import unittest


# Time: 831ms Passed: 9 Failed: 0
def duplicate_count(text):
    counter = 0
    chars = {}

    for each in text:
        char = each.lower()
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    for each in chars.values():
        if each > 1:
            counter += 1

    return counter



class Tests(unittest.TestCase):
    def test_accum(self):
        self.assertEqual(duplicate_count('abcde'), 0)
        self.assertEqual(duplicate_count('abcdea'), 1)
        self.assertEqual(duplicate_count('indivisibility'), 1)
        self.assertEqual(duplicate_count('jack13os43john'), 3)
        self.assertEqual(duplicate_count('Codewars'), 0)


if __name__ == '__main__':
    unittest.main()
