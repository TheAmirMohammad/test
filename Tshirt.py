sg = input()
s , g = sg.split(" ")
s , g = int(s) , int(g)

nsg = input()
ns , ng = nsg.split(" ")
ns , ng = int(ns) , int(ng)

if s>=ns and g>=ng :
    print("yes")
else:
    print("no")