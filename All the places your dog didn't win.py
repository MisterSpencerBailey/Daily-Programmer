place = str(input("What place did your dog get: "))
while not place.isdigit():
    place = input("Not a valid input, try again: ")
    break

total = str(input("How many dogs competed: "))
while not total.isdigit():
    total = input("Not a valid input, try again: ")

def less_100(total, place):
    i = 1
    total = int(total)

    for i in range(total):
        lastdigit = int(repr(i)[-1])
        place = int(place)
        if i != place:
            if i % 10 == 1:
                print(str(i)+"st")
            elif i % 10 >= 4 or i == 12:
                print (str(i)+"th")
            elif lastdigit == 2:
                print(str(i)+"nd")
            elif i % 10 == 3 and i < 10:
                print (str(i)+"rd")
            elif i % 10 == 3 and i > 15:
                print (str(i)+"rd")     
        i += 1

def more_100(total, place):
    i = 1
    total = int(total)

    for i in range(total):
        lastdigit = int(repr(i)[-1])
        place = int(place)
        if i != place:
            if i % 10 == 1:
                if i % 100 == 11:
                    print(str(i)+"th")
                else:
                    print(str(i)+"st")
            elif i % 10 >= 4 or i % 100 == 12:
                print (str(i)+"th")
            elif lastdigit == 2:
                print(str(i)+"nd")
            elif i % 10 == 3 and i % 100 > 10:
                print (str(i)+"rd")
            elif i % 100 == 3 and i > 15:
                print (str(i)+"rd")     
        i += 1

if int(total) <= 100:
    less_100(total, place)
else:
    more_100(total, place)
