import os
import numpy
import itertools

folder = 'round1A'
path = os.path.join(os.getcwd(),folder + '\\' +'BFF')
name = 'test'
input_name = name + '.in'
input_path = os.path.join(path,input_name)

with open(input_path, mode='r') as f:
        n_lines = int(f.readline().split()[0])
        people = []
        for i in range(n_lines):
            n_people = int(f.readline().split()[0])
            people.append([int(x) for x in f.readline().split()])

def get_max_cycle(list):
    #cyclic or reciprocal in the last one
    aux_dict = dict(enumerate(list))
    visited = list()
    counter = 1
    index = 0
    cycle = False
    while index not in visited and not(cycle):
        visited.append(i)
        index = aux_dict[i]

        if cycle:
            try:
                list.index()
            except:
                cycle = False

def find_reciprocal():


output_name = name + '.out'
output_path = os.path.join(path,output_name)
with open(output_path, mode='w') as f:
    for i,j in enumerate(result):
        f.write('Case #{}: {}\n'.format(i+1,str(j)))