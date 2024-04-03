'''
#41 Print "Hello, World!"

input=()
message = "Hello, World!"
for i in message:
        print(i, end="")

'''
'''
#42 Calculate the sum of two numbers

num1 = 3
num2 = 5
sum_result = 0
for _ in range(num1):
    sum_result += 1
for _ in range(num2):
    sum_result += 1
print("The sum of", num1, "and", num2, "is:", sum_result)

'''
'''
#43 Find the type of a variable

variable = 42
variable_type = type(variable)
print("Type of the variable:", variable_type)

'''
'''
#44 Perform string concatenation

str1 = "Python"
str2 = "Programming"
result = ""
for char in str1:
    result += char
for char in str2:
    result += char
print("result:",result)

'''
'''
#45 List slicing

input_list = [1, 2, 3, 4, 5]
start_index = 2
end_index = 4
output_list = []
for i in range(start_index, end_index):
    output_list.append(input_list[i])
print(output_list)

'''
'''
#46 Find the maximum number in a list

input_list = [3, 1, 4, 1, 5, 9, 2]
max_number = input_list[0]
for i in input_list[1:]:
    if i > max_number:
        max_number = i
print("Input:", input_list)
print("Output:", max_number)

'''
'''
#47 Check if an element exists in a tuple

my_tuple=(1,2,3,4)
element_to_check=3
elements_exist=False
for i in my_tuple:
    if i == element_to_check:
        elements_exist=True
        break
print(elements_exist)

'''
'''
#48 Merge two dictionaries

dict1={'a': 1, 'b': 2}
dict2= {'c': 3, 'd': 4}
for keys, values in dict2.items():
    dict1[keys]=values
print("dict1:",dict1)

'''

'''
#49 Count occurrences of an element in a list

input = [1, 4, 2, 4, 5, 4, 1]
element_to_count=4
count=0
for i in input:
    if i ==element_to_count:
        count+=1
print(count)

'''
'''
#50 Create a set from a list
lst=[1,2,2,3,3,3]
output_set= set()
for i in lst:
    output_set.add(i)
print(output_set)

'''