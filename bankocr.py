with open('input.txt') as f:
    lines = f.readlines()

line_len = 27
result = ''
for l in range(0, len(lines), 4):
    str = '' #account number
    for i in range(0, line_len, 3):
        if(lines[l][i+1] == '_' and 
            lines[l+1][i] == '|' and
            lines[l+1][i+1] == ' ' and 
            lines[l+1][i+2] == '|' and
            lines[l+2][i] == '|' and
            lines[l+2][i+1] == '_' and
            lines[l+2][i+2] == '|'):
            str += '0'
        elif(lines[l][i+1] == ' ' and 
            lines[l+1][i] == ' ' and
            lines[l+1][i+1] == ' ' and 
            lines[l+1][i+2] == '|' and
            lines[l+2][i] == ' ' and
            lines[l+2][i+1] == ' ' and
            lines[l+2][i+2] == '|'):
            str += '1'
        elif(lines[l][i+1] == '_' and 
            lines[l+1][i] == ' ' and
            lines[l+1][i+1] == '_' and 
            lines[l+1][i+2] == '|' and
            lines[l+2][i] == '|' and
            lines[l+2][i+1] == '_' and
            lines[l+2][i+2] == ' '):
            str += '2'
        elif(lines[l][i+1] == '_' and 
            lines[l+1][i] == ' ' and
            lines[l+1][i+1] == '_' and 
            lines[l+1][i+2] == '|' and
            lines[l+2][i] == ' ' and
            lines[l+2][i+1] == '_' and
            lines[l+2][i+2] == '|'):
            str += '3'
        elif(lines[l][i+1] == ' ' and 
            lines[l+1][i] == '|' and
            lines[l+1][i+1] == '_' and 
            lines[l+1][i+2] == '|' and
            lines[l+2][i] == ' ' and
            lines[l+2][i+1] == ' ' and
            lines[l+2][i+2] == '|'):
            str += '4'
        elif(lines[l][i+1] == '_' and 
            lines[l+1][i] == '|' and
            lines[l+1][i+1] == '_' and 
            lines[l+1][i+2] == ' ' and
            lines[l+2][i] == ' ' and
            lines[l+2][i+1] == '_' and
            lines[l+2][i+2] == '|'):
            str += '5'
        elif(lines[l][i+1] == '_' and 
            lines[l+1][i] == '|' and
            lines[l+1][i+1] == '_' and 
            lines[l+1][i+2] == ' ' and
            lines[l+2][i] == '|' and
            lines[l+2][i+1] == '_' and
            lines[l+2][i+2] == '|'):
            str += '6'
        elif(lines[l][i+1] == '_' and 
            lines[l+1][i] == ' ' and
            lines[l+1][i+1] == ' ' and 
            lines[l+1][i+2] == '|' and
            lines[l+2][i] == ' ' and
            lines[l+2][i+1] == ' ' and
            lines[l+2][i+2] == '|'):
            str += '7'
        elif(lines[l][i+1] == '_' and 
            lines[l+1][i] == '|' and
            lines[l+1][i+1] == '_' and 
            lines[l+1][i+2] == '|' and
            lines[l+2][i] == '|' and
            lines[l+2][i+1] == '_' and
            lines[l+2][i+2] == '|'):
            str += '8'
        elif(lines[l][i+1] == '_' and 
            lines[l+1][i] == '|' and
            lines[l+1][i+1] == '_' and 
            lines[l+1][i+2] == '|' and
            lines[l+2][i] == ' ' and
            lines[l+2][i+1] == '_' and
            lines[l+2][i+2] == '|'):
            str += '9'
        else: #illegible
            str += '?'                                                         
        
    if '?' in str:
        str += " ILL" 
    elif str.isdigit():
        ADD = 2 #constant used in calculation
        cal = 1
        for x in range(len(str)-1, 0, -1):
            cal *= int(str[x]) + ADD
            ADD += 1

        checksum = cal * int(str[0])
        
        if checksum % 11 != 0:
            str += " ERR"

    result += str + "\n"

f = open("output.txt", "w+")
f.write(result)
f.close()