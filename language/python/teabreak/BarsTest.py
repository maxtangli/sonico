#!python

from second_code import Bars
import unittest


class TestBars(unittest.TestCase):
    def setUp(self):
        pass

    def test_simple_rule(self):
        self.assertEqual(str(Bars("     ").next()), "     ")
        self.assertEqual(str(Bars("  i  ").next()), " iTi ")
        self.assertEqual(str(Bars(" i i ").next()), "iT Ti")
        self.assertEqual(str(Bars("  T  ").next()), "  i  ")
        self.assertEqual(str(Bars(" TiT ").next()), "  T  ")
        self.assertEqual(str(Bars(" iTi ").next()), "iTiTi")
        self.assertEqual(str(Bars(" TTT ").next()), " iii ")

    def test_rule(self):
        self.assertEqual(str(Bars(" I  ").next()), "iIi ")
        self.assertEqual(str(Bars(" ii ").next()), "iIIi")
        self.assertEqual(str(Bars(" Ii ").next()), "iTIi")
        self.assertEqual(str(Bars(" TI ").next()), "  Ii")
        self.assertEqual(str(Bars(" II ").next()), "iTTi")

    def test_loop(self):
        bs = Bars("Ti  ")
        self.assertEqual(str(bs.next()), " Ti ")
        self.assertEqual(str(bs.next()), "  Ti")
        self.assertEqual(str(bs.next()), "i  T")
        self.assertEqual(str(bs.next()), "Ti  ")
        bs = Bars("  iT")
        self.assertEqual(str(bs.next()), " iT ")
        self.assertEqual(str(bs.next()), "iT  ")
        self.assertEqual(str(bs.next()), "T  i")
        self.assertEqual(str(bs.next()), "  iT")

    def test_next(self):
        bs = Bars("I    IT ii  i I   I i   i   I  T")
        bs.next()
        self.assertEqual(str(bs), "Ii  iI iIIiiT Ii iI Ti iTi iIi  ")
        bs.next()
        self.assertEqual(str(bs), "TIiiIT IIITI iTI ITi T TiT IIIii")

    def tearDown(self):
        pass


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestBars))
    unittest.TextTestRunner(verbosity=2).run(suite)
