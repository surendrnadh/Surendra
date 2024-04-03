#6 Removal of duplicates using for loop
x=[1,2,2,3,3]
y=[]
for i in x:
 if i not in y:
    y.append(i)
print("removed duplicate:",y)


#6 Removal of duplicates using Functions

def duplicates(my_list):
    result_list=[]
    for i in my_list:
        if i not in result_list:
            result_list.append(i)
    return result_list
my_list=[1,2,2,3,3]
duplicates_list=duplicates(my_list)
print("removed duplicate:",duplicates_list)
my_list=['s','u','r','e','n','d','r','a']
duplicates_list=duplicates(my_list)
print("removed duplicate:",duplicates_list)