import sys

#Generate a list that holds all prime numbers from 0-100


def isPrime(k):
    isPrimeNumber = False
    
    if (k > 9 and (k%2) != 0):
        if (((k%3) != 0) and ((k%5) != 0) and ((k%7) != 0)):
            isPrimeNumber=True

    if (k < 9 and (k%2) != 0):
        isPrimeNumber=True

    # Deal with special primes
    if (k == 1): isPrimeNumber = False
    if (k == 2): isPrimeNumber = True

    return isPrimeNumber

primeNums = list()

for i in range(101):
    if isPrime(i):#No == True is needed, as this is boolean.
        primeNums.append(i)


    
print('There are ',len(primeNums), ' prime numbers between 0 to 100\n')
print('The List of all prime numbers from 0-100:\n',primeNums)
