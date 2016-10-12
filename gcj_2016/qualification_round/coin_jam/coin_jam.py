import os
import sympy
import math

folder = 'qualification_round'
path = os.path.join(os.getcwd(),folder + '\\' +'coin_jam')
name = 'C-large'
input_name = name + '.in'
input_path = os.path.join(path,input_name)

with open(input_path, mode='r') as f:
        n_lines = int(f.readline().split()[0])
        for i in range(n_lines):
            digits,numbers = [int(x) for x in f.readline().split()]


def change_base(number,base):
    result = 0
    for i,j in enumerate(list(reversed(str(number)))):
        result += int(int(j) * math.pow(base,i))
    return result

def get_bases(number):
    result=[]
    for i in range(2,11):
        result.append(change_base(number,i))
    return result

def is_jamcoin(numbers_list):
    for i in numbers_list:
        if sympy.isprime(i):
            return False
    else:
        return True

def get_factors(numbers_list):
    result = []
    for i in numbers_list:
        divisors = (d for d in range(2,i) if i % d == 0)
        result.append(divisors.__next__())
    return result

def fill_with_zeros(number):
        n_zeros = digits - len(str(number)) -2
        zeros=''
        for i in range(n_zeros):
            zeros += '0'
        result = '1' + zeros + str(number) + '1'
        return result

def print_solution(number,factors):
    result = str(number)
    for i in factors:
        result += ' ' + str(i)
    return result

result=[]

#the posibilities should be filtered
posibilities = (int(fill_with_zeros(int(bin(i)[2:]))) for i in range(int(math.pow(2,digits-2))))

counter=0
while counter<numbers:
    p = posibilities.__next__()
    bases = get_bases(p)
    if is_jamcoin(bases):
        result.append(print_solution(p,get_factors(bases)))
        counter += 1

if len(result)!=numbers:
    print('ERROR')

output_name = name + '.out'
output_path = os.path.join(path,output_name)
with open(output_path, mode='w') as f:
    f.write('Case #1:\n')
    for i in result:
        f.write('{}\n'.format(i))