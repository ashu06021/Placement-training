# Question:
# Count the frequency of each word in a sentence.
#
# Topic:
# Dictionary, String, Loop

sentence = input("Enter a sentence: ")

words = sentence.split()

frequency = {}

for word in words:

    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequency:")

for word in frequency:
    print(word, ":", frequency[word])