import sys

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

fp = [40,     8,   48,    16,    56,   24,    64,   32,
    39,     7,   47,    15,    55,   23,    63,   31,
    38,     6,   46,    14,    54,   22,    62,  30,
    37,     5,   45,    13,    53,   21,    61, 29,
    36,     4,   44,    12,    52,   20,    60,   28,
    35,     3,   43,    11,    51,   19,    59,   27,
    34,     2,   42,    10,    50,   18,    58,   26,
    33,     1,   41,     9,    49,   17,    57,   25]

s1 = [  [14,  4,  13,  1,   2, 15,  11,  8,   3, 10,   6, 12,   5,  9,   0,  7],
        [0, 15,   7,  4,  14,  2,  13,  1,  10,  6,  12, 11,   9,  5,   3,  8],
        [4,  1,  14,  8,  13,  6,   2, 11,  15, 12,   9,  7,   3, 10,   5, 0],
        [15, 12,   8,  2,   4,  9,   1,  7,   5, 11,   3, 14,  10,  0,   6, 13]
        ]

s2 = [ [15,  1,   8, 14,   6, 11,   3,  4,   9,  7,   2, 13,  12,  0,   5, 10],
          [3, 13,   4,  7,  15,  2,   8, 14,  12,  0,   1, 10,   6,  9,  11,  5],
          [0, 14,   7, 11,  10,  4,  13,  1,   5,  8,  12,  6,   9,  3,   2, 15],
         [13,  8,  10,  1,   3, 15,   4,  2,  11,  6,   7, 12,   0,  5,  14,  9] ]

s3 = [ [10,  0,   9, 14,   6,  3,  15,  5,   1, 13,  12,  7,  11,  4,   2,  8],
         [13,  7,   0,  9,   3,  4,   6, 10,   2,  8,   5, 14,  12, 11,  15,  1],
         [13,  6,   4,  9,   8, 15,   3,  0,  11,  1,   2, 12,   5, 10,  14,  7],
          [1, 10,  13,  0,   6,  9,   8,  7,   4, 15,  14,  3,  11,  5,   2, 12] ]

s4 = [ [7, 13,  14,  3,   0,  6,   9, 10,   1,  2,   8,  5,  11, 12,   4, 15],
         [13,  8,  11,  5,   6, 15,   0,  3,   4,  7,   2, 12,   1, 10,  14,  9],
         [10,  6,   9,  0,  12, 11,   7, 13,  15,  1,   3, 14,   5,  2,   8,  4],
          [3, 15,   0,  6,  10,  1,  13,  8,   9,  4,   5, 11,  12,  7,   2, 14] ]

s5 = [ [2, 12,   4,  1,   7, 10,  11,  6,   8,  5,   3, 15,  13,  0, 14,  9],
         [14, 11,   2, 12,   4,  7,  13,  1,   5,  0,  15, 10,   3,  9,   8,  6],
          [4,  2,   1, 11,  10, 13,   7,  8,  15,  9,  12,  5,   6,  3,   0, 14],
         [11,  8,  12,  7,   1, 14,   2, 13,   6, 15,   0,  9,  10,  4,   5,  3] ]

s6 = [ [12,  1,  10, 15,   9,  2,   6,  8,   0, 13,   3,  4,  14,  7,   5, 11,],
         [10, 15,   4,  2,   7, 12,   9,  5,   6,  1,  13, 14,   0, 11,   3,  8],
          [9, 14,  15,  5,   2,  8,  12,  3,   7,  0,   4, 10,   1, 13,  11,  6],
          [4,  3,   2, 12,   9,  5,  15, 10,  11, 14,   1,  7,   6,  0,   8, 13] ]

s7 = [ [4, 11,   2, 14,  15,  0,   8, 13,   3, 12,   9,  7,   5, 10,   6,  1],
         [13,  0,  11,  7,   4,  9,   1, 10,  14,  3,   5, 12,   2, 15,   8,  6],
          [1,  4,  11, 13,  12,  3,   7, 14,  10, 15,   6,  8,   0,  5,   9,  2],
          [6, 11,  13,  8,   1,  4,  10,  7,   9,  5,   0, 15,  14,  2,   3, 12], ]

s8 =  [ [13,  2,   8,  4,   6, 15,  11,  1,  10,  9,   3, 14,   5,  0,  12,  7],
          [1, 15,  13,  8,  10,  3,   7,  4,  12,  5,   6, 11,   0, 14,   9,  2],
          [7, 11,   4,  1,   9, 12,  14,  2,   0,  6,  10, 13,  15,  3,   5,  8],
          [2,  1,  14,  7,   4, 10,   8, 13,  15, 12,   9,  0,   3,  5,   6, 11] ]

sboxes = []

