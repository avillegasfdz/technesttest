import unittest

from oddsum_project.src.oddsum.oddsum import OddException,OddSum


class OddSumTestCase(unittest.TestCase):
    """ Class for OddSum unit tests    """
    def test(self):
        """ Tests adding odds and even numbers (all possibilities) """
        self.assertEqual(OddSum.sum(1, 3), 4)
        with self.assertRaises(OddException):
            OddSum.sum(2, 3)
        with self.assertRaises(OddException):
            OddSum.sum(2, 4)
        with self.assertRaises(OddException):
            OddSum.sum(1, 4)


if __name__ == '__main__':
    unittest.main()
