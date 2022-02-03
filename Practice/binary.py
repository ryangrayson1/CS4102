num = int(input("Enter a positive int: "))
ret = ""

def convert(num):
    global ret
    while num != 0:
        if num % 2 == 0:
            ret += "0"
        else:
            ret += "1"

        num =  num // 2

    return ret[::-1]

print(convert(num))
