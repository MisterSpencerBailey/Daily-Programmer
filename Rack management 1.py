# Source: https://www.reddit.com/r/dailyprogrammer/comments/5go843/20161205_challenge_294_easy_rack_management_1/
# Doesn't fully work.

points =  { 'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1,
           't': 1, 'l': 1, 's': 1, 'u': 1, 'd': 2, 'g': 2,'b': 3, 'c': 3,
           'm': 3, 'p': 3, 'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4, 'k': 5,
           'j': 8, 'x': 8, 'q': 10, 'z': 10 }


def scrabble(word1,word2):
    for letter in word2:
        if word2.count(letter) > word1.count(letter): # The word can be made if there are enough letters in list of
            return False                              # letters. If true, then the word can be made out of the letters
    return True

def longest_word(letters): 
    list_of_words = open('enable1.txt').read().split()
    longest = ''
    for words in list_of_words:
        if scrabble(letters, words):
            if len(words) > len(longest):
                longest = words
    print(longest)

def scoring(word):
    score = 0
    for letter in word:
        score += points[letter]
    return score

def highest_score(letters):
    highest_word = ''
    list_of_words = open('enable1.txt').read().split()

    for words in list_of_words:
        if scrabble(letters, words):
            if scoring(words) > scoring(highest_word):
                print(scoring(words), words)
                highest_word = words
    print(highest_word, scoring(highest_word))



#scrabble("uruqrnytrois","squinty")
#longest_word("dcthoyueorza")
#print(scoring("squinty"))
highest_score("iogsvooely")
