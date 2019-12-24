import unittest


def sum_dig_pow(a, b):
    result = []

    for num in range(a, b+1):
        sum_pow = 0
        for pow, digit in enumerate(str(num), 1):
            sum_pow += int(digit) ** pow
        if sum_pow == num:
            result.append(num)

    return result


class Tests(unittest.TestCase):
    def test_take_a_number_and_sum(self):
        self.assertEqual(sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
        self.assertEqual(sum_dig_pow(89, 135), [89, 135])


if __name__ == '__main__':
    unittest.main()
