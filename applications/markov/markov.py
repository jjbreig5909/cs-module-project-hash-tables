import random

# Read in all the words in one go
with open("applications\markov\input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
words = words.split()

class Markov(object):
    def __init__(self):
        self.word_size = len(words)
        self.cache = {}
        self.database()

    def triples(self):

        if len(words) < 3:
            return
        
        for i in range(len(words) - 2):

            #Yield is like "return", but returns a generator function
            yield (words[i], words[i+1], words[i+2])

    def database(self):
        for word1, word2, word3 in self.triples():
            key = (word1, word2)
            if key in self.cache:
                self.cache[key].append(word3)
            else:
                self.cache[key] = [word3]

    def new_sentence(self, size = 25):
        print(self.word_size)
        seed = random.randint(0, self.word_size-3)
        seed_word, next_word = words[seed], words[seed+1]
        word1, word2 = seed_word, next_word
        gen_words = []
        for i in xrange(size):
            gen_words.append(word1)
            word1, word2 = word2, random.choice(self.cache[(word1, word2)])
            gen_words.append(word2)
            return ' '.join(gen_words)

# TODO: construct 5 random sentences
# Your code here
print(Markov.new_sentence(30))
