mylar = float(input("Emter the number to test: "))

if (mylar>=50) and (mylar==60) and (mylar<=70):
    if mylar > 65:
        print("High")
    elif mylar < 65 and mylar > 55:
        print("Medium")
    else:
        print("Low")
else:
    print("Equal")