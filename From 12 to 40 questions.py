'''
#12 Difference between two list

list1=[1,2,3,4]
list2=[1,2]
list3=[]
for i in list1:
    if i not in list2:
        list3.append(i)
print(list3)

'''
'''
#13 second samllest number in list using for loop

list=[1,0.5,2,3,4,5]
smallest=min(list[0],list[1])
second_smallest=max(list[0],list[1])
for x in list:
    if x<smallest:
        second_smallest=smallest
        smallest=x
    elif x<second_smallest and x!=smallest:
        second_smallest=x
print("second_smallest:",second_smallest)

'''
'''
#14 unique vales from a list using for loop

lst=[1,2,3,4,5,5,6,6,6]
unique_values=[]
for i in lst:
    if i not in unique_values:
        unique_values.append(i)
print(unique_values)

'''
'''
#15 Check if a list is empty or not using for loop

lst=[]
is_empty=(True)
for i in lst:
    is_empty=False
    break
print('is_empty:',True)

'''
'''
#16 copy or clone a list

lst1 = {1, 2.2, "s,u,r,i", 4, 5}
lst2 = []
for i in lst1:
    lst2.append(i)
print("lst2:",lst2)

'''
'''
#17 list of words that are longer than n in a given words using for loop

lst= ['hello', 'world', 'name', 'python', 'programming']
lst2=[]
n=4
for i in lst:
    if len(lst)>n:
        lst.append(i)
    print("lst2:", lst2)

'''
'''
#17 list of words that are longer than n in a given words using for loop

input = ['hello', 'world', 'name', 'python', 'programming']
n = 4
output = []
index = 0
for i in range(len(input)):
    temp = input[i]
    if n < len(temp):
        output.append(temp[i])
print(output)
'''
'''

#18 Flatten a shallow list using for loop

lst1=[[1, 2, 3], [4.3, 5], ["suri"]]
lst2=[]
for i in lst1:
    for j in i:
        lst2.append(j)
        print('lst2:',lst2)
'''
'''
#19 Append a list to the second list using for loop

lst1=[1, 2, 3],[4, 5, 6]
lst2=[]
for i in lst1:
    for j in i:
        lst2.append(j)
    print("lst2:",lst2)
'''
'''
#20 Find the index of an item in a specified list.

lst=[1,2,3,4,5]
lst.index(4)
print("The index of 4 in the list:",lst.index(4))

'''
'''
#21 Check whether two lists are circularly identical using for loop.

lst1= [1, 2, 3, 4]
lst2=[2, 3, 4, 1]
for each in lst1:
    if each not in lst2:
        print("False")
        break
else:
    print("True")
'''
'''
#22 second largest number in list using for loop

list=[1, 3, 4, 5, 0, 2]
max=list[0]
second_largest=list[0]
for x in list:
    if x>max:
        second_largest=max
        max=x
    elif x>second_largest and x<max:
        second_largest=x
print("second_largest:",second_largest)

'''

'''
#23 concatenating a list which range goes from 1 to n using for loop

lst1= ['p', 'q']
n = 3
lst2 = []
for i in range(1, n + 1):
    for item in lst1:
        lst2.append(item + str(i))
print("lst2:",lst2)

#out put= ['p1', 'q1', 'p2', 'q2', 'p3', 'q3']

'''
'''
#24 Get the frequency of the elements in a list using for loop

lst = [1, 2, 2, 3, 4, 4, 4]
frequency_dict = {}
for i in lst:
    if i in frequency_dict:
        frequency_dict[i]+=1
    else:
        frequency_dict[i]=1
        print("frequency_dict:",frequency_dict)

'''
'''
#25 list contains a sublist using for loop in python
# lst=[2,4,3,5,7]
# sub_list=[4,3]
# for i in range(len(lst) - len(sub_list) + 1):
#         if lst[i:i+len(sub_list)] == sub_list:
#             result = lst(lst, sub_list)
# print(result)

#25 list contains a sublist using functions in python
# main_list = [2, 4, 3, 5, 7]
# sub_list = [4, 3]
# def is_sublist(main_list, sub_list):
#     for i in range(len(main_list) - len(sub_list) + 1):
#         if main_list[i:i+len(sub_list)] == sub_list:
#             return True
#     return False
# result = is_sublist(main_list, sub_list)
# print(result)
'''

