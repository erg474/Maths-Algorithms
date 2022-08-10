import time
import math

def PrimeCheck1(n):
    #standard loop
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True


def PrimeCheck2(n):
    #loop up to sqrt
    #loop only checks up to sqrt(n), factors are mirrored after sqrt(n)
    if n<=1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def PrimeCheck3(n):
    #loop up to sqrt excluding evens
    if n<=1:
        return False
    if n==2:
        return True
    if n > 2 and n % 2 ==0:  #2 not in loop anymore so check for multiples of 2
        return False
    for i in range(3, math.floor(math.sqrt(n))+1, 2):
        if n%i==0:
            return False
    return True

def SieveOfEratosthenes(n):
    #SieveOfEratosthenes Prime Checking Method

    #Create a Boolean Array "prime[0..n]" and initialise all entries as true.
    #A value in prime[i] will finally be false if i is not a prime, else true.

    prime = [True for i in range(n+1)]

    p = 2
    while(p * p <= n):
        #If prime[p] is not changed, then it is a prime
        if (prime[p]==True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p+=1
    c=0

    #Print all the prime numbers
    for p in range(2,n):
        if prime[p]:
            c += 1
    return c


def SieveOfAtkin(limit):
    # 2 and 3 are known
    # to be prime
    if limit > 2:
        print(2, end=" ")
    if limit > 3:
        print(3, end=" ")

    # Initialise the sieve
    # array with False values
    sieve = [False] * (limit + 1)
    for i in range(0, limit + 1):
        sieve[i] = False

    '''Mark sieve[n] is True if
    one of the following is True:
    a) n = (4*x*x)+(y*y) has odd
    number of solutions, i.e.,
    there exist odd number of
    distinct pairs (x, y) that
    satisfy the equation and
    n % 12 = 1 or n % 12 = 5.
    b) n = (3*x*x)+(y*y) has
    odd number of solutions
    and n % 12 = 7
    c) n = (3*x*x)-(y*y) has
    odd number of solutions,
    x > y and n % 12 = 11 '''
    x = 1
    while x * x <= limit:
        y = 1
        while y * y <= limit:

            # Main part of
            # Sieve of Atkin
            n = (4 * x * x) + (y * y)
            if (n <= limit and (n % 12 == 1 or
                                n % 12 == 5)):
                sieve[n] ^= True

            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                sieve[n] ^= True

            n = (3 * x * x) - (y * y)
            if (x > y and n <= limit and
                    n % 12 == 11):
                sieve[n] ^= True
            y += 1
        x += 1

    # Mark all multiples of
    # squares as non-prime
    r = 5
    while r * r <= limit:
        if sieve[r]:
            for i in range(r * r, limit + 1, r * r):
                sieve[i] = False

        r += 1

        # Print primes
    # using sieve[]
    for a in range(5, limit + 1):
        if sieve[a]:
            print(a, end=" ")

# Driver Code
#limit = 100000
#SieveOfAtkin(limit)

# This code is contributed
# by Smitha

#def SieveOfAtkin(n):



t0 = time.time()
c = 0
primes=[]

'''
for n in range(1,100000):
    x=PrimeCheck2(n)
    c+=x
    if x==True:
        primes.append(n)

print(primes, "\nNo. of Primes in range:", len(primes))
print("Total prime numbers in range : ", c)

t1=time.time()
print("Time taken : ", t1-t0)
print("End")

for prime in primes:
    if prime<10:

        print(primes[:primes.index(prime)])
        print(sum(primes[:primes.index(prime)]))
'''

t0_2 = time.time()
sieve = SieveOfEratosthenes(10000000)
print("Total prime numbers in range:", sieve)

t1_2 = time.time()
print("Time Required:", t1_2 - t0_2)

#for more methods, look here:
#https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
#https://www.reddit.com/r/learnprogramming/comments/1eqnx5/faster_way_to_find_primes/