#def Counting_machine(count):
    #if int(count) == 0:
       #condition = True
    #else:
       #condition = False
    #while condition == True:
     #Count = int(count):
     #count = Count+1
     #if count == 101:
        #break
     #print(str(count))
    #else:
       #print("YOUR ENTERED DIGIT MUST BE ZERO.") 
#Run = Counting_machine(input("Enter number: "))
#print(Run)

#        LEVEL 8
#     STUDENTS LIST MANAGER
#   ========================
# Most likely to be transfered to github repository.
#def Students_list():
   #students = []
   #while True:
       #print("1. Add student name.")
       #print("2. Remove student name.")
       #print("3. Show student list.")
       #print("4. Show number of students in the list.")
       #print("5. Exit.")
       #choice = input("Enter your choice (1-5): ")
       #if choice == "1":
           #name = input("Enter student name: ")
           #students.append(name)
       #elif choice == "2":
           #name = input("Enter the student name to remove: ")
           #students.remove(name)
       #elif choice == "3":
            #print("Student list: ")
            #print(students)
       #elif choice == "4":
           #print(f"Number of students in the list: {len(students)}")
       #elif choice == "5":
           #print("Exiting the program.")
           #break
       #else:
            #print("Invalid choice. Please try again.")

#Run = Students_list()
#Run

#     PROJECT 26 HIGHEST AND LOWEST NUMBER FINDER
#    =============================================
#def Highest_and_Lowest():
   #numbers = []
   #print("Enter numbers one by one. Type 'done' when finished. ")
   #while True:
        #num = input("Enter a number (or 'done' to finish): ").strip()
        #if num.lower() == "done":
            #break
        
        #try:
            #number = float(num)
            #numbers.append(number)
        #except ValueError:
              #print("Invalid input. Please enter a valid number or 'done' to finish. ")
              #continue
   #if len(numbers) == 0:
      #print("No numbers were entered.")
      #return
   #print("the highest number is:", max(numbers))
   #print("the lowest number is:", min(numbers))
   #print(f"The total number of numbers entered is: {len(numbers)}")

#Run = Highest_and_Lowest()
#Run

#        Project 27
#     Shopping List Manager
#   ==========================
#import time
#def Shopping_List_Manager():
    #items_bought = []
    #print("Welcome to the Shopping List Manager1 ")
    #print("You can add items to your shopping list, remove items, view the list, or exit the program.")
    #print("1. Add item to shopping list.")
    #print("2. Remove item from shopping list.")
    #print("3. View shopping list.")
    #print("4. Total number of items in Shopping List.")
    #print("5. Exit the program.")
    #while True:
     #choice = input("Enter your choice (1-5): ").strip()
     #if choice == "1":
         #item = input("Enter item: ")
         #items_bought.append(item)
     #elif choice == "2":
        #item = input("Enter item: ")
        #items_bought.remove(item)
     #elif choice == "3":
        #if len(items_bought) == 0:
         #print("Shopping list is Empty")
        #print(f"Shopping List: {items_bought}")
     #elif choice == "4":
         #print(f"You have {len(items_bought)} in your Shopping list.")
     #elif choice == "5":
        #print("Exiting program...")
        #time.sleep(1)
        #break
     #else:
        #print("Invalid choice. Please try again.")

#Run = Shopping_List_Manager()
#Run


#items = [1,2,3,4,5,6]
#for index,item in enumerate(items):
      #print(index,item)

 #    INTRODUCTION TO CLASSES:
 #   =========================   
#class Animal:
   #def walk(self):
      #print("Walking...")

#class Dog(Animal):
    #def __init__(self, name, age):
      #self.name = name 
      #self.age = age
    #def bark(self):
        #print("woof!")

#roger = Dog("Roger",8)
#print(roger.name)
#print(roger.age)
#roger.bark()
#roger.walk()
#   This section will be completed in the final aspect of your training...

#        INTRODUCTION TO MODULES
#      ===========================
# Modules enable us access or run functions from other files already created in a folder
# Example:
#from lib.dog import bark
#bark()
# The import chatgptassignment_contd would import the function Calculator() from the file  chatgptassignment_contd.py and the Calculator() written below the import would run the function.
#from math import sqrt
#print(sqrt(4))

# Sys Module
#import sys

#name = sys.argv[1]

#print("Hello "+name)

# Argparse Module
#import argparse

#parser = argparse.ArgumentParser(
    #description = 'This program prints the name of my dogs'
#)
#parser.add_argument('-c','--color',metavar='color',
#required=True,choices={'red','yellow'}, help='the color to search for')

#args = parser.parse_args()

#print(args.color)

# The Lamda function
#lambda num: num * 2

#multiply = lambda a,b : a * b
#print(multiply(2,4))
# the Lambda function enables the user to define or customize operators or operations he or she can make use of .
#example 2:
#division = lambda a,b: a/b
#print(division(2,4))
#    NEXT TOPIC
#Map(),filter(), reduce()

#numbers = [1,2,3]

#double = lambda a: a * 2

#result = map(double,numbers)
#print(list(result))
# map enables you to create a new list from your original list by applying a function over each item in the list which will yield each output for the new list.
# you can also write it in this form:
#numbers = [1,2,3]
#result = map(lambda a: a * 2,numbers)
#print(list(result))

#def Greeting_message(name):
    #first_letter = name[0].upper()
    #Remainder = name[1:].lower()
    #name = first_letter + Remainder
    #return(f"Hello {name}, Welcome to the Python Programming Language.")

#count = 1
#while count <= 3:
    #Name = input("Enter your name: ")
    #Run = Greeting_message(Name)
    #print(Run)
def Calculator_Projectv3(integer1, integer2, operation):

    X = float(integer1)
    Y = float(integer2)

    add_numbers = lambda X, Y: X + Y
    subtract = lambda X, Y: X - Y
    multiply = lambda X, Y: X * Y
    divide = lambda X, Y: X / Y

    if operation == "add":
        return add_numbers(X, Y)

    elif operation == "subtract":
        return subtract(X, Y)

    elif operation == "multiply":
        return multiply(X, Y)

    elif operation == "divide":
        if Y == 0:
            return "Error: Division by zero is undefined."
        return divide(X, Y)

    else:
        return "Invalid operation. Choose add, subtract, multiply, or divide."


while True:

    integer1 = input("Enter first number: ")
    integer2 = input("Enter second number: ")

    operation = input(
        "Enter operation [add, subtract, multiply, divide]: "
    ).strip().lower()

    try:
        Run = Calculator_Projectv3(integer1, integer2, operation)
        print("Result:", Run)

    except ValueError:
        print("Please enter valid numbers.")

    choice = input("Perform another calculation? (yes/no): ").strip().lower()

    if choice != "yes":
        print("Calculator closed.")
        break