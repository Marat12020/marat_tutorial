a=1
b=-2
c=-3
D=b**2-(4*a*c)
print(D)
count=0
if D==0:
    count=1
if D>0:
    count=2
print(count)
k=1
for i in range(count):
    x=(-b+k*D**0.5)/a
    k=-k
    print(x)
