# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
import string
#Notes: 
#I can use replace
cipher_key = {}
final_text = []
letter_cache = {}
frequent_letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
alphabet=[]
for i in range(65,91):
    alphabet.append(chr(i))

with open('applications/crack_caesar/ciphertext.txt') as f:
    ciphertext = f.read()

def find_cipher_frequency(cipher):
    for letter in alphabet:
        letter_cache[letter] = cipher.count(letter)

find_cipher_frequency(ciphertext)
sorted_letters = sorted(letter_cache.items(), key=lambda x: x[1], reverse=True)

for i in range(len(frequent_letters)-1):
    cipher_key[frequent_letters[i]] =  sorted_letters[i][0]

all_letters = [char for char in ciphertext]

new_key = dict([(value, key) for key, value in cipher_key.items()]) 

for letter in all_letters:
    if letter in new_key:
        letter = new_key[letter]
    final_text.append(letter)

result = ''.join(final_text)

print(result)






