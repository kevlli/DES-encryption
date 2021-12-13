#encrypt('a', "0001001100110100010101110111100110011011101111001101111111110001")

#pc1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 49, 51, 43, 35, 27, 1911     3   60    52    44   36
pc1 = [57,   49,    41,   33,    25,    17,    9,
    1,   58,    50,   42,    34,    26,   18,
    10,    2,    59,   51,    43,    35,   27,
    19,   11,     3,   60,    52,   44,   36,
    63,   55,    47,   39,    31,    23,   15,
    7,   62,    54,   46,    38,    30,   22,
    14,    6,    61,   53,    45,    37,   29,
    21,   13,     5,   28,    20,   12,    4,]
def encrypt(plaintext, key):
    key1 = ""
    for i in range(0,len(pc1)):
        #python starts at 0, table starts a 1, so subtract 1
        key1 += key[pc1[i] - 1]
    print(key1)
    #print(key[57])
    #print(key[49])
    #print(key[41])
    
    
    c0 = ""
    d0 = ""
    for i in range(0, len(key1)):
        if (i < len(key1) / 2):
            c0 += key1[i]
        else:
            d0 += key1[i]
    print (c0)
    print (d0)
    
    
    klistc = []
    shifts = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    for i in range(0, 16):
        if i == 0:
            klistc.append(leftshift(c0))
        else:
            klistc.append(leftshift(klistc[i - 1]))
            if shifts[i] == 2:
                klistc[i] = leftshift(klistc[i])
    for i in range(len(klistc)):
        print (klistc[i])
        print ("")
            
def leftshift(string):
    newstring = ""
    for i in range(len(string)):
        if i == len(string) - 1:
            newstring += string[0]
        else:
            newstring += string[i + 1]
    return (newstring)
    
        
    
