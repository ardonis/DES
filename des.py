def permute(i, table):
    permList = ["0"] * len(table)


    c = 0
    for x in table:
        permList[c] = i[x]

        c += 1

    return "".join(permList)


def xor(val1, val2):

    # takes two inputs as strings and xor-s them as long as both consist of 1 and 0. The two strings have to be the same lenght

    if len(val1) != len(val2):

        raise ValueError("Two inputs are different lenght!")

    out = ""

    dict1 = {"0": False, "1": True}

    for i in range(len(val1)):

        if dict1[val1[i]] == dict1[val2[i]]:

            out = out + "0"

        else:

            out = out + "1"

    return out


def Fbox(pText, Key):

    def expansion(inp):

       # takes a 32-bit string as input and expands it to 48 bits"""

        STable = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9,

                  8, 9, 10, 11, 12, 13, 12, 13, 14, 15,

                  16, 17, 16, 17, 18, 19, 20, 21, 20, 21,

                  22, 23, 24, 25, 24, 25, 26, 27, 28, 29,

                  28, 29, 30, 31, 32, 1]

        outnum = [0]*48

        cyclecount = int(0)

        for x in STable:

            outnum[cyclecount] = inp[x-1]

            cyclecount = cyclecount+1

        return "".join(outnum)

    def sBox(binInp, boxNum):

       # takes a 6-bit string and a number as inputs and returns a 4-bit output as string"""

        print(binInp)

        S1 = [[14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7],

              [0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8],

              [4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0],

              [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]]

        S2 = [[15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10],

              [3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5],

              [0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15],

              [13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9]]

        S3 = [[10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8],

              [13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1],

              [13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7],

              [1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12]]

        S4 = [[7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15],

              [13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9],

              [10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4],

              [3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14]]

        S5 = [[2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9],

              [14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6],

              [4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14],

              [11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3]]

        S6 = [[12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11],

              [10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8],

              [9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6],

              [4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13]]

        S7 = [[4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1],

              [13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6],

              [1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2],

              [6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12]]

        S8 = [[13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7],

              [1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2],

              [7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8],

              [2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11]]

        colomn = int(binInp[1:5], 2)

        row = int(binInp[0] + binInp[5], 2)

        output = ""

        if boxNum == 1:

            output = bin(S1[row][colomn]+16)[3:]

        elif boxNum == 2:

            output = bin(S2[row][colomn]+16)[3:]

        elif boxNum == 3:

            output = bin(S3[row][colomn]+16)[3:]

        elif boxNum == 4:

            output = bin(S4[row][colomn]+16)[3:]

        elif boxNum == 5:

            output = bin(S5[row][colomn]+16)[3:]

        elif boxNum == 6:

            output = bin(S6[row][colomn]+16)[3:]

        elif boxNum == 7:

            output = bin(S7[row][colomn]+16)[3:]

        elif boxNum == 8:

            output = bin(S8[row][colomn]+16)[3:]

        elif boxNum > 8:

            raise NameError("No more s-boxes")

        # print("colomn: {}\nrow: {}\ninput: {}\noutput: {}".format(colomn, row, binInp, output))"""

        return output

    def pBox(Inp):

        # takes a 32-bit input as string and shuffles the bits"""

        tbl = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31,

               10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

        out = [0]*32

        i = 0

        for x in tbl:

            out[x-1] = Inp[i]

            i = i+1

        return "".join(out)

    if len(pText) == 32:

        Text1 = expansion(pText)

    else:

        raise IndexError("input too long: " + str(len(pText)))

    text2 = xor(Text1, Key)

    text3 = []

    for i in range(8):

        text3.append(sBox(text2[i*6:i*6+6], i+1))

    text4 = pBox("".join(text3))

    return text4


def generateKey(K):
    # takes a 64-bit input, outputs a list of 48-bit sub-keys

    def PC1(a):
        tbl = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
               10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36]

        return permute(a, tbl)

    return PC1(K)



# testing part

print(generateKey("The Left and Right halves of the table show which bits from XXXX"))

