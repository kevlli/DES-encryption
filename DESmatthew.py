
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

def encrypt(plaintext, key):
    key1 = permutation(key, pc1)
    slist = split(key1)
    c0 = slist[0]
    d0 = slist[1]

    print (c0)
    print (d0)
    
    
    klistc = []
    klistd = []
    shifts = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    for i in range(0, 16):
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


    
    print("keys:")
    klist = []
    for i in range(0,16):
        subkey = klistc[i] + klistd[i]
        subkey = permutation(subkey, pc2)
        klist.append(subkey)
        #print keys
        print(klist[i])
        
    print("ip permutated plaintext:")
    plaintext1 = permutation(plaintext, ip)
    print(plaintext1)
    print("split plaintext:")
    print(split(plaintext1))

def permutation(string, ptable):
    pstring = ""
    for i in range(0,len(ptable)):
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

encrypt("0001001100110100010101110111100110011011101111001101111111110001", "0001001100110100010101110111100110011011101111001101111111110001")
