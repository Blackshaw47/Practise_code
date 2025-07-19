sentence = "I code because I love solving111 problems"
 
words = sentence.split()

longest = ""

for word in words:
    if len(word)> len(longest):
        longest = word

print(longest)
