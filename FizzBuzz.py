#Check desired output
#create array to return
#set up if else block
#first step is to check if both multiples of 3 and 5
#else modulo 5
#else module 3
#else none

def fizzBuzz(n):
    array = []
    if n % 3 == 0 and n % 5 == 0:
        array.append('FizzBuzz')
    elif n % 5 == 0:
        array.append("Buzz")
    elif n % 3 == 0:
        array.append("Fizz")
    else:
        array.append(str(n))
    return array

print(fizzBuzz(15))