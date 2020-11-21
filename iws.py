temp = int(input())

if temp > 100:
    print("Steam")
elif temp >= 0:
    print("Water")
elif temp >= -273:
    print("Ice")
else:
    print()