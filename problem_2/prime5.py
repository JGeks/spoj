import math

def simpleSieve(limit):
    primes = []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    
    for p in range(2, limit + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
    return primes

def segmentedSieve(n):
    limit = int(math.floor(math.sqrt(n)))  # Find primes up to sqrt(n)
    
    # Get all primes less than or equal to sqrt(n)
    primes = simpleSieve(limit)
    
    low = limit
    high = 2 * limit
    
    while low < n:
        if high >= n:
            high = n
        
        # Mark all numbers in the range [low, high] as prime initially
        mark = [True] * (high - low)
        
        # Use the primes found so far to mark multiples in the range [low, high]
        for p in primes:
            # Find the first multiple of 'p' in the range [low..high]
            loLim = max(p * p, (low + p - 1) // p * p)
            
            for j in range(loLim, high, p):
                mark[j - low] = False
        
        # Collect primes from the range [low, high]
        for i in range(low, high):
            if mark[i - low]:
                primes.append(i)
        
        # Move to the next segment
        low = high
        high = high + limit
    
    return primes

def main():
    num_tests = int(input())
    max_val = 1000000000  # We want to sieve primes up to this limit
    primes = segmentedSieve(max_val)
    
    for _ in range(num_tests):
        input_range = input().split()
        input_1, input_2 = map(int, input_range)
        
        # Print all primes in the given range
        for p in primes:
            if input_1 <= p <= input_2:
                print(p)
        print("")  # Blank line between results

main()
