hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

bin_string = ''
temp_bin_string = ''
temp_int_string = ''
temp_b64_string = ''

def hex_to_bin(a):
    hexDict = {
    '0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101',
    '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'a':'1010', 'b':'1011',
    'c':'1100', 'd':'1101', 'e':'1110', 'f':'1111'}
    return hexDict[a]

def bin_to_dec(a):
    num = 0
    for i in range(len(a)):
        k = len(a)-i -1
        if a[k] == '1':
            num += 2**i
    return (str)(num)


def dec_to_b64(a):
    base64Dict={'0':'A', '16':'Q', '32':'g', '48':'w',
    '1':'B', '17':'R', '33':'h', '49':'x',
    '2':'C', '18':'S', '34':'i', '50':'y',
    '3':'D', '19':'T', '35':'j', '51':'z',
    '4':'E', '20':'U', '36':'k', '52':'0',
    '5':'F', '21':'V', '37':'l', '53':'1',
    '6':'G', '22':'W', '38':'m', '54':'2',
    '7':'H', '23':'X', '39':'n', '55':'3',
    '8':'I', '24':'Y', '40':'o', '56':'4',
    '9':'J', '25':'Z', '41':'p', '57':'5',
    '10':'K', '26':'a', '42':'q', '58':'6',
    '11':'L', '27':'b', '43':'r', '59':'7',
    '12':'M', '28':'c', '44':'s', '60':'8',
    '13':'N', '29':'d', '45':'t', '61':'9',
    '14':'O', '30':'e', '46':'u', '62':'+',
    '15':'P', '31':'f', '47':'v', '63':'/'}
    return base64Dict[a];


#####################################
#####################################
#####################################



for i in range(len(hex_string)):
    #print(hex_string[i])
    #bin_string += hex_to_bin(hex_string[len(hex_string)-i-1])
    bin_string += hex_to_bin(hex_string[i])

#print (bin_string)

i = len(bin_string)-1

#print(i)

temp_bin_string=''
j=0
while (j<=i):
    temp_bin_string = bin_string[i-j] + temp_bin_string
    #print(temp_bin_string)
    j += 1
    if (j==i and (j+1)%6 != 0):
        for k in range(6-((j)%6)):
            temp_bin_string='0'+temp_bin_string
        #print(temp_bin_string)
        #print(bin_to_dec(temp_bin_string))
        temp_b64_string = dec_to_b64(bin_to_dec(temp_bin_string))+ temp_b64_string
        temp_bin_string = ''

    if (j % 6 == 0):
        #print(temp_bin_string)
        #print(bin_to_dec(temp_bin_string))
        temp_b64_string = dec_to_b64(bin_to_dec(temp_bin_string))+ temp_b64_string
        temp_bin_string = ''

print(temp_b64_string)
