# Write a program that prints the numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)
# Write a program that prints even numbers from 2 to 20 using a for loop and an if statement.
for i in range(2,21):
    if i%2==0:
        print(i)
# Write a program that prints the multiplication table of a given number using a for loop.
x = int(input("Enter a number whose table you want : "))
for i in range(1,11):
    print(x," * ",i," = ",x*i)
# Write a program that prints whether a given number is even or odd using if-else statements.
x = int(input("Enter a number: "))
if x%2==0:
    print("number is even ")
else:
    print("number is odd")
# Write a program that prints the factorial of a given number using a for loop.
x=  int(input("enter a number whose factorial you want : "))
fact = 1
for i in range(1,x+1):
    fact = fact * i
print(fact)  
