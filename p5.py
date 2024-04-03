# #5 Calculate Average numbers using for loop
# input=[1,2,3,4,5,]
# sum_num = 0
# for i in input:
#     sum_num = sum_num + i           
#     avg = sum_num / len(input)
# print(avg)

#5 Calculate Average numbers using functions

def Average(input):
    sum_num = 0
    avg=1
    for i in input:
        sum_num = sum_num + i           
        avg = sum_num / len(input)
    return avg
input=[1,2,3,4,5,]
print(Average(input))
input=[41,18,9,3,85,97]
print(Average(input))

