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
    


print(len(words))
print(words[0])
print(words[len(words)-1])
print(word_storage)




# TODO: construct 5 random sentences
# Your code here

