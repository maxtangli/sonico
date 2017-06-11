#!python

from second_code import SimpleBars
import unittest


class TestSimpleBars(unittest.TestCase):
    def setUp(self):
        pass

    def test_str(self):
        self.assertEqual(str(SimpleBars("     ")), "     ")
        self.assertEqual(str(SimpleBars("iTiTi")), "iTiTi")

    def test_len(self):
        self.assertEqual(len(SimpleBars("iTiTi")), 5)
        self.assertEqual(len(SimpleBars(" " * 80)), 80)

    def test_simple_rule(self):
        self.assertEqual(str(SimpleBars("     ").next()), "     ")
        self.assertEqual(str(SimpleBars("  i  ").next()), " iTi ")
        self.assertEqual(str(SimpleBars(" i i ").next()), "iT Ti")
        self.assertEqual(str(SimpleBars("  T  ").next()), "  i  ")
        self.assertEqual(str(SimpleBars(" TiT ").next()), "  T  ")
        self.assertEqual(str(SimpleBars(" iTi ").next()), "iTiTi")
        self.assertEqual(str(SimpleBars(" TTT ").next()), " iii ")

    def test_loop(self):
        bs = SimpleBars("Ti  ")
        self.assertEqual(str(bs.next()), " Ti ")
        self.assertEqual(str(bs.next()), "  Ti")
        self.assertEqual(str(bs.next()), "i  T")
        self.assertEqual(str(bs.next()), "Ti  ")
        bs = SimpleBars("  iT")
        self.assertEqual(str(bs.next()), " iT ")
        self.assertEqual(str(bs.next()), "iT  ")
        self.assertEqual(str(bs.next()), "T  i")
        self.assertEqual(str(bs.next()), "  iT")

    def tearDown(self):
        pass


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSimpleBars))
    unittest.TextTestRunner(verbosity=2).run(suite)
