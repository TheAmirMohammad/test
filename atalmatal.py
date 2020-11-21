nk = input()
n , k = nk.split(" ")
n , k  = int(n) , int(k)


li = []
for i in range(n):
    for j in range(2):
        li.append(i+1)

p = 0
p2 = 0
c = 2*n-1
flag = 0
while c > 0 :
    c2 = k
    while c2 > 0:
        if li[p% len(li)] != 0:
            c2 -= 1
            print(li[p% len(li)] , end=" ")
        p = (p + 1) 
    li[(p-1)% len(li)] = 0
    c -= 1
    print('')
    if c == 1:
        for i in range(2*n):
            if li[i] != 0 and flag == 0:
                p2 = li[i]
                flag = 1
            elif li[i] != 0 and flag == 1:
                if p2 == li[i]:
                    print(f"winner:{li[i]}")
                    flag = 2
                c=0
                break
for i in range(2*n):
    if li[i] != 0 and flag != 2 :
        print(f"winner:{li[i]}")
        break