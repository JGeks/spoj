# factorial = # of zeros at end
# 5! = 1
# 10! = 2
# 15! = 3
# 20! = 4
# 25! = 6
# 30! = 7
# 35! = 8
# 40! = 9
# 45! = 10
# 50! = 12
# etc

def zero_checker(prime_num):
    zeros = int(prime_num / 5)
    additional_zero = int(prime_num / 25)
    total_zeros = zeros + additional_zero
  
    return total_zeros

def main():
    num_tests = int(input())
    #print(f"Num tests:, {num_tests}")
    for x in range(num_tests):
        prime_num = int(input())
        print(zero_checker(prime_num))
        print("")


main()