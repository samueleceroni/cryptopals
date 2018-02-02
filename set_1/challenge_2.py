hex_string_1 = "1c0111001f010100061a024b53535009181c"
hex_string_2 = "686974207468652062756c6c277320657965"
hex_string_tot = ''

#hex_string_1 = "5"
#hex_string_2 = "5"



bin_string_1 = ''
bin_string_2 = ''

bin_string_total = ''
bin_string_temp = ''


hexDict = {
    '0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101',
    '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'a':'1010', 'b':'1011',
    'c':'1100', 'd':'1101', 'e':'1110', 'f':'1111'}

def hex_to_bin(a):
    return hexDict[a]

def bin_to_hex(a):
    for i in (hexDict):
        if(hexDict[i] == a):
            return i

def xor_string(a,b):
    if (a!=b):
        return '1'
    else:
        return '0'   

if len(hex_string_1) != len(hex_string_2):
    print("Strings are not equal.")
    exit()

for i in range(len(hex_string_1)):
    #print(hex_string[i])
    #bin_string += hex_to_bin(hex_string[len(hex_string)-i-1])
    bin_string_1 += hex_to_bin(hex_string_1[i])

#print(bin_string_1)

for i in range(len(hex_string_2)):
    #print(hex_string[i])
    #bin_string += hex_to_bin(hex_string[len(hex_string)-i-1])
    bin_string_2 += hex_to_bin(hex_string_2[i])

#print(bin_string_2)

for i in range (len(bin_string_1)):
    bin_string_total += xor_string(bin_string_1[i], bin_string_2[i])

#print(bin_string_total)

for i in range(len(bin_string_total)):
    bin_string_temp += bin_string_total[i]
    if ((i+1)%4 == 0):
        #print(bin_string_temp)
        hex_string_tot += (str)(bin_to_hex(bin_string_temp))
        bin_string_temp = ''

print(hex_string_tot)