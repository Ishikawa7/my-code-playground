'''
COUNT PRIMES:
Write a function that returns the number of prime numbers that exist
up to and including a given number
By the usual definition of prime for integers, negative integers can not be prim
'''

def count_primes(num):
    if num < 2:
        return 0
    primes = [2]
    for n in range(2, num + 1):
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.append(n)
    # print(primes)
    return len(primes)
