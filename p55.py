#55 Check if a number is prime
number=int(input('enter the number:'))
if number >=1:
    for i in range(2,int(number/2)+1):
        if number%i==0:
            print(number,'is not prime')
    else:
        print(number,'is prime')