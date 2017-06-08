#!python

from second_code import Bars
import unittest

class testBars(unittest.TestCase):
    def setUp(self):
        pass

    def test_simple_rule(self):
        self.assertEquals(str(Bars("     ").next()), "     ")
        self.assertEquals(str(Bars("  i  ").next()), " iTi ")
        self.assertEquals(str(Bars(" i i ").next()), "iT Ti")
        self.assertEquals(str(Bars("  T  ").next()), "  i  ")
        self.assertEquals(str(Bars(" TiT ").next()), "  T  ")
        self.assertEquals(str(Bars(" iTi ").next()), "iTiTi")
        self.assertEquals(str(Bars(" TTT ").next()), " iii ")

    def test_rule(self):
        self.assertEquals(str(Bars(" I  ").next()), "iIi ")
        self.assertEquals(str(Bars(" ii ").next()), "iIIi")
        self.assertEquals(str(Bars(" Ii ").next()), "iTIi")
        self.assertEquals(str(Bars(" TI ").next()), "  Ii")
        self.assertEquals(str(Bars(" II ").next()), "iTTi")

    def test_loop(self):
        bs = Bars("Ti  ")
        self.assertEquals(str(bs.next()), " Ti ")
        self.assertEquals(str(bs.next()), "  Ti")
        self.assertEquals(str(bs.next()), "i  T")
        self.assertEquals(str(bs.next()), "Ti  ")
        bs = Bars("  iT")
        self.assertEquals(str(bs.next()), " iT ")
        self.assertEquals(str(bs.next()), "iT  ")
        self.assertEquals(str(bs.next()), "T  i")
        self.assertEquals(str(bs.next()), "  iT")

    def test_next(self):
        bs = Bars("I    IT ii  i I   I i   i   I  T")
        bs.next()
        self.assertEquals(str(bs), "Ii  iI iIIiiT Ii iI Ti iTi iIi  ")
        bs.next()
        self.assertEquals(str(bs), "TIiiIT IIITI iTI ITi T TiT IIIii")

    def tearDown(self):
        pass

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(testBars))
    unittest.TextTestRunner(verbosity=2).run(suite)