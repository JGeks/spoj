def sieve_prime_check(input1, input2):
    prime = [True for i in range(input2+1)]
    p = 2
    while (p * p <= input2):
        
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, input2+1, p):
                prime[i] = False
        p += 1
    for p in range(input1, input2+1):
        if prime[p]:
            print(p)
            
def main():
    num_tests = int(input())
    #print(f"Num tests:, {num_tests}")
    for x in range(num_tests):
        number_range = (input())
        min_num, max_num = map(int, number_range.split())
        if min_num <= 2:
            min_num = 3
        sieve_prime_check(min_num, max_num)
        print("")
#2, 1 10, 3 5 

main()