def word_count(s):
    # Your code here
    word_cache = {}
    string_array = s.split(' ')
    unique_words = []
    if s == '':
        return {}

    for word in string_array:
        if word not in unique_words: 
            unique_words.append(word)
    
    for word in unique_words:
        word_cache[word] = 0

    for word in string_array:
        word_cache[word] +=1
    print(word_cache)
    return word_cache




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))