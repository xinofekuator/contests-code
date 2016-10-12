import numpy as np

path = 'C:/Users/Ignacio/PycharmProjects/hashCode/src/practice/'


def execute(name_file):
    with open(path + name_file + '.in', mode='r') as f:
        n_rows, n_columns = [int(x) for x in f.readline().split()]
        painting = [[0 for x in range(n_columns)] for x in range(n_rows)]
        row_count = 0
        for line in f:
            column_count = 0
            for x in line.split():
                for c in x:
                    if c == '#':
                        painting[row_count][column_count] = 1
                    column_count += 1
            row_count += 1

    matrix = np.matrix(painting)

    instructions = []
    line_instructions = []
    for i in range(n_rows):
        for j in range(n_columns):
            if painting[i][j]==1:
                instructions.append(['PAINT_SQUARE',i,j])

    with open(path + name_file + '.out', mode = 'w') as f:
        f.write(str(len(instructions)) + '\n')
        for i in instructions:
            f.write(i[0]+' '+ str(i[1]) + ' ' + str(i[2]) + ' ' + str(0) + '\n')

file1 = 'logo'
file2 = 'right_angle'
file3 = 'learn_and_teach'

execute(file1)
execute(file2)
execute(file3)

#def paint_square(r,c,s):

#def paint_line(r1,c1,r2,c2):

#def erase_cell(r,c):


