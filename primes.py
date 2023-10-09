"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes < 1:
        raise ValueError(number_of_primes)
    
    currentNumber = 2
    while number_of_primes > 0:
        if isPrime(currentNumber):
            list.append(currentNumber)
            number_of_primes = number_of_primes - 1
        currentNumber = currentNumber + 1
    return list

def isPrime(number):
    factors = 0
    for i in range(2, number):
        if number % i == 0:
            factors = factors + 1
    return factors == 0
    