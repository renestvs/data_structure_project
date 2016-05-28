__author__ = 'rene_'


####################################################
##############   joshepus recursivo ################
####################################################

##Recorencias
# J(1) = 1
# J(2n) = 2J(n-1) - 1
# J(2n +1) = 2J(n) + 1

def joshepus (n):
    if n <= 1:
        return 1
    else:
        if n%2 == 0:
            return (2*joshepus(n/2)-1)
        else:
            return (2*joshepus((n-1)/2)+1)

    def joshepus2 (n, m):
        if n == 1:
            return 0
        return (m + joshepus2(n-1,m)) % n

