from random import randint,sample

s1={k:randint(3,6) for k in sample('abcdef',randint(1,5))}
s2={k:randint(3,6) for k in sample('abcdef',randint(1,5))}
s3={k:randint(3,6) for k in sample('abcdef',randint(1,5))}
print(s1)
print(s2)
print(s3)
# commet=[]
# for x in s1:
#     if x in s2 and x in s3:
#         commet.append(x)
# print(commet)

#方法二
k1=s1.keys()
k2=s2.keys()
k3=s3.keys()
commet1=k1&k2&k3
print(commet1)
