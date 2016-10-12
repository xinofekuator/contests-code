import os
import math
import itertools
import numpy

folder = 'qualification_round'
path = os.path.join(os.getcwd(),folder + '\\' +'fractiles')
name = 'D-large'
input_name = name + '.in'
input_path = os.path.join(path,input_name)

with open(input_path, mode='r') as f:
        n_lines = int(f.readline().split()[0])
        tiles_list=[]
        complexity_list=[]
        students_list=[]
        for i in range(n_lines):
            tiles,complexity,students = [int(x) for x in f.readline().split()]
            tiles_list.append(tiles)
            complexity_list.append(complexity)
            students_list.append(students)

result=[]


def get_tile(array,complexity):
    result = array
    for i in range(complexity-1):
        if (i < complexity-2):
            result = result[0:1]
        aux_result = []
        for i in result:
            if i==0:
                aux_result.append(array)
            elif i==1:
                #GOLD --> more gold
                aux_result.append([1]*len(array))
            else:
                print('ERROR')
        result = [n for sublist in aux_result for n in sublist]
    return result

for tiles,complexity,students in zip(tiles_list,complexity_list,students_list):
    if students>=tiles and complexity>tiles:
        adv = int(math.pow(tiles,complexity)/tiles)
        aux_result=[]
        for i in range(tiles):
            aux_result.append(1 + i * adv)
        result.append(aux_result)
    elif complexity:
        result.append(['IMPOSSIBLE'])
    # cases = list(itertools.product([1,0], repeat = tiles))
    # n_cases = len(cases)
    # posibilities = numpy.matrix(cases)
    # steps = numpy.matrix.transpose(posibilities)
    # n_columns = int(math.pow(tiles,complexity))
    # final_matrix = []
    # for i in posibilities:
    #     final_matrix.append(get_tile(i.tolist()[0],complexity))
    # partial_result=[]
    # for i in range(students):
    #     if len(final_matrix)==1:
    #         break
    #     m = numpy.matrix(final_matrix)
    #     sum_values = sum(m).tolist()[0]
    #     max_value = max(sum_values)
    #     index = sum_values.index(max_value)
    #     partial_result.append(index+1)
    #     to_remove = m[:,index].nonzero()[0].tolist()
    #     new_matrix=[]
    #     for i,j in enumerate(final_matrix):
    #         if i not in to_remove:
    #             new_matrix.append(j)
    #     final_matrix = new_matrix
    #
    # if len(final_matrix)!=1:
    #     partial_result = ['IMPOSSIBLE']
    # result.append(partial_result)

def print_solution(indexes):
    result = ''
    for i in indexes:
        result += ' ' + str(i)
    return result

output_name = name + '.out'
output_path = os.path.join(path,output_name)
with open(output_path, mode='w') as f:
    for i,j in enumerate(result):
        f.write('Case #{}:{}\n'.format(i+1,print_solution(j)))