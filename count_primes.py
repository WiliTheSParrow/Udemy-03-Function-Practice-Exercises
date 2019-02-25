# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25
# By convention, 0 and 1 are not prime.


def count_primes(num):
    numprime = []

    for primeornot in range(2, num + 1):
        isitaprime = True
        for n in range(2, primeornot):
            if primeornot % n == 0:
                isitaprime = False
                break
        if isitaprime:
            numprime.append(primeornot)

    return len(numprime)

# Check
count_primes(100)