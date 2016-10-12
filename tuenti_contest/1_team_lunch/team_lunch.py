import os
import numpy

path = os.path.join(os.getcwd(),'1_team_lunch')
name = 'submitInput'
input_name = name + '.txt'
input_path = os.path.join(path,input_name)

with open(input_path, mode='r') as f:
        n_lines = int(f.readline().split()[0])
        tables = list()
        for i in range(n_lines):
            tables.append(int(f.readline().split()[0]))

result = list()
for i in tables:
    if i>4:
        result.append((i+1)//2 - 1)
    elif i == 0:
        result.append(0)
    else:
        result.append(1)

output_name = name + '.out'
output_path = os.path.join(path,output_name)
with open(output_path, mode='w') as f:
    for i,j in enumerate(result):
        f.write('Case #{}: {}\n'.format(i+1,str(j)))