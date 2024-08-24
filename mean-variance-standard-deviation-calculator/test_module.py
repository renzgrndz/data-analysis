import unittest
import mean_var_std

class UnitTests(unittest.TestCase):

    def test_calculate(self):
        actual = mean_var_std.calculate([2, 6, 2, 8, 4, 0, 1, 5, 7])
        expected = {
            'mean': {
                'overall': 3.888888888888889,
                'rows': [3.3333333333333335, 4.0, 4.333333333333333],
                'columns': [3.6666666666666665, 5.0, 3.0]
            },
            'variance': {
                'overall': 7.555555555555555,
                'rows': [6.055555555555555, 6.0, 5.055555555555555],
                'columns': [6.055555555555555, 6.0, 5.055555555555555]
            },
            'std_dev': {
                'overall': 2.74747712125472,
                'rows': [2.463450445948467, 2.449489742783178, 2.249445164372851],
                'columns': [2.463450445948467, 2.449489742783178, 2.249445164372851]
            },
            'max': {
                'overall': 8,
                'rows': [8, 8, 7],
                'columns': [8, 6, 7]
            },
            'min': {
                'overall': 0,
                'rows': [0, 0, 1],
                'columns': [1, 0, 0]
            },
            'sum': {
                'overall': 35,
                'rows': [11, 12, 13],
                'columns': [11, 12, 13]
            },
        }
        self.assertDictEqual(actual, expected, "Expected different output when calling 'calculate()' with '[2,6,2,8,4,0,1,5,7]'")

    def test_calculate2(self):
        actual = mean_var_std.calculate([9, 1, 5, 3, 3, 3, 2, 9, 0])
        expected = {
            'mean': {
                'overall': 4.0,
                'rows': [5.0, 3.0, 3.6666666666666665],
                'columns': [4.666666666666667, 4.333333333333333, 2.6666666666666665]
            },
            'variance': {
                'overall': 6.666666666666667,
                'rows': [10.666666666666666, 0.0, 14.888888888888891],
                'columns': [9.555555555555555, 11.555555555555557, 4.222222222222222]
            },
            'std_dev': {
                'overall': 2.581988897471611,
                'rows': [3.265986323710904, 0.0, 3.8586123009300755],
                'columns': [3.0912061651652345, 3.39934634239519, 2.0548046676563256]
            },
            'max': {
                'overall': 9,
                'rows': [9, 3, 9],
                'columns': [9, 9, 5]
            },
            'min': {
                'overall': 0,
                'rows': [1, 3, 0],
                'columns': [0, 1, 0]
            },
            'sum': {
                'overall': 35,
                'rows': [15, 9, 11],
                'columns': [14, 13, 8]
            },
        }
        self.assertDictEqual(actual, expected, "Expected different output when calling 'calculate()' with '[9,1,5,3,3,3,2,9,0]'")

    def test_calculate_with_few_digits(self):
        with self.assertRaisesRegex(ValueError, "Input list must contain exactly 9 elements."):
            mean_var_std.calculate([2, 6, 2, 8, 4, 0, 1,])

if __name__ == '__main__':
    unittest.main()
