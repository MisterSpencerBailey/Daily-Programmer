# Source: https://www.reddit.com/r/dailyprogrammer/comments/341c03/20150427_challenge_212_easy_r%C3%B6varspr%C3%A5ket/?ref=search_posts
# Doesn't work.

def encode():
    vowels = ["a", "e", "i", "o", "u", " "]
    i = 0
    new_phrase = str("")

    phrase = str(input("Enter your sentence: "))


    
    for i in range(len(phrase)):
        if phrase[i] in vowels:
            new_phrase += phrase[i]
        else:
            new_phrase += phrase[i] + "o" + phrase[i].lower()
            
        i += 1

    print(new_phrase)

#encode()

def decode():

    vowels = ["a", "e", "i", "o", "u", " "]
    i = 0
    new_phrase = str("")

    phrase = str(input("Enter your sentence: "))
    
    for i in range(len(phrase)):
        if phrase[i] not in vowels and phrase[i+2] == phrase[i]:
            new_phrase += phrase[i]
            i += 2
        else:
            new_phrase += phrase[i]
            i += 1
            
    print(new_phrase)
decode()
