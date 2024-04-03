#4 Intersection of two sets using loop
# set1={1,2,3,}
# set2={2,3,4}
# set3=[]
# for i in set1:
#     if i in set2:
#             set3.append(i)
# print(set3)

#4 Intersection of two sets using functions

def intersection(set1,set2):
    return set1&set2
set1={1,2,3,4,5}
set2={2,5,6,7,3}
output=intersection(set1,set2)
print(output)
