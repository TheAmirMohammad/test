nks = input()
n , k , s = nks.split()
n , k , s = int(n) , float(k) , float(s)

need = n*k

if s >= need:
    print("Kafie!")
else:
    print("Na! yeki bayad bere sabzi bekhare")