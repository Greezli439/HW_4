#1
tuple_a = (1, 2, 3, 4, 5)
tuple_b = (4, 5, 6, 7, 8)
tuple_c = (4, 5, 6, 7, 8, 9, 10, 11)
tuple_d = tuple_a + tuple_b + tuple_c
print(f'{tuple_d=}')

#2
res = []
for i in tuple_d:
    if tuple_d.count(i) > 1:
        res.append((i, tuple_d.count(i)))
res = tuple(res)
print(f'{res=}')

#3
res = []
temporary = []
for i in tuple_d:
    if tuple_d.count(i) > 1:
        if i not in temporary:
            temporary.append(i)
            pn = []
            for j in range(len(tuple_d)):
                if i == tuple_d[j]:
                    pn.append(j)
            res.append((i,tuple(pn)))
del temporary
res = tuple(res)
print(f'{res=}')

