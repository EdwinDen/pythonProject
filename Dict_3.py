# Exercise 6
student = dict(John=85, Emma=92, Sophia=78)

average = sum(student.values()) / len(student)

print(f"The Average is {average}")

# Exercise 7
def wordFrequencyCounter(sentence):
    words = sentence.split()
    text = ""
    word_frequency = {}

    for word in words:
        word = word.strip(".,?!").lower()
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    return word_frequency

sentence = "This is a test. This is just a Test"
print(wordFrequencyCounter(sentence))

# Exercise 8

dict1 = dict(a=1, b=4)
dict2 = dict(b=3, c=4)

merge_dict = {**dict1, **dict2}

print(merge_dict)
