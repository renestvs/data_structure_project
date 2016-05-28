__author__ = 'rene_'

from django.test import TestCase
from data_structure.second_bim import graph, pattern_searching

class Second_Bim_Test(TestCase):

    graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

    def graph_test(self):
        c = graph
        path = []
        c.find_path(graph, 'A', 'D', path)
        #self.assertEqual((c.joshepus2(13, 3) + 1), 13)

    def pattern_test(self):
        c = pattern_searching

        text = "GEEKS FOR GEEKS"
        word = "GEEK"
        q = 101  # A prime number
        c.kr(text, word, q)

        text = c.convert_string("abacaabaccabacabaabb")
        word = c.convert_string("abacab")
        self.assertEqual(c.kmp(text, word), 19)
        self.assertEqual(c.bm(text, word), 16)
        self.assertEqual(c.brute_force(text, word), 23)


        text = c.convert_string("HERE IS A SIMPLE EXAMPLE")
        word = c.convert_string("EXAMPLE")
        self.assertEqual(c.kmp(text, word), 27)
        self.assertEqual(c.bm(text, word), 16)
        self.assertEqual(c.brute_force(text, word), 17)

        text = c.convert_string("Faturei com folga na prova de complexidade de algoritmos")
        word = c.convert_string("algo")
        self.assertEqual(c.kmp(text, word), 55)
        self.assertEqual(c.bm(text, word), 19)
        self.assertEqual(c.brute_force(text, word), 50)

        text = c.convert_string("esta prova e mais longa que complicada")
        word = c.convert_string("cada")
        self.assertEqual(c.kmp(text, word), 39)
        self.assertEqual(c.bm(text, word), 18)
        self.assertEqual(c.brute_force(text, word), 34)


        text = c.convert_string("A jabuticaba acabou de acabar")
        word = c.convert_string("cabar")
        self.assertEqual(c.kmp(text, word), 31)
        self.assertEqual(c.bm(text, word), 13)
        self.assertEqual(c.brute_force(text, word), 29)


        text = c.convert_string("vi na mata uma arara e duas aranhas")
        word = c.convert_string("araras")
        self.assertEqual(c.kmp(text, word), 46)
        self.assertEqual(c.bm(text, word), 9)
        self.assertEqual(c.brute_force(text, word), 37)


        text = c.convert_string("a pattern matching algorithm")
        word = c.convert_string("rithm")
        self.assertEqual(c.kmp(text, word), 29)
        self.assertEqual(c.bm(text, word), 12)
        self.assertEqual(c.brute_force(text, word), 23)