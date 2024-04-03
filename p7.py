#7 Convert a list to a tuple using for loop
input = [1, 2, 3, 4, 5]
output = ()
for each in input:
    output += (each,) 
print(output)

#7 Convert a list to a tuple using functions

def Convert(list):
    tuple=()
    for i in list:
        tuple+=(i,)
    return tuple
list=[1, 2, 3, 4, 5]
print(Convert(list))
list=['kitkat','milkybar','munch','perk','cadbery']
tuple=Convert(list)
print(tuple)