
points =  { 'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1,
           't': 1, 'l': 1, 's': 1, 'u': 1, 'd': 2, 'g': 2,'b': 3, 'c': 3,
           'm': 3, 'p': 3, 'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4, 'k': 5,
           'j': 8, 'x': 8, 'q': 10, 'z': 10 }

def scrabble(word1,word2):
    for letter in word2:
        if word2.count(letter) > word1.count(letter): #The word can be made if there are enough letters in list of
            return False                              #letters. If true, then the word can be made out of the letters
    return True

def score(word):
    score = 0
    for i in range(len(word)):
        score += points[word[i]]*(i+1)
    return score

def efficient_testing():
    list_of_words = open('enable1.txt').read().split()
    previous_word = list_of_words[0]
    number = len(list_of_words)
    #Words >10 characters aren't possible for this challenge, so they're removed.
    for word in list_of_words:
        if len(word) > 10:
            list_of_words.remove(word)
    for words in list_of_words:
        if previous_word in words and score(words) > score(previous_word):
            list_of_words.remove(previous_word)
        previous_word = words
    return list_of_words

def highest_score(letters):
    high_score = 0
    word_list = open('enable1.txt').read().split()
    high_score_word = ''
    for words in word_list:
        if scrabble(letters,words) and score(words) > high_score:
            high_score = score(words)
            high_score_word  = words
    print(high_score_word, high_score)




#place_scoring("daily")
#efficient_testing()
highest_score("vepredequi")
