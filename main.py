my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print(my_list)
x = 0
while 1 > 0:
    if my_list[x] >= 0:
        print(my_list[x])
        x += 1
        if my_list[x] == 0:
            del my_list[x]
        continue
    break
