__author__ = 'rene_esteves'

from django.test import TestCase
from data_structure.class_2 import class_02

class Class2Test(TestCase):

    def test_factorial(self):
         c = class_02
         self.assertEqual(c.factorial(5),120)
         self.assertEqual(c.factorial(1),1)

    def test_sum(self):
        c = class_02
        self.assertEqual(c.sum(5),15)
        self.assertEqual(c.sum(2),3)
        self.assertEqual(c.sum(1),1)

    def test_fibonacci(self):
        c = class_02
        self.assertEqual(c.fibonacci(50),7778742049)
        #self.assertEqual(c.fibonacci(5), 8)

    def test_cres_natural_order(self):
        c = class_02
        c.cres_natural_order(5)
        print(" <= Manual_Test - cres_natural_order")

    def test_descres_natural_order(self):
        c = class_02
        c.descres_natural_order(10)
        print(" <= Manual_Test - descres_natural_order")

    def test_array_max(self):
        c = class_02
        array = [1,5,2,7,6]
        #c.array_max(array, 5)
        self.assertEqual(c.array_max(array, 5),7)

    def test_is_true(self):
        c = class_02
        array = [1,12,3,4,5,6,7,8,9,13]
        self.assertEqual(c.is_true(array, 0, 10),False)
        self.assertEqual(c.is_true(array, 0, 1),True)

    def test_seekvalue(self):
        c = class_02
        array = [1, 12, 3, 4, 5, 6, 7, 8, 9, 13]
        self.assertEqual(c.seekvalue(array, 10, 10), False)
        self.assertEqual(c.seekvalue(array, 10, 1), True)


    def test_binary_search(self):
        c = class_02
        array = [3,4,5,6,7,8,9,12,14,16,20]
        self.assertEqual(c.binary_search(array, 0, 10, 20), True)

    def test_sum_array(self):
        c = class_02
        array = [1,1,1,2]
        self.assertEqual(c.sum_array(array, 0),5)

    def test_invt_array(self):
        c = class_02
        array = [1,2,3,4,5,6,7,8]
        self.assertEqual(c.invt_array(array,0),None)

    def test_decimal_to_binary(self):
        c = class_02
        self.assertEqual(c.decimal_to_binary(10),"1010")

    def test_factoring(self):
        c = class_02
        self.assertEqual(c.factoring(4), 2.083333333333333)

    def test_expo(self):
        c = class_02
        self.assertEqual(c.exp(3,4), 81)

    def test_sumdig(self):
        c = class_02
        self.assertEqual(c.sumdig(1978), 25)

    def test_invdig(self):
        c = class_02
        self.assertEqual(c.invdig(1978, 3), 8791)

    def test_josephus(self):
        c = class_02
        c.josephus(5, 2)
        self.assertEqual(c.josephus(6, 2), 1)

    def test_triangle(self):
        c = class_02
        self.assertEqual(c.triangle(5), 15)

    def test_quad(self):
        c = class_02
        self.assertEqual(c.quad(5), 23)

    def test_mdc(self):
        c = class_02
        self.assertEqual(c.mdc(12,9), 3)


    def test_seekvalue2(self):
        c = class_02
        array = [1, 12, 3, 4, 5, 6, 7, 8, 9, 13]
        self.assertEqual(c.seekvalue2(array, 9, 10), False)
        self.assertEqual(c.seekvalue2(array, 9, 1), True)

    def test_is_true(self):
        c = class_02
        array = [0,1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(c.buscabinaria(array, 0, 10, 5),True)
        self.assertEqual(c.buscabinaria(array, 0, 10, 2),True)
        self.assertEqual(c.buscabinaria(array, 0, 10, 9), True)
        self.assertEqual(c.buscabinaria(array, 0, 10, 10), True)
        self.assertEqual(c.buscabinaria(array, 0, 10, 0), True)
        self.assertEqual(c.buscabinaria(array, 0, 10, 55), False)

    def test_is_true(self):
        c = class_02
        self.assertEqual(c.inverter(123, 2), 321)
        self.assertEqual(c.inverter(1234, 3), 4321)

    def test_inv_array(self):
        c = class_02
        c.v = [1,2,3,4,5,6,7,8,9]
        c.inv_array(0,8)
        print(c.v)

if __name__ == '__main__':
    TestCase.main()
