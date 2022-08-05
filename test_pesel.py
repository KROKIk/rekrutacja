import unittest
from pesel import validate_pesel


class Test(unittest.TestCase):

    def test_positives(self):
        f = open("positives.txt", "r")
        for pesel in f:
            self.assertTrue(validate_pesel(pesel))
        f.close()

    def test_negatives(self):
        f = open("negatives.txt", "r")
        for pesel in f:
            self.assertFalse(validate_pesel(pesel))
        f.close()


if __name__ == '__main__':
    unittest.main()
