from math import floor
from pip._vendor.requests.packages.urllib3.connectionpool import xrange

__author__ = 'rene_'

v = []
aux = []
size = []

############################################################
#######################  HeapSort  #########################
############################################################

def sift(i, n):
    esq = 2*i + 1
    dir = 2*i + 2
    maior = i
    print(esq, dir, maior)
    if esq < n and v[esq] > v[i]:
        maior = esq
        print("maior = esq", esq)
    if dir < n and v[dir] > v[maior]:
        maior = dir
        print("maior = dir", dir)
    if (maior != i):
        aux = v[i]
        v[i] = v[maior]
        v[maior] = aux
        print("sift", maior, n)
        sift(maior, n)


def sift_iterativo(i, n):
    swap = True
    while swap:
        esq = 2*i + 1
        dir = 2*i + 2
        maior = i
        if esq <= n and v[esq] > v[i]:
            maior = esq
        if dir <= n and v[dir] > v[maior]:
            maior = dir
        if (maior != i):
            aux = v[i]
            v[i] = v[maior]
            v[maior] = aux
            i = maior
        else:
            swap = False


def build():
    for i in xrange(int(floor(len(v)/2)-1), -1, -1):
        print("FOR - ", i)
        sift(i,len(v)-1)

def heapsort():
    print("==== build heap ====")
    build()
    print(v)
    print("==== heapsort ====")
    for i in xrange((len(v)-1), -1, -1):
        aux = v[i]
        v[i] = v[0]
        v[0] = aux
        print("ISOLA O MAIOR - ", v[i] )
        print("sift for - 0, ", i-1)
        sift_iterativo(0, i-1)
        print("HEAP MAX - ", v)

def max():
    if len(v) >= 0:
        return v[0]
    return -1 #erro não tratado


############################################################
######################  QuickSort  #########################
############################################################
def quicksort(min,max):
    print("====quicksort(",min, max,")")
    while min < max:
        print("====partition2(", min, max, ")")
        p = partition2(min,max)
        print("p-min < max-p = ", p-min, max-p, p-min < max-p)
        if (p-min < max-p):
            print("====quicksort 01(", min, p-1, ")")
            quicksort(min, p-1)
            min = p+1
        else:
            print("====quicksort 02(", p+1, max, ")")
            quicksort(p+1,max)
            max = p-1

def partition(left, right):
    pivot = v[left]
    l = left + 1
    r = right
    print("partition indices", pivot, l, r)
    while l < r:
        while l < right and v[l] < pivot:
            l+=1
            #print("left ", l)
        while r > left and v[r] >= pivot:
            r-=1
            #print("right ", r)
        if l < r:
            print("TORCAR : v[l] - ", v[l], "v[r] - ", v[r])
            aux = v[l]
            v[l] = v[r]
            v[r] = aux
    print("TORCAR PIVOT: v[left] - ", v[left], "v[r] - ", v[r], "pivot - ", pivot)
    v[left] = v[r]
    v[r] = pivot
    print("array", v)
    return r

def partition2(left, right):
    x = v[right]
    i = left - 1
    for j in xrange(left, right):
        if v[j] <= x:
            i += 1
            aux = v[i]
            v[i] = v[j]
            v[j] = aux
    aux = v[i+1]
    v[i+1] = v[right]
    v[right] = aux
    return i+1

############################################################
######################  MergeSort  #########################
############################################################

def mergesort(i, f):
    print("====MergeSort====")
    if i < f:
        m = int(floor((i+f)/2))
        print(i,f)
        print("====MergeSort01====")
        mergesort(i,m)
        merge(i, m, f)
        print("====merge01====")
        print("i,m,f", i, m, f)
        print("====MergeSort02====")
        mergesort(m+1, f)
        print("====merge02====")
        print("i,m,f", i,m,f)


def merge(i, m, f):
    i1 = i
    i2 = i
    i3 = m+1
    while i2 <= m and i3 <= f:
        if v[i2] < v[i3]:
            i1+= 1
            i2+= 1
            aux[i1] = v[i2]
        else:
            i1 += 1
            i3 += 1
            aux[i1] = v[i3]
    while i2 <= m:
        i1+=1
        i2+=1
        aux[i1] = v[i2]
    while i3 <= f:
        i1 += 1
        i3 += 1
        aux[i1] = v[i3]
    for j in xrange(i, f):
        v[j] = aux[j]

