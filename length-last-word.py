"""
Lab 2 assignment - Length of last word
Patrick Danford

This script will input a string of words, then return
the length of the last word in the string


"""

def length_of_last_word(sentence):
    string_list = sentence.split(" ")
    last_word = string_list [-1]
    return len(last_word)

test1 = ""
assert (length_of_last_word(test1) == 0)

test2 = "Hello, can you hear me"
assert (length_of_last_word(test2) == 2)

print length_of_last_word(raw_input("Enter a sentence: "))