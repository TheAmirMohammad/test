mn = input()
n , m = mn.split(" ")
n , m = int(n) , int(m)

g1 , g2 = 0 , 0

def gooshtCount(x):
    goosht = 0
    for i in range(len(x)):
        if x[i] == "*":
            goosht += 1
    return goosht

for i in range(n):
    zarf = input()
    g1 += gooshtCount(zarf)
    
for i in range(n):
    zarf = input()
    g2 += gooshtCount(zarf)

print(f"{g1} {g2}")