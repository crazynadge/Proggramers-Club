def BinaryToDecimal(num):
    num = bin(num)
    binaryNum = "0"
    for i in range(2, len(num)):
        binaryNum += num[i]
    return binaryNum
def Complement_2(num):
    negNum1 = ""
    for bit in num:
        if(bit == '0'):
            negNum1 += '1'
        else:
            negNum1 += '0'
    negNum2 = ""
    negNum1 = negNum1[::-1]
    if(negNum1[0] == '1'):
        counter = 1
        negNum2 += '0'
    else:
        negNum2 += '1'
        counter = 0

    for i in range(1, len(negNum1)):
        if(int(negNum1[i]) + counter == 1):
            negNum2 += '1'
            counter = 0
        elif(int(negNum1[i]) + counter == 0):
            negNum2 += '0'
        else:
            counter = 1
            negNum2+= '0'
    print(negNum2[::-1])
num = int(input("enter a number\n"))
num = BinaryToDecimal(num)
Complement_2(num)