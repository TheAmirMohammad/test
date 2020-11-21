pd = input()

p , d = pd.split(" ")
p , d = int(p) , int(d)

for i in range(1 , p+1 ):
    x = i*d % p
    if x>=0 and x<=p/2 :
        print(i*d)
        break