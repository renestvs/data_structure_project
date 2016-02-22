from django.test import TestCase

from data_structure.class_2 import class_02

class Class2Test(TestCase):

    def test_factorial(self):
         c = class_02
         self.assertEqual(c.factorial(5),120)
         self.assertEqual(c.factorial(1),1)

    def test_factorial_graph(self):
         c = class_02
         c.factorial_graph(5)

    def test_sum(self):
        c = class_02
        self.assertEqual(c.sum(5),15)
        self.assertEqual(c.sum(2),3)
        self.assertEqual(c.sum(1),1)

if __name__ == '__main__':
    TestCase.main()
