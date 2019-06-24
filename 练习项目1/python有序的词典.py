# -*- coding=utf-8 -*-
from collections import OrderedDict

d = OrderedDict()
f = {}
l = [i for i in range(10)]

for x in "ABCDEFGHIJ":
    #
    i = l.pop()
    d[x] = i

    f[x] = i
print(type(d))
print(d)
print('-----------------------------')
print(type(f))
print(f)