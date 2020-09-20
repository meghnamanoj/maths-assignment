'''euclids extended algorithm 
   expressing gcd in the form ax+by'''
a = input('a =')
b = input('b =')
a = int(a)
b= int(b)
if a<b:
    x = a
    a = b
    b = x
A = a
B = b
p = 0
q = 1
r = 1
s = 0
while a%b != 0:
    x =a//b
    aa = a
    bb = b
    pnew,qnew = p,q
    rnew,snew = r,s
    a = bb
    b = aa-x*bb
    r,s = pnew,qnew
    p,q = rnew - x*pnew,snew - x*qnew
print(p,q)
print(str(b),'=',str(p),'*',str(A),'+',str(q),'*',str(B))
'''Bezouts identity
    gcd(a,b)= ax+by
    the algorithm finds  x and y.
    Here 'a = bb and b = aa-x*bb 'these 2 functions finds the gcd and
    'r,s = pnew,qnew and p,q = rnew - x*pnew,snew - x*qnew ' finds the coeficient of a and b.
    the function 'rnew - x*pnew' finds the coefficient of a and 'snew - x*qnew' finds the coeficient
    of b.''' 
