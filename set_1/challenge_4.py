#########################################
hexDict = {
    '0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101',
    '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'a':'1010', 'b':'1011',
    'c':'1100', 'd':'1101', 'e':'1110', 'f':'1111'
    }

##########################################
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

###########################################
def hex_to_bin(a):
    return hexDict[a]

###########################################
def xor_bit(a,b):
    if (a!=b):
        return '1'
    else:
        return '0'

def xor_hexstring_byte(hex_string, num):
    bin_string_1 = ''
    #decode hex string to bin
    for i in range(len(hex_string)):
        bin_string_1 += hex_to_bin(hex_string[i])

    bin_string_2 = ''
    bin_string_total = ''
    temp_string_bin = ''
    string_char = ''
    bin_char = to_binary(num)

    # add data to bin_string_2
    while(len(bin_string_2)<len(bin_string_1)):
        bin_string_2 = bin_string_2 + bin_char
    
    # calculate xor between the two generated strings
    for i in range (len(bin_string_1)):
        bin_string_total += xor_bit(bin_string_1[i], bin_string_2[i])

    # convert bin_string_total into string_char (8bit per time) 
    for i in range(len(bin_string_total)):
        temp_string_bin += bin_string_total[i]
        if((i+1)%8 == 0):
            string_char += chr(int(temp_string_bin, 2)) 
            temp_string_bin = ''

    #return the string_char
    return string_char

######################################
def calculate_score (string_char):

    tempscore = 0

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

        #print(tempscore)

    return tempscore

######################################
def best_score_string (hex_string):
    score = {}
    bestscore = -1
    bestkey = ''

    for num in range (128):
        temp_string = xor_hexstring_byte(hex_string, num)
        score[str(num)] = calculate_score(temp_string)

    for num in score:
        if score[num] > bestscore:
            bestscore = score[num]
            bestkey = num

    string_char = xor_hexstring_byte(hex_string, int(bestkey))
    
    #print(bestscore)

    return string_char, bestscore, bestkey


def main():
    thebestscore = -1
    thebestkey = ''
    thebeststring = ''
    index = -1
    bestscores = {}
    beststring = {}
    bestkeys = {}

    f = open("4.txt","r") #opens file with name of "4.txt"
    string_list = f.read().splitlines()
    f.close()

    for i in range(len(string_list)):
        beststring[str(i)], bestscores[str(i)], bestkeys[str(i)] = best_score_string (string_list[i]) 

    #for i in range(len(string_list)):
    #    print(str(beststring[str(i)])+ " : " + str(bestscores[str(i)]))

    for i in range(len(bestscores)):
        if (thebestscore < bestscores[str(i)]):
            thebestkey = bestkeys[str(i)]
            thebestscore = bestscores[str(i)]
            thebeststring = beststring[str(i)]
            index = i

    '''
    print(f.readline())
    f.close()
    '''
    print("original string (" + str(i) + "): \"" + string_list[i] + "\"\n")
    print("string: " + thebeststring)
    print("score: " + str(thebestscore))
    print("key: \'" + str(chr(int(thebestkey))) + '\'')



if __name__ == '__main__':
    main()