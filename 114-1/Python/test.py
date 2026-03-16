while 1:
    l = int(input())
    if l <= 0:
        break

    tokens = input().split(' ')[:3]
    s = ""
    for y in range(2*l-1):
        for x in range(2*l-1):
            center = l
            dy = abs(l-1 - y)
            dx = abs(l-1 - x)
            c = dx+dy
            s += f"{tokens[(dx if dx >= dy else dy)  % 3]}{'' if x == 2*l-2 else ' '}"
        s+="\n"
    print(s)

#
# def q2():
#     text = "Learn Python. Python is a popular programming language. Python can be used on a server to create web applications. Start learning Python now."
#     for k, v in {k:text.count(k) for k in sorted(filter(lambda x: 65 < ord(x)  <= 90 or 97 < ord(x) <= 122, text))}.items():
#         print(f"{k}: ", "*"*v)
# q2()
#
#
#








