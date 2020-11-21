abcdm = input()
a , b , c , d , m = abcdm.split(" ")
a , b , c , d , m = int(a) , int(b) , int(c) , int(d) , int(m)

newA = m*c +a
newB = m*d +b

soodA = c*m
soodB = d*m

if newA>newB and soodA>soodB :
    print("Eyval baba!")
elif newA<newB and soodA<soodB :
    print("Eyval baba!")
else:
    print("Naaa, eshtebahe!")