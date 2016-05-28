from pip._vendor.requests.packages.urllib3.connectionpool import xrange

__author__ = 'rene_'

######################
##### chapter 7 ######
######################

def convert_string(string):
    array = [None] * len(string)
    i=0
    for char in string:
        array[i] = char
        i+=1
    return array

def brute_force(text, word):
    comp = 0
    for i in range(len(text)-len(word)):
        j = 0
        if text[i + j] != word[j]: comp += 1
        while j<len(word) and text[i+j] == word[j]:
            comp+=1
            j+=1
        if j==len(word):
            print("Word found at i: ", i, " - comp = ", comp)
            # return i-j
            return comp

    print("Word not found - comp = ", comp)
    return comp

def automata():#TODO
    return ""

def kmp(text, word):
    comp=0
    failure = failure_function(word)
    print('failure_function = ',failure)
    i = 0
    j = 0
    while i < len(text):
        comp+=1
        if text[i] == word[j]:
            if j == len(word)-1:
                print("Word found at i-j: ", i-j, " - comp = ", comp)
                #return i-j
                return comp
            else:
                i+=1
                j+=1
        else:
            if j != 0:
                j = failure[j-1]
            else:
                i+=1
    print("Word not found - comp = ", comp)
    return comp

def failure_function(word):
    if len(word) > 0:
        failure = [None]*len(word)
        failure[0] = 0
        j = 0
        i = 1
        while i < len(word):
            if word[i] == word[j]:
                j += 1
                failure[i] = j
                i += 1
            else:
                if j == 0:
                    failure[i] = 0
                    i += 1
                else:
                    j = failure[j-1]
        return failure
    else:
        return -1

def bm(text, word): #
    m = len(word)
    n = len(text)
    if m > n: return -1
    skip = []
    for k in range(256): skip.append(m)
    for k in range(m - 1): skip[ord(word[k])] = m - k - 1
    skip = tuple(skip)
    k = m - 1
    comp = 0
    while k < n:
        j = m - 1;
        i = k
        #print("FORA", text[i], " - ", word[j], " - ", i)
        if text[i] != word[j]: comp +=1
        while j >= 0 and text[i] == word[j]:
            #print("DENTRO", text[i], " - ", word[j], " - ", i)
            comp += 1
            j -= 1;
            i -= 1
            if text[i] != word[j]: comp += 1
        if j == -1:
            print("Word found at i+1: ", i+1, " - comp = ", comp)
            #return i + 1
            return comp
        #print("FORA 2", text[i], " - ", word[j], " - ", i)
        k += skip[ord(text[k])]

    print("Word not found - comp = ", comp)
    return comp

# Following program is the python implementation of
# Rabin Karp Algorithm given in CLRS book

# d is the number of characters in input alphabet
d = 256

# pat  -> pattern
# txt  -> text
# q    -> A prime number

def kr(text, word, q):
    M = len(word)
    N = len(text)
    i = 0
    j = 0
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    h = 1

    # The value of h would be "pow(d, M-1)%q"
    for i in xrange(M - 1):
        h = (h * d) % q

    # Calculate the hash value of pattern and first window
    # of text
    for i in xrange(M):
        p = (d * p + ord(word[i])) % q
        t = (d * t + ord(text[i])) % q

    # Slide the pattern over text one by one
    for i in xrange(N - M + 1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if p == t:
            # Check for characters one by one
            for j in xrange(M):
                if text[i + j] != word[j]:
                    break

            j += 1
            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j == M:
                print("Pattern found at index " + str(i))

        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N - M:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % q

            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t + q


    # This code is contributed by Bhavya Jain