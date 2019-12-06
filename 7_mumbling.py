import unittest


# Time: 794ms Passed: 120 Failed: 0
def accum(s):
    mumbling = []

    for index, char in enumerate(s):
        mumble = char*(index+1)
        mumbling.append(mumble.capitalize())

    return '-'.join(mumbling)


class Tests(unittest.TestCase):
    def test_accum(self):
        self.assertEqual(accum('abcd'), 'A-Bb-Ccc-Dddd')
        self.assertEqual(accum('RqaEzty'), 'R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy')
        self.assertEqual(accum('cwAt'), 'C-Ww-Aaa-Tttt')
        self.assertEqual(accum('GaP'), 'G-Aa-Ppp')
        self.assertEqual(accum('Codewars'), 'C-Oo-Ddd-Eeee-Wwwww-Aaaaaa-Rrrrrrr-Ssssssss')


if __name__ == '__main__':
    unittest.main()
