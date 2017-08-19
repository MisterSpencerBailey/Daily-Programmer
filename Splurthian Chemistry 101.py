element = str(input("Enter an element name: ")).lower()
symbol = str(input("Enter a symbol name: ")).lower()
highest = 0

while len(symbol) != 2:
    symbol = str(input("Enter a symbol name: ")).lower()   

def verify(element, symbol):

    for letter in range (len(element)): # Finds last occurence of last letter in symbol
        if element[letter] == symbol[1]:
            highest = letter

    if symbol[0] not in element or symbol[1] not in element: #Checks if symbol letters
        print("False1")                                      #are in the element
        return False


    if element.index(symbol[0]) > highest: #Checks to make sure symbol letters in correct order
        print("False2")                    #in compared to order in elements
        return False

    
    if symbol[0] == symbol[1] and element.count(symbol[0]) != 2: #Checks to make sure if symbol name 
        print("False3")                                          # is same letters, is used twice in element
        return False
                                        


verify(element, symbol)
