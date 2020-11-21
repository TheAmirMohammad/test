n = int(input())
an = input()
jam = 0

an = (an.split(" "))

def isOdd(n):
    if n%2 == 0:
        return False
    else:
        return True

def count(i , n):
    return (n-i)*(i+1)

for i in range(n//2):
    n2 = n -1 -i
    tedad = count(i , n)
    # print(f"{i+1}&{n2+1} - {an[i]}&{an[n2]} - {tedad}")
    jam += tedad*(int(an[i])+int(an[n2]))
    # print(jam)

if isOdd(n):
    n2 = (n//2)
    tedad = count(n2 , n)
    # print(f"{n2} - {an[n2+1]} - {tedad}")
    jam = jam + tedad*int(an[n2])
    # print(jam)

print(jam)