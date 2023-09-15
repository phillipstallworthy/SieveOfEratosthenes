# A Sieve of Eratosthenes

limit = 42 # CS data structures start at zero...(numbers are 0 -> limit-1)
print (limit)

data = list(()) 

i = 1
while i <= limit:
    data.append('u')
    i += 1

x = 1
while x <= limit / 2:

    # the next unknown x is prime. This is the nature of the sieve.
    x = data.index('u', x+1)
    data[x]=1

    # all multiples of x are not prime, obviously
    y = x + x
    while y < limit:
        data[y] = 0
        y += x

count = 0
for num in data:
    if num != 0:
        print(count)
    count += 1