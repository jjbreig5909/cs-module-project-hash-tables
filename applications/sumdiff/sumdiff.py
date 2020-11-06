"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))

q = (1, 3, 4, 7, 12)
results = []

def f(x):
    return x * 4 + 6

# Your code here
import itertools
answers = []

for num in q:
    answers.append(f(num))

arr1 = [1, 3, 4, 7, 12]
arr2 = []

potential_combinations = itertools.product(q, repeat=4)

def find_combos(combos):
    for item in combos:
       if item[0]+item[1] == item[2]-item[3]:
           results.append([item[0], item[1], item[2],item[3]])

find_combos(potential_combinations)
print(results)

