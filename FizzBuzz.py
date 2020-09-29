#Check desired output
#create array to return
#setup loop in range 1, n + 1
#set up if else block
#first step is to check if both multiples of 3 and 5
#else modulo 5
#else module 3
#else none

def fizzBuzz(n):
    array = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            array.append('FizzBuzz')
        elif i % 5 == 0:
            array.append("Buzz")
        elif i % 3 == 0:
            array.append("Fizz")
        else:
            array.append(str(i))
    return array

print(fizzBuzz(100))