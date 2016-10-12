import os

folder = 'qualification_round'
path = os.path.join(os.getcwd(),folder + '\\' +'counting_sheep')
name = 'A-large'
input_name = name + '.in'
input_path = os.path.join(path,input_name)

with open(input_path, mode='r') as f:
        n_lines = int(f.readline().split()[0])
        numbers = []
        for i in range(n_lines):
            numbers.append(f.readline().split()[0])


result = []
for n in numbers:
    digits = list('1234567890')
    found = False
    position = 0
    if n=='0':
        result.append('INSOMNIA')
        found = True
    while not found:
        position += 1
        current_number = str(position * int(n))
        for d in current_number:
            if d in digits:
                digits.remove(d)
            if len(digits)==0:
                found = True
                result.append(current_number)
                break
            elif position == 100:
                found = True
                result.append('INSOMNIA')
                print('insomnia {}'.format(n))
                break

output_name = name + '.out'
output_path = os.path.join(path,output_name)
with open(output_path, mode='w') as f:
    for i,j in enumerate(result):
        f.write('Case #{}: {}\n'.format(i+1,j))