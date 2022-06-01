# sentence to count the words
sentence = "Goal driven and dynamic professional, educated to degree standard in Biochemistry."

# The count words function decalration
def wordsCount(sentence):
    counter = 0;
    strList = sentence.split(" ")
    for character in strList:
        counter += 1
    print(counter)

# The count words function call
wordsCount(sentence)
