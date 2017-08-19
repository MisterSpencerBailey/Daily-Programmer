def is_anagram(text1, text2):
    text1 = text1.replace(" ", "") #Removes all spaces
    text2 = text2.replace(" ", "")

    if sorted(text1) == sorted(text2):
        print(text2, "is an anagram of",text1)
        return True
    else:
        print("Git gud")
        return False

is_anagram("Astronomers", "Moon starer")
