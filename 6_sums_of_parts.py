import unittest


# Time: 5515ms Passed: 75 Failed: 0
def parts_sums(ls):
    sums = [0]*(len(ls)+1)

    for i in range(len(ls)-1, -1, -1):
        sums[i] = sums[i+1]+ls[i]

    return sums


class Tests(unittest.TestCase):
    def test_parts_sums(self):
        # self.assertEqual(parts_sums([]), [0])
        self.assertEqual(parts_sums([0, 1, 3, 6, 10]), [20, 20, 19, 16, 10, 0])
        self.assertEqual(parts_sums([1, 2, 3, 4, 5, 6]), [21, 20, 18, 15, 11, 6, 0])


if __name__ == '__main__':
    unittest.main()
