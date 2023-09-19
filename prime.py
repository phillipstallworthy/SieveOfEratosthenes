import argparse
from sieve import sieve

parser = argparse.ArgumentParser(description='Generate a list of primes')
parser.add_argument('limit', type=int, help='Test every integer for primeness upto this limit')
args = parser.parse_args()
if args.limit > 1024: parser.error("limit cannot be larger than 1024")

max_prime = args.limit

print (sieve(max_prime))