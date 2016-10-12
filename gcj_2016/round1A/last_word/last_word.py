import os
import numpy

folder = 'round1A'
path = os.path.join(os.getcwd(),folder + '\\' +'last_word')
name = 'A-large-practice'
input_name = name + '.in'
input_path = os.path.join(path,input_name)

with open(input_path, mode='r') as f:
        n_lines = int(f.readline().split()[0])
        words = []
        for i in range(n_lines):
            words.append(f.readline().split()[0])


result = list()

last_word = []
for w in  words:
    for letter in w:
        if len(last_word)==0:
            last_word.append(letter)
        else:
            if (letter >= last_word[0]):
                last_word = [letter] + last_word
            else:
                last_word.append(letter)
    result.append(''.join(last_word))
    last_word = []

output_name = name + '.out'
output_path = os.path.join(path,output_name)
with open(output_path, mode='w') as f:
    for i,j in enumerate(result):
        f.write('Case #{}: {}\n'.format(i+1,j))