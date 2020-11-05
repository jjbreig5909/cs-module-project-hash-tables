# Your code here
with open('applications/histo/robin.txt') as f:
    words = f.read()

words = words.lower()

word_array = words.split (' ')
print(word_array)