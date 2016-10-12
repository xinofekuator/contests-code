import os
import numpy
import re

path = os.path.join(os.getcwd(),'4_street_fighter')
name = 'test'
input_name = name + '.txt'
input_path = os.path.join(path,input_name)

with open(input_path, mode='r') as f:
        n_lines = int(f.readline().split()[0])
        moves = list()
        for i in range(n_lines):
            aux_moves = re.split('-|\\n',f.readline())
            moves.append(aux_moves)


combos = list()
buttons = ['K', 'L', 'LD', 'D', 'U', 'RD', 'R', 'P', 'RU', 'LU']
buttons_dict={'K':0, 'L':1, 'LD':2, 'D':3, 'U':4, 'RD':5, 'R':6, 'P':7, 'RU':8, 'LU':9}
combos.append([['L', 'LD', 'D', 'RD', 'R'],'P']) #plus not P
combos.append([['R','RD','D', 'LD', 'L'],'K']) #plus not K
combos.append([['D', 'RD', 'R'],'P']) #plus not P or the one above
combos.append([['R', 'D', 'RD'],'P']) #plus not P
combos.append([['D', 'LD', 'L'],'K']) #plus not K


combos_to_look=list()
for i,j in combos:
    for b in buttons:
        if b!=j:
            combos_to_look.append(i+[b])

combos_transformed = list()
for i in combos_to_look:
    aux_list = list()
    for j in i:
        if j != '':
            aux_list.append(buttons_dict[j])
    combos_transformed.append(aux_list)

moves_transformed = list()
for i in moves:
    aux_list = list()
    for j in i:
        if j != '':
            aux_list.append(buttons_dict[j])
    moves_transformed.append(aux_list)

final_combos = []
final_moves = []
for i in combos_transformed:
    final_combos.append(''.join([str(a) for a in i]))
for i in moves_transformed:
    final_moves.append(''.join([str(a) for a in i]))

result = list()
for i in final_moves:
    count = 0
    actual_text = i
    for c in final_combos:
        if c in actual_text:
            count += 1
            # actual_text = actual_text.replace(c,'',1)
    result.append(count)

output_name = name + '.out'
output_path = os.path.join(path,output_name)
with open(output_path, mode='w') as f:
    for i,j in enumerate(result):
        f.write('Case #{}: {}\n'.format(i+1,str(j)))