# Write a function that takes in a string of one or more words, and returns the same string,
# but with all five or more letter words reversed.

def spin_words(sentence):
    sentence = sentence.split()
    for word in range(len(sentence)):
        if len(sentence[word]) >= 5:
            sentence[word] = sentence[word][::-1]
    return " ".join(sentence)

# tests:
print(spin_words('Welcome'))
print(spin_words('CodeWars'))
print(spin_words('Hey fellow warriors'))
print(spin_words('I love programming'))
print(spin_words('Smolensk'))