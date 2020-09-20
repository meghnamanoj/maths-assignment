'''Code for finding gcd'''
a = input('a =')
b = input('b =')
if a<b:
    x = a
    a = b
    b = x
a = int(a)
b = int(b)
while b!= 0:
    a , b = b ,a%b
print(a)
