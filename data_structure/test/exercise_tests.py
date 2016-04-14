__author__ = 'rene_'

from django.test import TestCase
from data_structure.class_2 import exercise

class ExerciseTest(TestCase):

    # def descrente_test(self):
    #     c = exercise
    #     c.descrente(10)
    #
    # def crescente_test(self):
    #     c = exercise
    #     c.crescente(10)
    #
    # def descre_test(self):
    #     c=exercise
    #     c.descre(10)
    #
    # def converte_test(self):
    #     c=exercise
    #     self.assertEqual(c.converte(10), "1010")
    #
    # def binary (self):
    #     x = 25
    #     while (x > 0):
    #         print (x)
    #         x = int(x/2)
    #     print ("Goodbye")

    def produto_interno_test(self):
        u = [1, 2, 3, 4]
        v = [1, 2, 3, 4]
        c = exercise
        self.assertEqual(c.produto_interno(u,v,3), 30)
