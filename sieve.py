# A Sieve of Eratosthenes
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

#import argparse
#parser = argparse.ArgumentParser(description='Generate a list of primes')
#parser.add_argument('limit', type=int, help='Test every integer for primeness upto this limit')
#args = parser.parse_args()
#if args.limit > 1024: parser.error("limit cannot be larger than 1024")

#max_prime = args.limit



def sieve(max_prime):

    prime_or_not = list(()) 

    integer_counter = 1
    while integer_counter <= max_prime:
        prime_or_not.append('unknown')
        integer_counter += 1
    prime_or_not[0]=0
    prime_or_not[1]=0

    integer_counter = 1
    while integer_counter <= max_prime / 2: #we may have an issue here. odd max_prime goes long.

        # the next integer is prime, because all multiples of the previous integer have been marked not prime.
        integer_counter = prime_or_not.index('unknown', integer_counter+1)
        prime_or_not[integer_counter]=1 #does 1 mean prime. 

        # all multiples of integer_counter are not prime, obviously
        y = integer_counter + integer_counter
        while y < max_prime:
            prime_or_not[y] = 0
            y += integer_counter

    count = 0
    returnme = ""
    for num in prime_or_not:
        if num != 0:
            #print(count,'', end='')
            returnme += (str(count))
            returnme += (" ")
        count += 1
    
    return returnme


#print (sieve(max_prime))
