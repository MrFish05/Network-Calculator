# Converts a decimal number into binary
def decimal_to_binary(decimal_number):
    number = int(decimal_number)
    res = ""

    while number != 0: 
        if number%2 != 0:
            res = "1"+res
        else:
            res = "0"+res

        number = int(number/2)

    return res

# Converts a binary number in 8 bit lenght if smaller
def eight_bit_binary(binary_number):
    res = binary_number

    while(len(res) < 8):
        res = "0"+res

    return res
        

# Converts a decimal ip address in a binary ip address
def decimal_ip_to_binary_ip(decimal_ip):
    ip = decimal_ip.split(".")
    res = ""
    x = 0

    for i in ip:
        if x != 3:
            res = res+eight_bit_binary(decimal_to_binary(i))+"."
            x = x+1
        else:
            res = res+eight_bit_binary(decimal_to_binary(i))
            x = x+1

    return res

# Makes the subnet from the CIDAR number in binary
def subnetmask_binary(cidar_number):
    res = "-1"
    if (cidar_number < 33 and cidar_number > 0):
        for x in range(4):
            for y in range(8):
                if(cidar_number!=0):
                    res=res+"1"
                    cidar_number-=1
                else:
                    res=res+"0"
            if(x<3):
                res=res+"."

    return res