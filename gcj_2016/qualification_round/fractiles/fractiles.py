import os
import math
import itertools
import numpy

folder = 'qualification_round'
path = os.path.join(os.getcwd(),folder + '\\' +'fractiles')
name = 'fractiles'
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

for tiles,complexity,students in zip(tiles_list,complexity_list,students_list):

    cases = list(itertools.product([1,0], repeat = tiles))
    n_cases = len(cases)
    posibilities_indexes = list(range(n_cases))
    posibilities = numpy.matrix(cases)
    steps = numpy.matrix.transpose(posibilities)

    def update_steps():
        updated_posibilities = []
        for i in posibilities_indexes:
            updated_posibilities.append(cases[i])
        updated_posibilities = numpy.matrix(updated_posibilities)
        updated_steps = numpy.matrix.transpose(updated_posibilities)
        return updated_steps

    #list of position to look at given
    #for instance: in a complexity 3, two numbers are given the position of the first change and the position of the second
    def get_posibilities(list_positions,steps):
        for level in range(complexity-1):
            steps_aux = steps
            new_posibilities = []
            #print('level {}, list_pos:{}, steps:{}'.format(level,list_positions[level],steps_aux[list_positions[level]]))
            for j,k in enumerate(steps_aux[list_positions[level]].tolist()[0]):
                if k==0:
                    new_posibilities.append(posibilities[j].tolist()[0])
                else:
                    new_posibilities.append([1]*tiles)
            new_posibilities = numpy.matrix(new_posibilities)
            steps_aux =  numpy.matrix.transpose(new_posibilities)
        return new_posibilities

    #the number of elements is the complexity-1
    def get_position(position_list):
        value = 0
        for i in position_list:
            value =+ tiles * i
        return value

    options=[]
    if complexity >3:
        for i in range(complexity-1):
            options.append(range(tiles))
        positions = list(itertools.product(*options))
    elif complexity == 2:
        positions = [[i] for i in range(tiles)]
    else:
        positions = []

    #create the whole solution space
    turns = 0
    partial_result = []
    for i in positions:
        if turns >= students:
            partial_result.append('IMPOSSIBLE')
            break
        current_posibilities = get_posibilities(i,steps)
        sum_values = sum(current_posibilities).tolist()[0]
        max_value = max(sum_values)
        index = sum_values.index(max_value)
        to_remove = current_posibilities[:,index].nonzero()[0].tolist()
        print('i: {}, positions:{}'.format(to_remove,posibilities_indexes))
        for i in to_remove:
            posibilities_indexes.remove(i)
        #partial_result.append(get_position(i)+index)
        if len(posibilities_indexes)==1:
            partial_result.append(index)
            #ended
        turns += 1
        update_steps()
        #sum_values.append(sum(current_posibilities).tolist()[0])
    #sum_values = list(itertools.chain(*sum_values))

def print_solution(indexes):
    result = ''
    for i in indexes:
        result += ' ' + str(i)
    return result

output_name = name + '.out'
output_path = os.path.join(path,output_name)
with open(output_path, mode='w') as f:
    for i in result:
        f.write('Case #{}:{}\n'.format(print_solution(i)))