sboxes.append(s1)
sboxes.append(s2)
sboxes.append(s3)
sboxes.append(s4)
sboxes.append(s5)
sboxes.append(s6)
sboxes.append(s7)
sboxes.append(s8)

psbox = [16,   7,  20,  21,
                         29,  12,  28,  17,
                          1,  15,  23,  26,
                          5,  18,  31,  10,
                          2,   8,  24,  14,
                         32,  27,   3,   9,
                         19,  13,  30,   6,
                         22,  11,   4,  25]

def encrypt(plaintext, key, base):
    if (base == "hex" or base == "hexadecimal"):
        length = len(plaintext)
        plaintext = format(int(plaintext, 16), "b")
        plaintext = addzeros(plaintext, length * 4)
        length = len(key)
        key = format(int(key, 16), "b")
        key = addzeros(key, length * 4)

    #else if (base == 'ascii' or base == 'ASCII' or base == 'text'):
        
    while(len(plaintext) % 64 != 0):
        plaintext += '0'
    for x in range( int(len(plaintext) / 64) ):
        encrypthelper(plaintext[64 * x: 64 * (x+1)], key)

    
        


    
def encrypthelper(plaintext, key):

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
    ipsplit = split(plainip)
    ipL = [ ipsplit[0] ]
    ipR = [ ipsplit[1] ]

    for i in range (16):
        ipL.append(ipR[i])
        ipR.append( addzeros( format(int(ipL[i],2) ^ int(functionf(ipR[i],klist[i]),2), "b") , 32) )

        
    ipRL = []
    for j in range (17):
        ipRL.append(ipR[j] + ipL[j])
        
    FinalPerm = permutation(ipRL[j], fp)
    print(FinalPerm)
    #addzeros makes sure that the starting zero is not removed
    print(addzeros((hex(int(FinalPerm, 2))[2:]),16))

def decrypt(plaintext, key, base):
    if (base == "hex" or base == "hexadecimal"):
        length = len(plaintext)
        plaintext = format(int(plaintext, 16), "b")
        plaintext = addzeros(plaintext, length * 4)
        length = len(key)
        key = format(int(key, 16), "b")
        key = addzeros(key, length * 4)

    #else if (base == 'ascii' or base == 'ASCII' or base == 'text'):
        
    while(len(plaintext) % 64 != 0):
        plaintext += '0'
    for x in range( int(len(plaintext) / 64) ):
        decrypthelper(plaintext[64 * x: 64 * (x+1)], key)

    
        


    
def decrypthelper(plaintext, key):

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
    klistc = reverselist(klistc)
    klistd = reverselist(klistd)
    

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
    ipsplit = split(plainip)
    ipL = [ ipsplit[0] ]
    ipR = [ ipsplit[1] ]

    for i in range (16):
        ipL.append(ipR[i])
        ipR.append( addzeros( format(int(ipL[i],2) ^ int(functionf(ipR[i],klist[i]),2), "b") , 32) )

        
    ipRL = []
    for j in range (17):
        ipRL.append(ipR[j] + ipL[j])
        
    FinalPerm = permutation(ipRL[j], fp)
    print(FinalPerm)
    #addzeros makes sure that the starting zero is not removed
    print(addzeros((hex(int(FinalPerm, 2))[2:]),16))



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

def split(string):
    slist = ["",""]
    for i in range(0, len(string)):
        if (i < len(string) / 2):
            slist[0] += string[i]
        else:
            slist[1] += string[i]
    return slist

def functionf(text, key):
    expandedtext = permutation(text, ebit)
    xored = int(key,2) ^ int(expandedtext,2)
    xored = format(xored, "b")

    xored = addzeros(xored, 48)
    #while (len(xored) != 48) : #adds leading 0s to first 6 bits
        #xored = '0' + xored
    compacted = ""
    for i in range(8):
        compacted += sbox(xored[i * 6: (i + 1) * 6], sboxes[i])
    compacted = permutation(compacted,psbox)
    return compacted
    
def sbox(text, s):
    row = int(text[0]) * 2 + int(text[5])
    column = int(text[1]) * 8 + int(text[2]) * 4 + int(text[3]) * 2 + int(text[4])
    value = format(s[row][column], "b")

    value = addzeros(value, 4)
    #while (len(value) != 4):
        #value = '0' + value #adds prefixing 0s for some bits (i.e. 0001)
    return value

def addzeros(binarystring, length):
    while (len(binarystring) < length):
        binarystring = '0' + binarystring
    return binarystring

def reverselist(keylist):
    x = []
    for i in range(0, len(keylist)):
        x.append(keylist[len(keylist) - i - 1])
    return x

inp = open("plaintext.txt", "rb").read()
for x in range(len(inp)):
    print(inp[x])

encrypt("0123456789ABCDEF","133457799BBCDFF1","hex")
decrypt("85e813540f0ab405","133457799BBCDFF1","hex")

