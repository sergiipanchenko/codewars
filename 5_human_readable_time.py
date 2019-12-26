import unittest


# Time: 797ms Passed: 108 Failed: 0
def make_readable(seconds):
    mins, secs = divmod(seconds, 60)
    hours, mins = divmod(mins, 60)
    return str(hours).rjust(2, '0')+':'+str(mins).rjust(2, '0')+':'+str(secs).rjust(2, '0')


class Tests(unittest.TestCase):
    def test_dots_and_boxes(self):
        self.assertEqual(make_readable(0), '00:00:00')
        self.assertEqual(make_readable(5), '00:00:05')
        self.assertEqual(make_readable(60), '00:01:00')
        self.assertEqual(make_readable(86399), '23:59:59')
        self.assertEqual(make_readable(359999), '99:59:59')


if __name__ == '__main__':
    unittest.main()
