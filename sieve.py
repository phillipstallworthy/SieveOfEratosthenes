# A Sieve of Eratosthenes
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

import math


def sieve(max_prime):

    prime_or_not = list(())
    not_prime = 0
    prime = 1

    integer_counter = 0
    while integer_counter <= max_prime :
        prime_or_not.append(prime) 
        integer_counter += 1

    prime_or_not[0]=not_prime
    prime_or_not[1]=not_prime

    integer_counter = 1
    while integer_counter <= math.ceil(max_prime / 2): 

        # the next "prime" is definitly prime, because all multiples of the current prime have been marked not prime.
        integer_counter = prime_or_not.index(1, integer_counter + 1)

        # all multiples the current prime, are not prime.
        y = integer_counter + integer_counter
        while y <= max_prime:
            prime_or_not[y] = not_prime
            y += integer_counter

    return_me = ""
    for index, prime in enumerate(prime_or_not):
        if prime != 0:
            return_me += (str(index))
            return_me += (" ")
    return return_me



