__author__ = 'rene_'

def descrente(n):
    print(n)
    if n == 0: #base case
        return 0
    return descrente(n-1) #recursive call

def crescente(n):
    if n == 0:
        return print (n)
    crescente(n-1)
    return print(n)

# def descre(n):
#     print (n)
#     if n == 0:
#         return print(n)
#     descre(n-1)
#     return print(n)
#
# def converte(n):
#     if n <= 0: #base case
#         return str("")
#     return converte(int(n/2)) + str(n%2) #recursive call
#
# def somadig(a1, x):
#     if x == 0: # Base case
#         return a1[x][x]
#     return a1[x][x] + somadig(a1, x-1) #recursive call
#
#
# def Rec(n):
#     if (n==1):
#         return 1;
#     return 2*Rec(n-1) + Funcao(a1, n)
#
# def Funcao(a1, n):
#     for(i=0; i<n; i++):
#         for(j=i; j>0; j--):
#             for (k=j; k > 0; k--):
#                 a1[i][j][k] = 4*i*i+j
#     return a1[n-1,n-1, n-1]


def produto_interno(u,v,n):
    if n == 0:
        return u[n]*v[n]
    return u[n]*v[n] + produto_interno(u,v,n-1)

class Head:
    value = 0
    next = ""

class Position:
    head, next ,index = 0

class Node:
    next = None
    previous = None
    value = None

def remove(position): #O(1)
    position.head = None


# k = valor
# x = indice
def modify(k,x): #O(n)
    Position.index = 1
    Position = Head
    while Position.index < k:
        Position = Position.next
        Position.index += 1
    remove(Position) #O(1)
    insert(k) #O(n)

def insert(k): #O(n)
    Position = Head
    while k.value < Position.value:
        Node.previous = Position.previous
        Node.next = Position
        Node.previous.next = Node
        Position.previous = Node


#Prova

#metodo principal
def verifica_abb(raiz):
    if raiz is None:
        return True
    e , d = 0
    return v_abb(raiz, e, d)

def v_abb(node, min, max):
    menore, maiore, menord, maiord = 0
    if node.esq is None:
        min = node.value
    else:
        x = v_abb(node.esq, menore, maiord)
        if x is False or node.value < maiore:
            return False
        min = menore
    if node.dir is None:
        max = node.value
    else:
        x = v_abb(node.dir, menord, maiord)
        if x is False or node.value > menord:
            return False
        max = maiord
    return True

def binary(x):
    if x == 0:
        print (0)
    else:
        while x != 0:
            Stack.push(x%2)
            x /= 2
        while Stack.isEmpty() is True:
            print (Stack.top())
            Stack.pop()

