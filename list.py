#Create an empty list called my_list.
my_list = []
print(my_list)
#Add the numbers 1, 2, 3, and 4 to my_list
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
print(my_list)
# Retrieve and print the element at index 2.
print("Element at index 2",my_list[2])
#Change the element at index 1 to 5.
my_list[1] = 5
print(my_list)
#Remove the element at index 3
my_list.pop(3)
print(my_list)
#Print the length of my_list.
print("The length of my list is ",len(my_list))
#Check if 3 is in my_list and print the result
if 3 in my_list:
    print ("yes 3 is in my list")
print("checking element in the list",3 in my_list)
#Create a list of fruits called fruits_list with at least 5 different fruits.
fruits_list = ["apple","banana","mango","kiwi","orange"]
#Add a new fruit, 'banana', to the end of the list
fruits_list.append("banana")
print("The extended list is ",fruits_list)
# Insert 'apple' at index 1
fruits_list.insert(1,"apple")
print("The extended list is ",fruits_list)
## Remove 'orange' from the list.
if 'orange' in fruits_list:
    fruits_list.remove("orange")
print("The extended list is ",fruits_list)
## Check how many times 'apple' appears in the list.
print(fruits_list.count("apple"))
# Reverse the order of the elements in the list.
fruits_list.reverse()  
print(fruits_list) 
# Sort the list in alphabetical order (if the elements are strings).
fruits_list.sort()
print("this is sorted list in alphabetical order",fruits_list)
# Print the updated fruits_list and the count of 'apple'.
print("The count of apples in the list is ",fruits_list.count("apple"))
#Create a list of 10 numbers (e.g., 0, 1, 2, ..., 9) called numbers_list.
numbers_list = [0,1,2,3,4,5,6,7,8,9]
#Print the first 5 elements of numbers_list.
print("The first five elemnts of the number list are ",numbers_list[0:5])
#Print the last 3 elements of numbers_list.
print("The last three elemnts of the number list are ",numbers_list[7:10])
#Print every second element from numbers_list.
print("The every second elemnts of the number list are ",numbers_list[1:10:2])
#Print the elements from index 2 to index 7 (inclusive).
print("The every second elemnts of the number list are ",numbers_list[2:8])
#Print the elements in reverse order using slicing.
print("The every second elemnts of the number list are ",numbers_list[::-1])
#Create an empty tuple called my_tuple.
my_tuple = ()
# Create a tuple called single_item_tuple with a single item of your choice.
single_item_tuple = ("dhruv")
# Create a tuple called fruits_tuple with at least 5 different fruits.
fruits_tuple = ("apple","banana","orange","pomegranate","papaya")
# Retrieve and print the third item from fruits_tuple.
print("The third fruit listed on fruit tuple is = ",fruits_tuple[2])
# Check if 'banana' is in fruits_tuple and print the result.
print("banana" in fruits_tuple)
# Concatenate fruits_tuple with a tuple containing three more fruits.
tup = ("guava","litchi","lemon")
fruits = list(fruits_tuple)
fruits = fruits_tuple + tup
fruits_tuple = tuple(fruits)
print(fruits_tuple)
# Create a new tuple numbers_tuple with 5 numbers of your choice.
numbers_tuple = (1,2,3,4,5)
# Retrieve and print the last 3 items from numbers_tuple.
print(numbers_tuple[-3:])
# Check if 10 is in numbers_tuple and print the result.
print(10 in numbers_tuple)
# Create a new tuple by combining fruits_tuple and numbers_tuple.
new_tuple = numbers_tuple + fruits_tuple
print(new_tuple)
