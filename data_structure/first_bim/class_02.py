__author__ = 'rene_esteves'


def factorial(input):
    if input < 1:  # base case
        return 1
    else:
        return input * factorial(input - 1)  # recursive call


def sum(input):
    if input == 1:  # base_case
        return 1
    else:
        return input + sum(input - 1)  # recursive call


def fibonacci(input):
    if input == 1 or input == 0:  # base_case
        print("PAROU")
        return 1
    else:
        return fibonacci(input - 1) + fibonacci(input - 2)  # recursive call


# ====
def cres_natural_order(input):
    if input == 0:  # base_case
        return print(input, "- ", end="")
    else:
        cres_natural_order(input - 1)  # recursive call
        return print(input, "- ", end="")


def descres_natural_order(input):
    if input == 0:  # base_case
        return print(input, end="")
    else:
        print(input, "- ", end="")
        return descres_natural_order(input - 1)  # recursive call


def array_max(array, position):
    if position >= 0:  # base case
        maior = int(array_max(array, position - 1))  # recursive call
        if position < len(array):  # vet size
            if (maior > array[position]):
                return maior
            else:
                return array[position]
        return maior  # final return
    else:
        return 0  # first valid return


def is_true(array, position, value):
    if len(array) > position:  # base_case
        if array[position] == value:
            return True
        else:
            return is_true(array, position + 1, value)  # recursive call
    else:
        return False


def seekvalue(array, position, value):
    if position >= 0:  # base case
        is_true = seekvalue(array, position - 1, value)  # recursive call
        if position < len(array) and is_true is not True:  # vet lenght and valid return
            if array[position] == value:
                return True
            else:
                return False
        return is_true  # final return
    else:
        return False  # first valid return


def binary_search(array, start, end, value):
    middle = int((start + end) / 2)
    if array[middle] == value:
        return True
    else:
        if start == end:
            return False
        else:
            if (value < array[middle]):
                return binary_search(array, start, middle - 1, value)
            else:
                return binary_search(array, middle + 1, end, value)


def sum_array(array, position):
    if len(array) == position:  # base_case
        return 0
    else:
        return array[position] + sum_array(array, position + 1)  # recursive call


def invt_array(array, position):  # TODO there's something wrong
    if len(array) - 1 == position:  # base_case
        return print(array[position])
    else:
        array[len(array) - position - 1] = invt_array(array, position + 1)  # recursive call
        return print(array[position])


# ====
def decimal_to_binary(input):
    if input <= 0:  # base case
        return str("")
    else:
        return decimal_to_binary(int(input / 2)) + str(input % 2)  # recursive call


def factoring(input):
    if input == 1:  # base case
        return 1
    else:
        return float(factoring(input - 1) + 1 / input)  # recursive call


def exp(base, expo):
    if expo == 0:  # base case
        return 1
    else:
        return exp(base, expo - 1) * base  # recursive call


def sumdig(input):
    if input < 0:
        return sumdig(- input)  # recursive call for negative numbers
    if input == 0:  # base case
        return 0
    else:
        return input % 10 + int(sumdig(input / 10))  # recursive call


def invdig(input, size):
    if input < 1:  # base case
        return 0
    else:
        return int(input % 10) * pow(10, size) + int(invdig(input / 10, size - 1))  # recursive call


def josephus(elements, interval):
    if elements == 1:
        return 1
    else:
        print(elements, interval)
        return (josephus(elements - 1, interval) + interval) % elements


def triangle(input):
    if input == 1:  # base case
        return 1
    else:
        return triangle(input - 1) + input  # recursive call


def quad(input):
    if input == 2:  # base case
        return 2
    else:
        return quad(input - 1) + (2 * input - 1)  # recursive call


def mdc(p, q):
    if q == 0:  # base case
        return p
    else:
        return mdc(q, p % q)  # recursive call


def seekvalue2(array, position, value):
    if position >= 0:  # base case
        if array[position] == value:
            return True
        else:
            return seekvalue2(array, position - 1, value)  # recursive call
    else:
        return False  # worst case


def buscabinaria(array, inicio, fim, valor):
    if inicio <= fim:
        meio = int((inicio + fim) / 2)
        if array[meio] == valor:
            return True
        else:
            if array[meio] > valor:
                return buscabinaria(array, inicio, meio - 1, valor)
            else:
                return buscabinaria(array, meio + 1, fim, valor)
    else:
        return False


def inverter(numero, expo):
    print("numero", numero)
    if numero == 0:
        return numero
    else:
        return (int(numero % 10) * pow(10, expo)) + inverter(int(numero / 10), expo - 1)


v = []


def inv_array(i, f):
    if i < f:
        aux = v[i]
        v[i] = v[f]
        v[f] = aux
        inv_array(i + 1, f - 1)
