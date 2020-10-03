a = int(input("Enter a number: "))
b = int(input("Enter a different number: "))
c = int(input("Enter a different number: "))

if a > b:
    boolean1 = "true"
    if a > c:
        boolean2 = "true"
        print(a)
    else:
        print(b)
else:
    if b > c:
        print(c)    
    else:
        print(b)
