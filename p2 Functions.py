#2 list of elements using for loop
# list=(1,2,3,4,5)
# count=0
# for i in list:
#     count=count+1
# print('the length of list is:', count)

#2 list of elements using functions

def length(my_list):
    size=0
    for i in my_list:
        if isinstance(i,list):
            size+=length(i)
        else:
            size+=1
    return size
my_list=[1,2,3,4,5,8,9,0,4]
print(length(my_list))
my_list=['apple','call','suri','length','size','roja']
print(length(my_list))