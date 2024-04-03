#11 removing the 0th, 4th, and 5th elements using for loop
list1=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list2=[]
for i in range(len(list1)):
    if i==0 or i==4 or i==5:
        continue
    
    list2.append(list1[i])
print(list2)

#11 removing the 0th, 4th, and 5th elements using functions

def remove_elements(list1):
    list2=[]
    for i in range(len(list1)):
        if i==0 or i==4 or i==5:
            continue
        list2.append(list1[i])
    return list2
list1=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list2=remove_elements(list1)
print(remove_elements(list1))