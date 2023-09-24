# Define a method greet(name) that prints a greeting message with the given name.
def greet(name):
    print("hello ", name)
    
name = input("enter your name: ")
greet(name)
# Define a method calculate_average(numbers) that calculates and returns the average of a list of numbers.
def average(a,b):
    return (a+b)/2

a = int(input("enter a number: "))
b = int(input("enter second number: "))
print(average(a,b))
# Define a method is_prime(num) that checks and returns whether a number is prime or not.
def prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if(num%i==0):
            return False
        
    return True

num = int(input("enter a number: "))
if print(num):
    print("The ",num," is prime number")
else :
    print("the ",num," is not prime number")
        

# Define a method reverse_string(s) that reverses and returns a given string.
def reversestring(name):
    print(name[::-1])

name = input("enter a string : ")
reversestring(name)