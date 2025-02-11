import math
prime = []
def segmentedSieve(n):
    
    # Compute all primes smaller than or equal 
    # to square root of n using simple sieve
    limit = int(math.floor(math.sqrt(n)) + 1)
    
    # Divide the range [0..n-1] in different segments 
    # We have chosen segment size as sqrt(n). 
    low = limit
    high = limit * 2
    
    # While all segments of range [0..n-1] are not processed, 
    # process one segment at a time 
    while low < n:
        if high >= n:
            high = n
            
        # To mark primes in current range. A value in mark[i] 
        # will finally be False if 'i-low' is Not a prime, 
        # else True. 
        mark = [True for i in range(limit + 1)]
        
        # Use the found primes by simpleSieve() 
        # to find primes in current range 
        for i in range(len(prime)):
            
            # Find the minimum number in [low..high] 
            # that is a multiple of prime[i] 
            # (divisible by prime[i]) 
            # For example, if low is 31 and prime[i] is 3, 
            # we start with 33. 
            loLim = int(math.floor(low / prime[i]) * 
                                         prime[i])
            if loLim < low:
                loLim += prime[i]
                
            # Mark multiples of prime[i] in [low..high]: 
            # We are marking j - low for j, i.e. each number 
            # in range [low, high] is mapped to [0, high-low] 
            # so if range is [50, 100] marking 50 corresponds 
            # to marking 0, marking 51 corresponds to 1 and 
            # so on. In this way we need to allocate space 
            # only for range 
            for j in range(loLim, high, prime[i]):
                mark[j - low] = False
        low = low + limit
        high = high + limit
    return prime

def main():
    num_tests = int(input())
    # make list of all prime numbers lower than 1 billion
    max = 1000000
    prime = segmentedSieve(max)
    #print(f"Num tests:, {num_tests}")
    for x in range(num_tests):
        number_range = (input())
        input_1, input_2 = map(int, number_range.split())
        for p in range(input_1, input_2+1):
            if prime[p]:
                print(p)
        print("")
#2, 1 10, 3 5 

main()