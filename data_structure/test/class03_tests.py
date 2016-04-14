__author__ = 'rene_'

from django.test import TestCase
from data_structure.class_2 import class_03

class Class3Test(TestCase):

    def test_tree(self):
        c = class_03

        print (c.test_tree())





    def test_noh(self):
         c = class_03

         no1 = c.No(1)
         no2 = c.No(2)
         no3 = c.No(3)
         no4 = c.No(4)
         no5 = c.No(5)
         no6 = c.No(6)
         no7 = c.No(7)


         head = c.Head(no1)
         tail = c.Tail(no7)

         no1.next = no2
         no2.next = no3
         no3.next = no4
         no4.next = no5
         no5.next = no6
         no6.next = no7
         no7.next = no1

         no1.prev = no7
         no2.prev = no1
         no3.prev = no2
         no4.prev = no3
         no5.prev = no4
         no6.prev = no5
         no7.prev = no6

         no = head.next
         k = 2
         # while no != tail.next:
         #     print (no.__str__())
         #     no = no.next

         if (no != None):
             i = 0
             while i <= k:
                 print("passou = ", no.__str__())
                 if (i == k):
                     if (no.next != no):
                         print("matou = ", no.__str__())
                         no.prev.next = no.next
                         no.next. prev = no.prev
                         no = no.next
                         i = 0
                     else:
                         print("VENCEDOR = ", no.__str__())
                         break
                 else:
                    i += 1
                    no = no.next

         # #self.assertEqual(no.carga,"teste")

    def test_stack_array(self):
        c = class_03

        stack = c.stack_array

        self.assertEqual(stack.is_empty(stack),True)

        stack.push(stack, 1)
        stack.push(stack, 2)

        stack.top(stack)

    def binary_test(self):
        c = class_03
        s = c.Stack
        c.binary(s, 10)

if __name__ == '__main__':
    TestCase.main()