'''
#26 all permutations of a list using loops

input_list = [1, 2, 3]
output = []
for i in input_list:
    for j in input_list:
        if i != j:
            for k in input_list:
                if k != i and k != j:
                    output.append((i, j, k))
print(output)
'''
'''
#27 difference between two lists using for loop

lst1 = [1, 2, 3, 4]
lst2 = [2, 3]
lst3 = []
for i in lst1:
    if i not in lst2:
        lst3.append(i)
        print("lst3:",lst3)

'''      
'''
#27 difference between two lists 

list1 = [1, 2, 3, 4]
list2 = [2, 3]
output = []
for item in list1:
    found = False
    for item2 in list2:
        if item == item2:
            found = True
            break
    if not found:
        output.append(item)
print(output)
'''
'''
# 28 list of characters into a string using loops

lst = ['P', 'y', 't', 'h', 'o', 'n']
string = ''
for char in lst:
    string += char
print("string:", string)

'''
'''
#29 The index of an item in a specified list using loop

lst=[10, 20, 30, 40, 50]
search_item = 40
for i in range(len(lst)):
     if lst[i] == search_item:
        print("search_item:",search_item)

'''
'''
#30 Flatten a list without using recursion using for loop

lst = [[1, 2], [3, 4], [5, 6]]
output = []
for i in lst:
    for j in i:
        output.append(j)
        print("output:",output)
'''
'''
#31 Create and display all combinations of letters, selecting each letter from a different set using for loop

lst1={'1': ['a', 'b'], '2': ['c', 'd']}
lst2=[]
for i in lst1['1']:
    for j in lst1['2']:
        combination = i+j
        lst2.append(combination)
        print("lst2:",lst2)
'''

'''
#32 Initialize a list to store the top 3 values using for loop

input_dict = {'a': 27, 'b': 15, 'c': 4, 'd': 32, 'e': 3,'f':82}
top_values = []
for key, value in input_dict.items():
    for i in range(min(3, len(top_values))):
        if value > top_values[i]:
            top_values.insert(i, value)
            top_values = top_values[:6]
            break
    else:
        top_values.append(value)
print("top_values:",top_values)

'''
'''
#33 Combine values in a Python list of dictionaries

lst = [{1: 10}, {2: 20}, {3: 30}]
output_dict = {}
for i in lst:
    for j, k in i.items():
        output_dict[j] = k
print(output_dict)

'''
'''
#34 Create a dictionary from a string

input_string = "w3resource"
char_count = {}
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print("char_count:",char_count)

'''
'''
#35 Print a dictionary in table format using for loop

input = {1: ["Sam", 21], 2: ["Bob", 25], 3: ["Cara", 30]}
# Print the table header
print("ID  Name  Age")
for key, values in input.items():
    print(f"{key}   {values[0]}   {values[1]}")

'''
'''
#36 Count the values associated with a key in a dictionary

input  = {'A': [1, 2, 3], 'B': [4, 5], 'C': [6]}
output = {}
for i, int in input.items():
    output[i] = len(int)
print("output:",output)

'''
'''
#37 Convert a list into a nested dictionary of keys.

lst = [1, 2, 3, 4]
nested_dict = {}
temp = nested_dict
for i in lst:
    temp[i] = {}
    temp = temp[i]
print("nested_dict:", nested_dict )

'''
'''
#38 Sort a list alphabetically in a dictionary

lst = {'n1': ['c', 'b', 'a'], 'n2': ['e', 'd']}
output = {}
for i, j in lst.items():
    sorted_list = sorted(j)
    output[i] = sorted_list
print("output:", output)

'''

'''
#39 Remove spaces from dictionary keys

input = {"a b": 1, "c d": 2, "e f": 3}
output = {}
for i, j in input.items():
    output[i.replace(' ', '')] = j
print(output)

'''

#40 Get the top three items in a shop

input = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
output = []
sorted_items = sorted(input.items(), key=lambda x: x[1])
for i in range(3):
    output.append(sorted_items[i][0])
print("output:", output)

