krepkar_numbers = []
def check_krepkar(n):
    squared = str(n**2) #Is a str to be able to check length easier
    first_half = squared[0:int(len(squared)/2)] #Splits N^2 to be added up to check if they == N
    second_half = squared[int(len(squared)/2):len(squared)]
    #print (n, first_half, second_half)
    if len(squared) <= 2: #Skips smaller numbers since they can't be a krepkar numbers.
        return False
    if int(first_half) + int(second_half) == n:
        return True
def check_in_range(start,end):
    for number in range(start,end):
        if check_krepkar(number) is True:
            krepkar_numbers.append(number)

    print(krepkar_numbers)

#check_in_range(1,1000000)


