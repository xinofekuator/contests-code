import os

path = os.path.join(os.getcwd(),'3_machine')
name = 'submitInput'
input_name = name + '.txt'
input_path = os.path.join(path,input_name)

with open(input_path, mode='r') as f:
        dots = f.readline().split()
        code = f.readline().split()
        instructions = dict()
        is_code = True
        line = f.readline().split()
        symbols = ["#","1","0",""]
        actions = ['move','state','write']
        actual_symbol = None
        actual_state = None
        while line[0] != 'tapes:':
            first_line = line[0].replace(':','')
            first_line = first_line.replace("'",'')
            if first_line in symbols:
                actual_symbol = first_line
                instructions[actual_state][actual_symbol]=dict()
            elif first_line in actions:
                instructions[actual_state][actual_symbol][first_line] = line[1]
            else:
                actual_state=first_line
                instructions[actual_state] = dict()
            line = f.readline().split()

        tape = f.readline().split()
        inputs = list()
        while tape[0] != '...':
            inputs.append(tape[1].replace("'",""))
            tape = f.readline().split()

result = list()

for input in inputs:
    state = 'start'
    cursor = 0
    aux_result = list(input)
    while state != 'end':
        try:
            symbol = aux_result[cursor]
        except:
            symbol = ''
        for action,value in instructions[state][symbol].items():
            if action == 'move':
                if value ==  'left':
                    cursor -= 1
                elif value == 'right':
                    cursor += 1
            elif action == 'state':
                state = value
            elif action == 'write':
                try:
                    aux_result[cursor] = value.replace("'","")
                except:
                    aux_result.append(value.replace("'",""))
    result.append("".join(aux_result))

output_name = name + '.out'
output_path = os.path.join(path,output_name)
with open(output_path, mode='w') as f:
    for i,j in enumerate(result):
        f.write('Tape #{}: {}\n'.format(i+1,j))