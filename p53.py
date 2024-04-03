#53 Print the Fibonacci sequence up to n terms

input=7
Fibonacci_num=[0,1]
for i in range(2,input):
    Fibonacci_num.append(Fibonacci_num[i-1]+Fibonacci_num[i-2])
print(Fibonacci_num)