from collections import defaultdict
from collections import namedtuple
from itertools import product

from pip._vendor.requests.packages.urllib3.connectionpool import xrange

__author__ = 'rene_'

######################
##### chapter 10 #####
######################

def make_change(moedas, troco):
    #moedas -  vetor de moedas disponiveis (menor e de 1 centavo)
    quant = [0]
    ultima = [0]
    for cents in xrange(1,troco):
        quantProv = cents # solucao provisoria: todas de 1 centavo
        ultProv = 1 # ultima moeda dessa solucao
        for j in xrange(0,len(moedas)):
            if moedas[j] > cents:
                continue # essa moeda nao serve
            if quant[cents-moedas[j]] + 1 < quantProv:
                quantProv = quant[cents - moedas[j]] + 1
                ultProv = moedas[j]
        quant[cents] = quantProv #solucao para troco=cents
        ultima[cents] = ultProv #ultima moeda dessa solucao


d, T, N = [], [], []
def matrix_chain(n):
    global N, T
    for i in n:
        N[i,i].append(0) # subproblemas triviais
    for b in xrange(1,n): #tamanho dos subproblemas
        for i in xrange(0, n-b):
            j = i+b #novo intervalo para o subproblema
            N[i,j].append(int('inf')) # valor provisorio para a solucao
            T[i,j].append(i) #valor provisorio para a solucao
            for k in xrange(i,j): #equacao de calculo
                x = N[i,k] + N[k+1,j] + d[i]*d[k+1]*d[j+1]
                if N[i,j] > x:
                    N[i,j].append(x)
                    T[i,j].append(k)
    return N[0,n-1]

#===========
#===LCS=====
def lcs_grid(xs, ys):
    '''Create a grid for longest common subsequence calculations.

    Returns a grid where grid[(j, i)] is a pair (n, move) such that
    - n is the length of the LCS of prefixes xs[:i], ys[:j]
    - move is \, ^, <, or e, depending on whether the best move
      to (j, i) was diagonal, downwards, or rightwards, or None.

    Example:
       T  A  R  O  T
    A 0< 1\ 1< 1< 1<
    R 0< 1^ 2\ 2< 2<
    T 1\ 1< 2^ 2< 3\
    '''
    Cell = namedtuple('Cell', 'length move')
    grid = defaultdict(lambda: Cell(0, 'e'))
    sqs = product(enumerate(ys), enumerate(xs))
    for (j, y), (i, x) in sqs:
        if x == y:
            cell = Cell(grid[(j-1, i-1)].length + 1, '\\')
        else:
            left = grid[(j, i-1)].length
            over = grid[(j-1, i)].length
            if left < over:
                cell = Cell(over, '^')
            else:
                cell = Cell(left, '<')
        grid[(j, i)] = cell
    return grid

def lcs(xs, ys):
    '''Return a longest common subsequence of xs, ys.'''
    # Create the LCS grid, then walk back from the bottom right corner
    grid = lcs_grid(xs, ys)
    i, j = len(xs) - 1, len(ys) - 1
    lcs = list()
    for move in iter(lambda: grid[(j, i)].move, 'e'):
        if move == '\\':
            lcs.append(xs[i])
            i -= 1
            j -= 1
        elif move == '^':
            j -= 1
        elif move == '<':
            i -= 1
    lcs.reverse()
    return lcs

#============
p, w, B = [], [], []
def knapsack(c, n):
    global B, w, p
    for i in c:
        B[0,i].append(0) # nenhum item e considerado
    for k in xrange(1,n): #incremetno nos itens
        for i in c: #incremento na capacidade
            if w[k] > i:
                B[k,i].append(B[k-1,i])
            else:
                B[k,i].append(max(B[k-1,i], B[k-1, i-w[k]] + p[k]))
    return B[n,c]

X = []

def vetorx(c, n):
    global B, X
    r = c #peso disponivel na mochila
    s = B[n,c] #lucro corrente
    for i in xrange(n,0,-1):
        if B[i-1,r] == s:
            X[i].append(0) # item i nao entrou
        else:
            X[i].append(1) #item i entrou
            s -= p[i]
            r -= w[i]

