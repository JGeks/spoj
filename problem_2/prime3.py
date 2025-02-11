def sieve_prime_check(n):
    prime = [True for i in range(n+1)]
    prime[0] = prime[1] = False
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return prime
            
def main():
    num_tests = int(input())
    # make list of all prime numbers lower than 1 billion
    max = 10000000
    prime = sieve_prime_check(max)
    sieve_prime_check(max)
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