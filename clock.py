try :
    cl = input()
    h , m = cl.split(" ")

except ValueError:
    h = cl
    m = input()

h , m = int(h) , int(m)

newH = 12 - h
newM = 60 - m

if newH == 12 : newH = 0
if newM == 60 : newM = 0

print("{:0>2}:{:0>2}".format(newH , newM))