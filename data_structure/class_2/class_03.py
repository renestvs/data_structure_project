from math import floor

__author__ = 'rene_'

###################################
####           Stack           ####
###################################

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def binary(s, n):
    while n > 0:
        s.push(s, n%2)
        n = int(n/2)
    while len(s.self) != 0:
        print (s.top())
        s.pop()

def binary(n):
    aux = ""
    while n > 0:
        Stack.push(n%2)
        n = int(n/2)
    while Stack.isEmpty() is False:
        aux += Stack.top()
        Stack.pop()
    return aux


def inv_iter(i,f):
    while f > i:
        Stack.push(i+1,f-1)
    while Stack.isEmpty(f):
        (i,f) = Stack.pop()
        aux = v[f]
        v[f] = v[i]
        v[i] = aux



###################################
####           Nodes           ####
###################################
class No:

    def __init__(self, cargo=None, next=None, prev=None):
        self.cargo = cargo
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.cargo)

class Head:

    def __init__(self, next=None):
        self.next = next

    def __str__(self):
        return str(self.next)

class Tail:

    def __init__(self, next=None):
        self.next = next

    def __str__(self):
        return str(self.next)

def josephus(node, k):
    if (node != None):
        i = 0
        while i <= k:
            i+=1
            no = node.next
            print("passou = ", node.__str__())
            if (i == k):
                if(node.next != node):
                    print("matou = ", node.__str__())
                    i = 0
                    no.prev.next = no.next
                    no.next.prev = no.prev
                else:
                    return node.__str__()
    return None


###################################
####           Trees           ####
###################################
class Tree:

    def __init__(self, cargo=None, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


###################################
####            Stack          ####
###################################

class stack_array:

    max = 100
    array = [None] * max
    index = 0

    def is_empty(self):
        if self.index == 0:
            return True
        return False

    def is_full(self):
        if self.max == self.index:
            return True
        return False

    def top(self):
        if self.is_empty() == False:
            return self.array[self.index]
        return "Empty Stack"

    def pop(self):
        if self.is_empty() == False:
            self.array[self.index] = None
            self.index = self.index - 1
        else:
            return "Empty Stack"

    def push(self, cargo):
        if self.is_full() == False:
            self.array[self.index] = cargo
            self.index = self.index + 1
        else:
            return "Full Stack"

def polinomio_comum(x, i):
    if i == 0:
        return a[i]
    return pow(x,i) * a[1] + polinomio_comum(x, i-1)

def polinomio_horner(x, k):
    if k == 0:
        return a[k]
    return a[k-1] + x * polinomio_horner(x,k-1)

#def build(v):
    #for i=floor(n/2); i>0; i--:
     #   sift(i,n)

def max():
    return v[1]

def sift(x,i):
    return ""

size = 0
v = ["",""]
def extract_max():
    if size < 1:
        return "ERROR - Heap vazio"
    else:
        max = v[1]
        v[1] = v[size-1]
        sift (1, size)
        return max

def modify(k, x):
    if k > size or k < 1:
        return "ERROR"
    else:
        v[k] = x
        while k > 1 and v[int(floor(k/2))] < v[k]: # concerta para cima
            aux = v[k]
            v[k] = v[int(floor(k/2))]
            v[int(floor(k / 2))] = aux
            k = int(floor(k / 2))
        sift(k, size) #ou conserta para baixo

def insert(x):
    modify(size+1, x)

a = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
b = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
c = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

n = len(a)

# c = []
# b = []
# a = []
# i = 0
# j = 0
# k = 0
#
# def mult():
#     c[i,j] += a[i, k]*b[k,j]
#     k = k+1
#     if k > n:
#         k = 1
#         j = j+1
#         if j > n:
#             j = 1
#             i = i+1
#             if i > n:
#                 return 0
#     mult()


def test_tree():

    no1 = Tree(10)
    no2 = Tree(8)
    no3 = Tree(11)
    no4 = Tree(7)
    no5 = Tree(9)

    no1.left = no2
    no1.right = no3

    no2.left = no4
    no2.right = no5

    left = None
    right = None

    if (no1 == None):
        print("Arvore Vazia = TRUE")
        return True
    return vabb(no1, left, right)

menore = 99
maiore = 0
menord = 99
maiord = 0

def vabb(noh, min, max):

    if noh.left is None :
        min = int(noh.__str__())
        print("1st IF - ", min)
    else:
        print("1st call (noh.left, menore, maiore) - ", noh.left, menore, maiore)
        x = vabb(noh.left, menore, maiore)
        print("int(noh.__str__()) < maiore ", int(noh.__str__()), maiore, int(noh.__str__()) < maiore)
        if x is False or int(noh.__str__()) < maiore:
            return False
        min = menore
        print("min = menore", min)
    if noh.right is None:
        max = int(noh.__str__())
        print("2nd IF - ", max)
    else:
        print("2nd call (noh.right, menord, maiord) - ", noh.right, menord, maiord)
        x = vabb(noh.right, menord, maiord)
        print("int(noh.__str__()) > menord ", int(noh.__str__()), menord, int(noh.__str__()) > menord)
        if x is False or int(noh.__str__()) > menord:
            return False
        max = maiord
        print("max = maiord", max)
    print("===RETURN TRUE===")
    return True