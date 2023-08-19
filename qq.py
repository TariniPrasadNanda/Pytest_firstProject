# s="my name is chiku"
# # count=0
# # for x in s:
# #     if x=="i":
# #         count+=1
# #         if count==2:
# #             x="n"
# #
# #     print(x,end="")
# d=s.split()
# for i in d:
#     print(i[::-1],end=" ")

import random as r

ph_no = []


ph_no.append(r.randint(6, 9))


for i in range(1, 10):
    ph_no.append(r.randint(0, 9))


for i in ph_no:
    print(i, end="")