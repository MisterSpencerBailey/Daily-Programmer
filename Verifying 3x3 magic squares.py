def verify_3x3():
    inputs =[8, 1, 6,
             3, 5, 7,
             4, 9, 2]
    if inputs[4] + inputs[1] + inputs[7] == 15 and inputs[4]+inputs[3]+inputs[5] == 15 and inputs[0] + inputs[4] + inputs[8] == 15:
        print("This is a magic square.")
    else:
        print("This is not a magic square.")    
#verify_3x3()


def verify_any():
    inputs =[8, 1, 6,3, 5, 7,4, 9, 2]
    width = len(inputs) **0.5                   # Finds width/height of the list by finding square root.
    height = width
    width_number = int(width)
    height_number = int(height)
    total = 0
    central_number = (len(inputs)+1)/2
    magic_number = central_number*len(inputs)


    for i in range (len(inputs)):
        total += inputs[i]
        print (total)
        


verify_any()
    
    
