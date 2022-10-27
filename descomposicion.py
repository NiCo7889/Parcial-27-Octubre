num = input("Tu número: ")
if len(num) != 4:
    print("Tu número no es válido")
else:
    for c in range(3, -1, -1):
        res = num[c]
        if c == 0:
            n ="1000"
            m = n.replace("1", res)
            print(m)
        elif c == 1:
            n ="0100"
            m = n.replace("1", res)
            print(m)
        elif c == 2:
            n ="0010"
            m = n.replace("1", res)
            print(m)
        elif c == 3:
            n ="0001"
            m = n.replace("1", res)
            print(m)
