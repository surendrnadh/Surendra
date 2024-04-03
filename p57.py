#57 Use the modulo operator to check for even numbers
number=int(input('enter the number:'))
# if number >=1:
for i in range(2,int(number/2)+1):
    if number%i==0:
        print(number,'is even')
        break
else:
     print(number,'is not even')