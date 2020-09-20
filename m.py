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
'''here we write a in the for a = qb +r
    and the while loop the new a becomes b and new b becomes remainder of a/b(a%b)
    the loop continues until the new b becomes zero ,the final a is the gcd(a,b)'''

