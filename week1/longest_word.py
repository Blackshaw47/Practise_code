sentence = "I code because I love solving111 problems"




def longest_word(sentence):
    words = sentence.split()

    longest = ""

    for word in words:
        if len(word)> len(longest):
            longest = word

    return longest

long_word = longest_word(sentence)
print(long_word)