######################################
###########  memoization #############
######################################

def memoize(f):
    cache = {}
    return lambda *args: cache[args] if args in cache else cache.update({args: f(*args)}) or cache[args]

@memoize
def fibonacci(n):
    return n if n < 2 else fibonacci(n-2) + fibonacci(n-1)

items = []

def knapsack(item, maxweight):
    #
    # """
    # Solve the knapsack problem by finding the most valuable
    # subsequence of `items` subject that weighs no more than
    # `maxweight`.
    #
    # `items` is a sequence of pairs `(value, weight)`, where `value` is
    # a number and `weight` is a non-negative integer.
    #
    # `maxweight` is a non-negative integer.
    #
    # Return a pair whose first element is the sum of values in the most
    # valuable subsequence, and whose second element is the subsequence.
    #
    # #>>> items = [(4, 12), (2, 1), (6, 4), (1, 1), (2, 2)]
    # #>>> knapsack(items, 15)
    # (11, [(2, 1), (6, 4), (1, 1), (2, 2)])
    # """
    global items
    items = item
    j = maxweight
    result = []
    for i in xrange(len(items), 0, -1):
        if knapsack_bestvalue(i, j) != knapsack_bestvalue(i - 1, j):
            result.append(items[i - 1])
            j -= items[i - 1][1]
    result.reverse()
    return knapsack_bestvalue(len(items), maxweight), result

# Return the value of the most valuable subsequence of the first i
# elements in items whose weights sum to no more than j.
@memoize
def knapsack_bestvalue(i, j):
    global items
    if i == 0: return 0
    value, weight = items[i - 1]
    if weight > j:
        return knapsack_bestvalue(i - 1, j)
    else:
        return max(knapsack_bestvalue(i - 1, j),
                   knapsack_bestvalue(i - 1, j - weight) + value)

    #Example
    #lcs("HUMAN", "CHIMPANZEE")
    #['H', 'M', 'A', 'N']

xs, ys = "",""
def lcs(__xs__, __ys__):
    '''Return the longest subsequence common to xs and ys.'''
    global xs,ys
    xs = __xs__
    ys = __ys__
    return lcs_(len(xs), len(ys))

@memoize
def lcs_(i, j):
    global xs, ys
    if i and j:
        xe, ye = xs[i-1], ys[j-1]
        if xe == ye:
            return lcs_(i-1, j-1) + [xe]
        else:
            return max(lcs_(i, j-1), lcs_(i-1, j), key=len)
    else:
        return []

@memoize
def make_change_memoization(amount, coins):
    numberofcoins = 0
    actualcoins = {}
    if len(coins) == 1:
        numberofcoins =  amount / coins[0]
        actualcoins[coins[0]] = numberofcoins
    elif amount == 1:
        numberofcoins = 1
        actualcoins[coins[0]] = 1
    elif amount == 0:
        numberofcoins = 0
    else:
        if (amount - coins[-1]>= 0):
            sol1 = make_change_memoization(amount-coins[-1], coins)
            sol2 = make_change_memoization(amount, coins[:-1])
            numberofcoins += min(1+ sol1[0], sol2[0])
            if 1+ sol1[0]<sol2[0]:
                if coins[-1] in actualcoins:
                    actualcoins[coins[-1]] += 1
                else:
                    actualcoins[coins[-1]] = 1
                actualcoins = { x: actualcoins.get(x, 0) + sol1[1].get(x, 0) for x in set(actualcoins) | set(sol1[1]) }
            else:
                actualcoins = actualcoins + sol2[1]
                actualcoins = { x: actualcoins.get(x, 0) + sol2[1].get(x, 0) for x in set(actualcoins) | set(sol2[1]) }
        else:
            sol = make_change_memoization(amount, coins[:-1])
            numberofcoins += sol[0]
            actualcoins = { x: actualcoins.get(x, 0) + sol[1].get(x, 0) for x in set(actualcoins) | set(sol[1]) }
    return (numberofcoins, actualcoins)