def  gcd(a, b):
    reminder = a
    while reminder != 0:
        new = a % b
        if new == 0:
            reminder = 0
        else:
            a = b
            b = new
    return b

if __name__=='__main__':
print(gcd(8, 40))
