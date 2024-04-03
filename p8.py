#8 swap two variables using for loop
a=5
b=10
for i in range(1):
 print("a =", b)
 print("b =", a)

 #8 swap two variables using functions

 def swapping(a,b):
    print('before swapping of two numbers:(',a,',',b,')')
    a,b=b,a
    return a,b
result=swapping(a=2,b=3)
print('after swapping of two numbers:',result)
result=swapping('x','suri')
print('after swapping of two numbers:',result)