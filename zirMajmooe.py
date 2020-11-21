def f(number,n):
    if number != 0 :
        print("{" , str(number).replace("", " ")[1: -1] , "}")
        if(number%10==n):
            f(number//10,n)
        else:
            if len(str(number)) != 1:
                newnumber = f1(number,n)
                f(newnumber,n)
def f1(number,n):
    s = 0
    j = n-number%10-1
    k = j
    for i in range(number%10+1,n+1):
        s += i*(10**j)
        j -= 1
    
    result = str(number//(10)) + str(s)
    return int(result)
n = int(input())
x=n
for j in range(1 , n+1):
    a = ''
    for i in range(j,x+1):
        a += str(i)
    # print(a)
    f(int(a),n)

print("{ }")