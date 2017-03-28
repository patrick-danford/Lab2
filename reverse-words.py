"""
Lab 2 assignment
Patrick Danford

This script will input a string of words, then print
the words in the string back in reverse order


"""
# basic code attempt:

# sentence = raw_input("Enter a sentence: ")
# separated = sentence.split()
# backwards = separated[::-1]
# result = " ".join(backwards)

# print result


# function attempt:

def reverse_words(sentence):
    separated = sentence.split()
    backwards = separated[::-1]
    return " ".join(backwards)

test1 = "hello there patrick"
assert (reverse_words(test1) == "patrick there hello")

test2 = ""
assert (reverse_words(test2) == "")

test3 = "1"
assert (reverse_words(test3) == "1")

print reverse_words(raw_input("Enter a sentence: "))

