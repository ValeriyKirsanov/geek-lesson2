a = list(input(' введите значение'))
b = int(len(a))
print(b)
if b%2 == 0 :
    a[: :2], a[1 : :2] = a[1 : :2], a[: :2]
    #print(a)
    print(''.join([str(i) for i in a]))
else :
    b = list(a)

    c_revers = b [::-1]
    s = (c_revers[0])
    #print(s)
    b.pop(-1)
    #print(b)

    b[: :2], b[1 : :2] = b[1 : :2], b[: :2]
    #print(b)
    print((''.join([str(i) for i in b])) + (s))