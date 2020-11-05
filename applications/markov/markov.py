import random

# Read in all the words in one go
with open("applications\markov\input.txt") as f:
    words = f.read()
   

# TODO: analyze which words can follow other words
# Your code here

words = words.split()
start_words = []
stop_words = []
word_storage = {}

#Generating start and stop word list:
for i in range(len(words)-1):
    if words[i].istitle():
        start_words.append(words[i])
    if words[i].endswith(".") or words[i].endswith("!") or words[i].endswith("?") or words[i].endswith('."') or words[i].endswith('!"') or words[i].endswith('?"'):
        stop_words.append(words[i])
    if words[i] in word_storage:
        word_storage[words[i]].append(words[i+1])
    if words[i] not in word_storage:
        word_storage[words[i]] = [words[i+1]]

def findNextWord(sentence, word):
    if word in stop_words:
        return sentence
    next_word = random.choice(word_storage[word])
    sentence += " " + next_word
    return findNextWord(sentence, next_word)

def newSentence():
    new_sentence = ''
    new_sentence += random.choice(start_words)
    result = findNextWord(new_sentence, new_sentence)
    print(result)
    




# TODO: construct 5 random sentences
# Your code here
newSentence()
newSentence()
newSentence()
newSentence()
newSentence()
