import random
pass
i8K3X@V@X7x

n=2
alpha="abcdefghijklmnopqrstuvwxyz"
l=[i for i in range(1,n+1) if i//2!=0]

string=""
print(l)
if n in l:
    string=alpha[random.randint(0,25)]*n
else:
    t=n//2
    string=(t-1)*alpha[random.randint(0,25)]+(t+1)*alpha[random.randint(0,25)]
print(string)



