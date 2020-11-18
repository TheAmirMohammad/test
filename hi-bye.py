n = int(input())
guys = input()

li = guys.split(" ")

for i in range(1 ,n):
    for j in range(i , 0 , -1):
        print(f"{li[i]}: salam {li[j-1]}!")

for i in range(n):
    print(f"{li[i]}: khodafez bacheha!")
    for j in range(i+1 , n):
        print(f"{li[j]}: khodafez {li[i]}!")