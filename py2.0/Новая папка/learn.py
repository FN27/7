import collections
letter_list = list("sample text")
x = ['rot', 'morty', 'rot', 'prikol']
letter_cnt = collections.Counter({x})
print(letter_cnt.elements())