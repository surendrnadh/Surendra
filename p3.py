#3concatenate two lists using for loop
# list1=[1,2,3]
# list2=[4,5,6]
# for lists in list2:
#     list1+=[lists]
# print(list1)

#3concatenate two lists using functions
def concatenation_lists(list1,list2):
            return list1+list2
list1=[1,2,3,4]
list2=[5,8,9,0,3]
output=concatenation_lists(list1,list2)
print(output)