# Source: https://www.reddit.com/r/dailyprogrammer/comments/52enht/20160912_challenge_283_easy_anagram_detector/

def is_anagram(text1, text2):
    text1 = text1.replace(" ", "") #Removes all spaces
    text2 = text2.replace(" ", "")

    
    # Two sentences will always be an anagram if their sorted values are equals as they have the same values. 
    if sorted(text1) == sorted(text2):
        print(text2, "is an anagram of",text1)
        return True
    else:
        print("Is not an anagram")
        return False

is_anagram("Astronomers", "Moon starer")
