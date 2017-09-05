#  Source: https://www.reddit.com/r/dailyprogrammer/comments/6ldv3m/20170705_challenge_322_intermediate_largest/
#  TODO: Get this to be more efficient. Times for >3 are abysmal. 


def find_max(n):
    #  This function is creating the largest possible number it can be by taking the length of digits of N and turning it into 9s.
    
    limit = ''
    for i in range(n):
        limit += '9'

    return int(limit) # Makes sure the limit is now an integer instead of a string

def is_palindrome(n):
    #  Checking if N is the same backwards by iterating backwards and verifying they're equals.
    
    n = str(n) # Method needs a str to modify N like an object rather than an int.

    if n == n[::-1]:
        return True

def largest_palindrome(limit):
    
    maximum = find_max(limit) #  
    minimum = 10**(limit-1) #  Taking 10^digit length of N - 1 to create 1x number, which will always be the lowest digit of N-digit length  

    largest = 0

    for n1 in range(maximum, minimum, -1):
        for n2 in range(maximum, minimum, -1):
            if is_palindrome(n1*n2) and n1*n2 >  largest:
                    largest = n1*n2
                
    return largest
