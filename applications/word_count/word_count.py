import string
def word_count(s):
    # Your code here
    word_cache = {}
    s = s.lower()
    exclude = set('":;,.-+=/\|[]{}()*^&')
    s = ''.join(ch for ch in s if ch not in exclude)
    new_string = ''
    

    if s == '':
        return {}

    for letter in s:
        if letter in exclude:
            pass
        else:
            new_string = new_string + letter
    
    if new_string == '':
        return {}

    string_array = new_string.split()

    for word in string_array:
        if word in word_cache:
            word_cache[word] += 1
        else:
            word_cache[word] = 1

    print(word_cache)
    return word_cache




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))