# Write a program that adds two numbers and prints the result.
def add(a,b):
    return a+b

a = int(input())
b = int(input())
print(add(a,b))
# Write a program that calculates the square of a number and prints the result.
def square(num):
    return num**2

num = int(input())
print("the square of the number is: ",square(num))
#Write a program that calculates the area of a circle given its radius and prints the result.
def area(radius):
    return (3.14)*radius**2

radius = int(input("enter radius: "))
print("the area of the number is: ",area(radius))
# Write a program that converts Celsius to Fahrenheit and vice versa based on user input
def celTOfar(celci):
    return (celci*9/5)+32
def fartocel(fahren):
    return (fahren*-32)*5/9

choice =int(input("Enter 1 for celcius change and 2 for fahrenhiet: "))
if choice==1:
    celci = int(input("Enter celcius: "))
    print(celTOfar(celci))
elif choice ==2:
    fahren = int(input("Enter fahren: "))
    print(fartocel(fahren))
#Write a program that calculates the simple interest using the formula: 
def simpleInterest(p,r,t):
    SI = (p*r*t)/100
    return SI

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))

print(simpleInterest(principal,rate,time))
# tell given input is four digit number or not 
n = int (input("Enter a number"))
if n>999:
    print("Yes the number is four digit number")
else:
    print("no it is not four digit number")