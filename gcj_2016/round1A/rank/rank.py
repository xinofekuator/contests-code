import os
import numpy

folder = 'round1A'
path = os.path.join(os.getcwd(),folder + '\\' +'rank')
name = 'B-large-practice'
input_name = name + '.in'
input_path = os.path.join(path,input_name)

with open(input_path, mode='r') as f:
        n_lines = int(f.readline().split()[0])
        matrix_list = list()
        for i in range(n_lines):
            size = int(f.readline().split()[0])
            matrix = list()
            for j in range(2*size-1):
                line = [int(x) for x in f.readline().split()]
                matrix.append(line)
            matrix_list.append(matrix)
            matrix = []

result = list()

for i in matrix_list:
    count = dict()
    for j in i:
        for k in j:
            if k in count.keys():
                count[k] = count[k] + 1
            else:
                count[k] = 1
    aux_result = []
    for key,value in count.items():
        if value%2 != 0:
            aux_result.append(key)
    result.append(sorted(aux_result))

def print_list(list):
    result = ''
    for i in list:
        result = result + ' ' + str(i)
    return result

output_name = name + '.out'
output_path = os.path.join(path,output_name)
with open(output_path, mode='w') as f:
    for i,j in enumerate(result):
        f.write('Case #{}:{}\n'.format(i+1,print_list(j)))