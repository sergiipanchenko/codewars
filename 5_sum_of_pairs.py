import unittest


# Time: 6349ms Passed: 12 Failed: 0
# def sum_pairs(ints, s):
#     check_dict = {}
#
#     for num in ints:
#         remainder = s - num
#
#         if remainder in check_dict:
#             return [remainder, num]
#
#         check_dict[num] = num


# Time: 6926ms Passed: 12 Failed: 0
def sum_pairs(ints_lst, target):
    seen = set()

    for num in ints_lst:
        if target - num in seen:
            return [target - num, num]
        seen.add(num)


class Tests(unittest.TestCase):
    def test_sum_pairs(self):
        self.assertEqual(sum_pairs([1, 4, 8, 7, 3, 15], 8), [1, 7])
        self.assertEqual(sum_pairs([1, -2, 3, 0, -6, 1], -6), [0, -6])
        self.assertEqual(sum_pairs([20, -13, 40], -7), None)
        self.assertEqual(sum_pairs([1, 2, 3, 4, 1, 0], 2), [1, 1])
        self.assertEqual(sum_pairs([10, 5, 2, 3, 7, 5], 10), [3, 7])
        self.assertEqual(sum_pairs([4, -2, 3, 3, 4], 8), [4, 4])
        self.assertEqual(sum_pairs([0, 2, 0], 0), [0, 0])
        self.assertEqual(sum_pairs([5, 9, 13, -3], 10), [13, -3])


if __name__ == '__main__':
    unittest.main()
