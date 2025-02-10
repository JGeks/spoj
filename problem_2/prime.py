def prime_check(i):
    if i > 1:
    # Iterate from 2 to n // 2
        for p in range(2, int(i//2)+1):  
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
            if i % p == 0:
                return False
        else:
            return True
    else:
        return False

            
def main():
    num_tests = int(input())
    #print(f"Num tests:, {num_tests}")
    for x in range(num_tests):
        number_range = (input())
        input_1, input_2 = map(int, number_range.split())
        for i in range(input_1 , input_2 + 1):
            if prime_check(i):
                print(i)
        print("")
#2, 1 10, 3 5 

main()