v = input()
li =[]

for i in range(len(v)):
    li.append(v[i])

for i in range(len(li)):
    for j in range(i+1):
        print(li[i] , end="")
    for j in range(i+1 , len(li)):
        print(li[j] , end="")
    print()