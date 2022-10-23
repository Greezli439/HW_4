#1
list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]
list_f = [9, 3, 4, 1, 8, 6, 5, 2, 0, 7]
list_c = list_a + list_b
print(f'ex_1: {list_c=}')
print()

#2
list_c_1 = []
if len(list_a) == len(list_b):
    for i in range(len(list_a)):
        list_c_1.append(list_a[i])
        list_c_1.append(list_b[i])
print(f'ex_2: {list_c_1=}')
print()

#3
list_c_a, list_c_b = [], []
for i in list_a:
    if i % 2 == 0:
        list_c_a.append(i)
for i in list_b:
    if i % 2 == 1:
        list_c_b.append(i)
print(f'ex_3: {list_c_a=}')
print(f'ex_3: {list_c_b=}')
print()

#4
list_d = list_c[:]
list_d.reverse()
print(f'ex_4: {list_d=}')
print()

#5
res = []
for i in range(len(list_d)):
    res.append(list_d[i] + list_c[i])
print(f'ex_5: {res=}')
print()

#6
list_f1 = []
for i in list_f:
    list_f1.append(i + 1)
res1, res2 = list_f1[:], list_f1[:]
res1.sort()
res2.sort(reverse = True)
print(f'ex_6: {res1=}')
print(f'ex_6: {res2=}')
print()

#7
res = []
for i in range(len(list_d)):
    res.append((list_c[i], list_d[i]))
print(f'ex_7: {res=}')