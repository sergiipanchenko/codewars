import unittest


# Time: 831ms Passed: 10 Failed: 0
def rgb(r, g, b):
    return conversion(r) + conversion(g) + conversion(b)


def conversion(n_dec):
    if n_dec < 0:
        n_dec = 0
    if n_dec > 255:
        n_dec = 255
    n_hex = str(hex(n_dec)[2:]).rjust(2, '0').upper()

    return n_hex


class Tests(unittest.TestCase):
    def test_rgb(self):
        self.assertEqual(rgb(0, 0, 0), '000000')
        self.assertEqual(rgb(1, 2, 3), '010203')
        self.assertEqual(rgb(255, 255, 255), 'FFFFFF')
        self.assertEqual(rgb(254, 253, 252), 'FEFDFC')
        self.assertEqual(rgb(-20, 275, 125), '00FF7D')


if __name__ == '__main__':
    unittest.main()
