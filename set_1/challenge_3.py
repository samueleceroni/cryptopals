hex_string_1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
bin_string_1 = ''
bin_string_2= ''
bin_string_total = ''
temp_string_bin = ''
string_char = ''
bin_char=''

score = {}
bestscore =-1
bestkey = ''

def to_binary(a):
    bin_a=bin(a)
    bin_b=''
    i=len(bin_a)-1
    while bin_a[i] == '0' or bin_a[i] == '1':
        bin_b = bin_a[i] + bin_b
        i -= 1
    while(len(bin_b)<8):
        bin_b = '0' + bin_b
    return bin_b

hexDict = {
    '0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101',
    '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'a':'1010', 'b':'1011',
    'c':'1100', 'd':'1101', 'e':'1110', 'f':'1111'}


def hex_to_bin(a):
    return hexDict[a]


def xor_bit(a,b):
    if (a!=b):
        return '1'
    else:
        return '0'


def decipher(hex_string_1, num):
    tempscore = 0
    bin_string_1 = ''
    #decode hex string to bin
    for i in range(len(hex_string_1)):
        bin_string_1 += hex_to_bin(hex_string_1[i])

    bin_string_2= ''
    bin_string_total = ''
    temp_string_bin = ''
    string_char = ''
    bin_char=''
    bin_char = to_binary(num)

    while(len(bin_string_2)<len(bin_string_1)):
        bin_string_2 = bin_string_2 + bin_char

    for i in range (len(bin_string_1)):
        bin_string_total += xor_bit(bin_string_1[i], bin_string_2[i])

    for i in range(len(bin_string_total)):
        temp_string_bin += bin_string_total[i]
        if((i+1)%8 == 0):
            string_char += chr(int(temp_string_bin, 2)) 
            temp_string_bin = ''

    for letter in range(len(string_char)):
        let = string_char[letter]
        if ord(let)>128:
            tempscore = 0
            break
        elif let == 'a' or let == 'A':
            tempscore+=8
        elif let == 'e' or let == 'E':
            tempscore+=13
        elif let == 'i' or let == 'I':
            tempscore+=7
        elif let == 't' or let == 'T':
            tempscore+=9
        elif let == 'o' or let == 'O':
            tempscore+=8
        elif let == 'n' or let == 'N':
            tempscore+=7
        elif let == ' ':
            tempscore+=13


    score[str(num)] = tempscore

    return str (chr(int(bin_char, 2)) + ' : ' + string_char)



for num in range (128):
    decipher(hex_string_1, num)

for num in score:
    if score[num] > bestscore:
        bestscore = score[num]
        bestkey = num

print(decipher(hex_string_1, int(bestkey)))