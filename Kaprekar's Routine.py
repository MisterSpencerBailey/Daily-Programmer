# Source: https://www.reddit.com/r/dailyprogrammer/comments/56tbds/20161010_challenge_287_easy_kaprekars_routine/


def largest_digit(n):
    largest =sorted(str(n), reverse=True)[0] #Sorts it largest -> smallest and takes first digit
    return largest
def descending_order(n):
    descending = sorted(str(n))
    num = int(''.join(map(str,descending))) #Turns the sorted list into a single int
    return num
def ascending_order(n):
    descending = sorted(str(n), reverse=True)
    num = int(''.join(map(str,descending))) #Turns the reverse sorted list into a single int
    return num
def Kaprekar(n1):
    count = 0
    while n1 != 6174:
        count += 1
        n2 = ascending_order(n1)-descending_order(n1)
        n1 = n2
    return count
