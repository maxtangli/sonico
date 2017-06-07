#!python

from second_code import SimpleBars
import unittest


class testSimpleBars(unittest.TestCase):
    def setUp(self):
        pass

    def test_str(self):
        self.assertEquals(str(SimpleBars("     ")), "     ")
        self.assertEquals(str(SimpleBars("iTiTi")), "iTiTi")

    def test_len(self):
        self.assertEquals(len(SimpleBars("iTiTi")), 5)
        self.assertEquals(len(SimpleBars(" " * 80)), 80)

    def test_simple_rule(self):
        self.assertEquals(str(SimpleBars("     ").next()), "     ")
        self.assertEquals(str(SimpleBars("  i  ").next()), " iTi ")
        self.assertEquals(str(SimpleBars(" i i ").next()), "iT Ti")
        self.assertEquals(str(SimpleBars("  T  ").next()), "  i  ")
        self.assertEquals(str(SimpleBars(" TiT ").next()), "  T  ")
        self.assertEquals(str(SimpleBars(" iTi ").next()), "iTiTi")
        self.assertEquals(str(SimpleBars(" TTT ").next()), " iii ")

    def test_loop(self):
        bs = SimpleBars("Ti  ")
        self.assertEquals(str(bs.next()), " Ti ")
        self.assertEquals(str(bs.next()), "  Ti")
        self.assertEquals(str(bs.next()), "i  T")
        self.assertEquals(str(bs.next()), "Ti  ")
        bs = SimpleBars("  iT")
        self.assertEquals(str(bs.next()), " iT ")
        self.assertEquals(str(bs.next()), "iT  ")
        self.assertEquals(str(bs.next()), "T  i")
        self.assertEquals(str(bs.next()), "  iT")

    def tearDown(self):
        pass


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(testSimpleBars))
    unittest.TextTestRunner(verbosity=2).run(suite)
