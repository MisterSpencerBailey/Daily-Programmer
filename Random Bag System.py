import random

pieces = ["O", "I", "S", "Z", "L", "J", "T"]
string = ""

for i in range(len(pieces)):
    string += random.shuffle(pieces)
    i += 1

print(string)
