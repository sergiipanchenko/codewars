# https://www.codewars.com/kata/human-readable-duration-format
import unittest


# best practice
def format_duration(seconds):
    if not seconds:
        return 'now'

    minute, second = divmod(seconds, 60)
    hour, minute = divmod(minute, 60)
    day, hour = divmod(hour, 24)
    year, day = divmod(day, 365)


    periods = {'year': year, 'day': day, 'hour': hour, 'minute': minute, 'second': second}
    result_list = []

    for each in periods:
        if periods[each]:
            plupal = str(each)

            if periods[each] > 1:
                plupal += 's'

            result_list.append(str(periods[each])+' '+plupal)

    if len(result_list) == 1:
        return str(result_list[0])
    elif len(result_list) == 2:
        return str(result_list[0]+' and '+result_list[1])

    return ', '.join(result_list[:-2]) + ', ' + result_list[-2]+' and '+result_list[-1]


class Tests(unittest.TestCase):
    def test_format_duration(self):
        self.assertEqual(format_duration(1), '1 second')
        self.assertEqual(format_duration(62), '1 minute and 2 seconds')
        self.assertEqual(format_duration(120), '2 minutes')
        self.assertEqual(format_duration(3600), '1 hour')
        self.assertEqual(format_duration(3662), '1 hour, 1 minute and 2 seconds')
        self.assertEqual(format_duration(37863462), '1 year, 73 days, 5 hours, 37 minutes and 42 seconds')


if __name__ == '__main__':
    unittest.main()
