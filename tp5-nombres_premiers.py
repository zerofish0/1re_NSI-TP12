#####################################
### TP 5 : Les fonctions (encore) ###
#####################################

### II) Nombres premiers ###
#Question 1
def canDivide(n : int,d : int) -> bool :
    """Savoir si n est divible par d
    params : n ; d
    return bool
    """
    return n % d == 0

#Question 2
def getDiviser(n : int) -> list :
    """Renvoie la liste des diviseurs de n
    params : n
    return : list
    """
    return [i for i in range(1,int(n/2+1))  if canDivide(n,i)] + [n]


#Question 3
def isPrime(n : int) -> bool :
    """Savoir si n est premier
    params : n
    return : bool
    """
    return len(getDiviser(n))==2

#Question 4
def factor(n : int) -> list:
    """Renvoie la decomposition en produits de facteurs premiers de n
    params : n
    return : list [(n1,pow1),(n2,pow2) ...]
    """
    #1) on recupere tous les facteurs premiers
    rawfactors = list()
    i = 2
    while n > 2 :
        while n % i == 0 :
            rawfactors.append(i)
            n //= i
        i += 1
    #2) on crée une liste de tuple contenant le facteur et sa puissance
    rawset = set(rawfactors)
    factors = list()
    for n in rawset :
        factors.append((n,rawfactors.count(n)))
    return factors


#Bonus : reduction d'une fraction, implementation du lcm
def gcd(n1 : int, n2 : int) -> int:
    """Renvoie le plus grand diviseur commun de  n1 et n2
    params : n1 ; n2
    return : int
    """
    while n2 :
        n1, n2 = n2, n1 % n2
    return abs(n1)

def irreductible(num : int,den : int) -> tuple :
    """Renvoie une fraction (num/den) sous forme irredcutible
    params : num , den
    return : tuple
    """
    irreductible_num = num // gcd(num,den)
    irreductible_den = den // gcd(num,den)
    return (irreductible_num,irreductible_den)

def lcm(x : int,y : int) -> int:
    """Renvoyer le plus petit multiple commun entre x et y
    params : x ; y
    return : int
    """
    return y * (x//gcd(x,y))























