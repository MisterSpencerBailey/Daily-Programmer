InputNumber = int(input("Please enter an integer: "))

while InputNumber > 1:
    if InputNumber % 3 == 0:
        InputNumber = InputNumber/3
        print (InputNumber)
    elif (InputNumber + 1) % 3 == 0:
        InputNumber = (InputNumber+1)/3
        print (InputNumber)
    else:
        InputNumber =(InputNumber-1) / 3
        print (InputNumber)
