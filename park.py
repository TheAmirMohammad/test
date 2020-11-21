xy = input()
xy1 = input()

x , y = xy.split(" ")
x1 , y1 = xy1.split(" ")

if int(x1) - int(x) >= 0:
    print("Right")
else:
    print("Left")