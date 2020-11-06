# Your code here
with open('applications/histo/robin.txt') as f:
    words = f.read()

word_cache = {}
words = words.lower()
exclude = set('" : ; , . - + = / \ | [ ] { } ( ) * ^ &')
word_array = words.split (' ')
print(word_array)

for word in word_array:
    if word not in exclude:

        if word in word_cache:
            word_cache[word] += "#"
        
        if word not in word_cache:
            word_cache[word] = "#"
       

sorted_words = sorted(word_cache.items(), key=lambda x: x[1], reverse=True)

print(sorted_words)