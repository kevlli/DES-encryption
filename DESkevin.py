

#pc1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 49, 51, 43, 35, 27, 1911     3   60    52    44   36
pc1 = [57,   49,    41,   33,    25,    17,    9,
    1,   58,    50,   42,    34,    26,   18,
    10,    2,    59,   51,    43,    35,   27,
    19,   11,     3,   60,    52,   44,   36,
    63,   55,    47,   39,    31,    23,   15,
    7,   62,    54,   46,    38,    30,   22,
    14,    6,    61,   53,    45,    37,   29,
    21,   13,     5,   28,    20,   12,    4]

pc2 = [14,    17,   11,    24,     1,    5,
    3,    28,   15,     6,    21,   10,
    23,    19,   12,     4,    26,    8,
    16,     7,   27,    20,    13,    2,
    41,    52,   31,    37,    47,   55,
    30,    40,   51,    45,    33,   48,
    44,    49,   39,    56,    34,   53,
    46,    42,   50,    36,    29,   32]

ip = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44,
    36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14,
    6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41,
    33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39,
    31, 23, 15, 7]

ebit = [32,     1,    2,     3,     4,    5,
                  4,     5,    6,     7,     8,    9,
                  8,     9,   10,    11,    12,   13,
                 12,    13,   14,    15,    16,   17,
                 16,    17,   18,    19,    20,   21,
                 20,    21,   22,    23,    24,   25,
                 24,    25,   26,    27,    28,   29,
                 28,    29,   30,    31,    32,    1]
def encrypt(plaintext, key):
    key1 = permutation(key, pc1)
    c0 = ""
    d0 = ""
    for i in range(len(key1)):
        if (i < len(key1) / 2):
            c0 += key1[i]
        else:
            d0 += key1[i]
    #print (c0)
    #print (d0)
    
    
    klistc = []
    klistd = []
    shifts = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    for i in range(16):
        if i == 0:
            klistc.append(leftshift(c0))
            klistd.append(leftshift(d0))
        else:
            klistc.append(leftshift(klistc[i - 1]))
            klistd.append(leftshift(klistd[i - 1]))
            if shifts[i] == 2:
                klistc[i] = leftshift(klistc[i])
                klistd[i] = leftshift(klistd[i])
    #for i in range(len(klistc)):
    #    print (klistc[i])
    #    print ("")
    #    print (klistd[i])
    #    print("")


    klist = []
    for i in range(16):
        subkey = klistc[i] + klistd[i]
        subkey = permutation(subkey, pc2)
        klist.append(subkey)
        #print(klist[i])

    #Step 2
    plainip = permutation(plaintext, ip)
    #print(plainip)
    #divide into two halve
    ipL = [plainip[:(int)(len(plainip)/2)]]
    ipR = [plainip[(int)(len(plainip)/2):]]
    print(ipL[0])
    print(ipR[0])
    for i in range (16):
        #ipL.append(ipR[i])
        #ipR.append(ipL[i] ^(klist[i] ^ permutation(ipR[i], ebit)))
        


def permutation(string, ptable):
    pstring = ""
    for i in range(len(ptable)):
        #python starts at 0, table starts at 1, so subtract 1
        pstring += string[ptable[i] - 1]
    return pstring

    
def leftshift(string):
    newstring = ""
    for i in range(len(string)):
        if i == len(string) - 1:
            newstring += string[0]
        else:
            newstring += string[i + 1]
    return (newstring)

def functionf(text, key):
    expandedtext = permutation(text, ebit)
    xored = key ^ expandedtext
    compacted = ""
    
    
permutation("11100001100110010101010111111010101011001100111100011110",pc2)
    
        
encrypt('0000000100100011010001010110011110001001101010111100110111101111', "0001001100110100010101110111100110011011101111001101111111110001")