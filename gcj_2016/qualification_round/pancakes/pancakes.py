import os
import numpy

folder = 'qualification_round'
path = os.path.join(os.getcwd(),folder + '\\' +'pancakes')
name = 'B-large'
input_name = name + '.in'
input_path = os.path.join(path,input_name)

with open(input_path, mode='r') as f:
        n_lines = int(f.readline().split()[0])
        stacks = []
        for i in range(n_lines):
            stacks.append(f.readline().split()[0])

boolean_array=[]
for i in stacks:
    aux_array=[]
    for j in i:
        if j=='+':
            aux_array.append(True)
        elif j=='-':
            aux_array.append(False)
        else:
            print('Error')
    boolean_array.append(aux_array)


result = []
for n in boolean_array:
    movements = 0
    aux_list = n
    smiles = False
    while not smiles:
        aux_value = aux_list[0]
        position = -1
        for i,j in enumerate(aux_list):
            if j!=aux_value:
                position = i
                break
        if position==-1:
            if aux_value==False:
                movements += 1
            result.append(movements)
            smiles = True
        else:
            sublist_1 = aux_list[0:position]
            sublist_2 = aux_list[position:len(aux_list)]
            #invert the list
            sublist_1 = numpy.invert(sublist_1)
            sublist_1 = list(reversed(sublist_1))
            #print('{} s1: {} s2: {} p:{}'.format(aux_list,sublist_1,sublist_2,position))
            aux_list = sublist_1 + sublist_2
            #add a movement
            movements += 1



output_name = name + '.out'
output_path = os.path.join(path,output_name)
with open(output_path, mode='w') as f:
    for i,j in enumerate(result):
        f.write('Case #{}: {}\n'.format(i+1,j))