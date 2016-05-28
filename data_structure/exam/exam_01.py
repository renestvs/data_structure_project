__author__ = 'rene_esteves'

class exam_01:

    def somadig(self, input):
        if input < 0: #base case
            return int(self.somadig(self, -input))
        if input == 0: #base case
            return 0
        return input%10 + int(self.somadig(self, input/10))


exam_01.somadig(exam_01, 10000);

####################################################
##############     Question 10     #################
##############     by Prof. Alonso #################
####################################################

V = []

def sift (i,n):
    while i <= (n/2):
        maior = V[i]
        if maior < V[2*i]:
            maior = V[2*i]
            x = 2*i
        if 2*i + 1 <= n:
           if maior < V[2*i+1]:
               maior = V[2*i+1]
               x = 2*i + 1
        if maior != V[i]:
            aux = V[i]
            V[i] = V[x]
            V[x] = aux
            i = x
        else:
            i = n

####################################################
##############     Question 10     #################
##############     by Rene         #################
####################################################

V = []

def sift (i,n):
    swap = True
    while swap:
        maior = i
        esq = 2*i
        dir = 2*i+1
        if esq <= n and V[esq] > V[maior]:
            maior = esq
        if dir <= n and V[dir] > V[maior]:
            maior = dir
        if maior != i:
            aux = V[maior]
            V[maior] = V[i]
            V[i] = aux
            i = maior
        else:
            swap = False

####################################################
##############     Question 03     #################
##############     by Rene         #################
####################################################

V = []

def vabb (node):
    if node == None:
        return True
    h = log(2, sum_nodes(node, 0) + 1) #h=lg n+1
    if h != floor(h):
        return False
    return True

def sum_nodes(node):
    if node != None:
        a = sum_nodes(node.esq)
        b = sum_nodes(node.dir)
        return a+b+1

####################################################
##############     Question 03     #################
##############     by Prof. Alonso #################
####################################################

#Calcula a altura das sub-arvores; e
#Se todos os nós tem dois filhos.

def completa (node):
    if node is None:
        return True
    comp = True
    h1 = testh(comp, node.esq)
    h2 = testh(comp, node.dir)
    return comp and (h1 == h2)

def testh(comp, node):
    if node is None or comp is False:
        return 0
    if (node.esq is None and node.dir is None) or (node.esq != None and node.dir is None):
        c = False
        return 0
    h1 = testh(comp, node.esq)
    h2 = testh(comp, node.dir)
    comp = comp and (h1 == h2)
    return h1 + 1
















