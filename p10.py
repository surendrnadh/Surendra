#10 Create a dictionary from two lists
# list1=['a', 'b', 'c']
# list2=[1, 2, 3]
# list3={}
# for i in range(len(list1)):
#     list3.update({list1[i]:list2[i]})
# print(list3)

x1=['a', 'd,', 'f']
x2=[1,2,3]
x3={}
for i in range(len(x1)):
    x3.update({x1[i]:x2[i]})
print(x3)

#10 Create a dictionary from two lists unsing functions.

def Create_dictionary(list1,list2):
    result_dictionary={}
    for i in range(len(list1)):
        result_dictionary.update({list1[i]:list2[i]})
    return result_dictionary
list1=['a', 'b', 'c']
list2=[1, 2, 3]
result_dictionary=Create_dictionary(list1,list2)
print(result_dictionary)