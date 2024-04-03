'''
#1 list reverse condition
list=[1,2,3,4,5]
print("list before reverse:",list)
list.reverse()
print("list after reverse:",list)

'''
'''
#1 list reverse using sort condition
lst = [1,2,3,4,5]
lst.sort(reverse=True)
print(lst)

'''

'''
#2 list of elements using for loop
list=(1,2,3,4,5)
count=0
for i in list:
    count=count+1
print('the length of list is:', count)

'''

'''
#2 list of elements using index
list=[1,2,3,4,5]
print("using index no:",list[4])

'''
'''
#3concatenate two lists using for loop
list1=[1,2,3]
list2=[4,5,6]
for lists in list2:
    list1+=[lists]
print(list1)
'''

'''
#3concatenate two lists 
list1=[1,2,3]
list2=[4,5,6]
print("new list3:",list1+list2)

'''
'''
#4 Intersection of two sets using loop
set1={1,2,3,}
set2={2,3,4}
set3=[]
for i in set1:
    if i in set2:
            set3.append(i)
print(set3)  
'''        

'''
#4 Intersection of two sets
set1={1,2,3}
set2={2,3,4}
print(set1.intersection(set2))

'''
'''
#5 Calculate Average numbers using for loop
input=[1,2,3,4,5,]
sum_num = 0
for i in input:
    sum_num = sum_num + i           
    avg = sum_num / len(input)
print(avg)
'''
'''
#5 Calculate average numbers
list=[1,2,3,4,5]
average=sum(list)/len(list)
print("Average list:",average)


'''
'''
#6 Removal of duplicates using for loop
x=[1,2,2,3,3]
y=[]
for i in x:
 if i not in y:
    y.append(i)
print("removed duplicate:",y)
'''

'''
#6 Remove duplicates
list1=[1,2,2,3,3,3]
temp=set(list1)
list1=list(temp)
print("new:", list1)

'''
'''
#7 Convert a list to a tuple using for loop
input = [1, 2, 3, 4, 5]
output = ()
for each in input:
    output += (each,) 
print(output)
'''
'''
#7 Convert list to tuple
x=[1,2,3,4,5]
x=tuple(x)
print(type(x),x)

'''
'''
#8 swap two variables using for loop
a=5
b=10
for i in range(1):
 print("a =", b)
 print("b =", a)

'''
'''
#8 swap two variables
a=5
b=10
temp=a
a=b
b=temp
print("value of a:",a)
print("value of b:",b)

'''
'''
#9 ASCII Value of a Character using ord
input_char='A'
 ord(input_char)
print("ASCII Value of a Character;",ord(input_char))

'''
'''
#9 ASCII Value of a Character using ord
input_char='A'
ord(input_char)
print("ASCII Value of a Character;",ord(input_char))

'''
'''
#10 Create a dictionary from two lists
list1=['a', 'b', 'c']
list2=[1, 2, 3]
list3={}
for i in range(len(list1)):
    list3.update({list1[i]:list2[i]})
print(list3)
'''

'''
#11 removing the 0th, 4th, and 5th elements using for loop
list1=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list2=[]
for i in range(len(list1)):
    if i==0 or i==4 or i==5:
        continue
    list2.append(list1[i])
print(list2)

'''