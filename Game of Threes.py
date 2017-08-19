# Source: https://www.reddit.com/r/dailyprogrammer/comments/3r7wxz/20151102_challenge_239_easy_a_game_of_threes/

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
