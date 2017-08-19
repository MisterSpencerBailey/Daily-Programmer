# Source: https://www.reddit.com/r/dailyprogrammer/comments/3ofsyb/20151012_challenge_236_easy_random_bag_system/
# Doesn't work.

import random

pieces = ["O", "I", "S", "Z", "L", "J", "T"]
output = ""

for i in range(len(pieces)):
    output += random.shuffle(pieces)
    i += 1

print(output)
