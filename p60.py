#60 Compare two numbers using relational operators

num1 = 5
num2 = 3
result=''
for i in range(num1-num2):
    result+='>'
    break
print(num1,result,num2)

i=0
while i<num1-num2:
    result+='>'
    break
print(num1,result,num2)