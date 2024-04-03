'''
#1 list reverse condition
list=[1,2,3,4,5]
print("list before reverse:",list)
list.reverse()
print("list after reverse:",list)

'''

#1 list reverse condition using functions.

def reverse(my_list):
    new_list=[]
    for values in reversed(my_list):
        new_list.append(values)
    return new_list
my_list=[1,2,3,4,5]
print(reverse(my_list))
