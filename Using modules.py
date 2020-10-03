cookbook = int(input("What recipe would you like to make? (Please state the number)\n"))
if cookbook == 1:
    import mymodule as mx
    mx.greeting("Nana")

    a = mx.person1["age"]
    print(a)

    mx.omin(2)

    mx.tmin(4)

    mx.cmin(10)

    mx.smallest(0)
else:
    print("Updates pending")


