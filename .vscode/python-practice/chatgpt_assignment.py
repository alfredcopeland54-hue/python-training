#Number 1
#def person(name,age,school,course):
 #   print(name)
 #   print(school)
 #   print(course)
 #   print(int(age))

#person(input("Type in your name here: "),input("How old are you? "),input("Where did you receive your tertiary education? "), input("What course did you study? "))

#Number 2
#a=10
#b=20
#count1= a+10
#count2 = b-10
#print(count1)
#print(count2)

#Number 3
#def Calculator(x,y):
   # x = float(x)
   # y = float(y)
   # print(x+y)
   # print(x-y)
   # print(x*y)
   # print(x/y)

# Calculator(input("Type in x value: "),input("Type in y value: "))

#Number 4
#def User(First_name,Last_name):
  #cap1=First_name[:1].upper()
  #cap2=Last_name[:1].upper()
  #cap1ii=First_name[1:10].lower()
  #cap2ii=Last_name[1:10].lower()
  
  #First_name=cap1+cap1ii
  #Last_name=cap2+cap2ii
  
  #print(First_name+" "+Last_name)
  


#User(input("Type in your First name: "),input("Type in your Last name: "))

#Number 5
#def player(word):
   # print(len(word))
   # print(word[:1])
    #ttl=int(len(word))
   # ttl1=ttl-1
    #print(word[ttl1:ttl])
    #print(word.upper())
    #print(word.lower())

#player(input("What is your response? "))

#Number 6  
#def username(firstname,lastname,year,age):
    #ttl=len(firstname+lastname)
    #name=firstname+lastname
    #year = str(year)
    #age = str(age)
    #ffl=firstname[:1]
    #ffl1=name[1:ttl]
    #name_1 = ffl.upper()+ffl1.lower()
    #checkage = 2026 - int(year)
    #if checkage == int(age):
       #print(name_1+year+"/"+age)
    #else:
       #print("Inconsistency in inputed data")
    #if int(year)>2026:
       #print("You are currently in the year 2026.")




#username(input("Type in your First name here: "),input("Type in your Lastname here: "),input("Your Date of Birth: "),input("Your age: "))

#Number 7
#def user(birthyear):
    #if int(birthyear)>2026:
        #return("This is currently the year 2026")
    #if int(birthyear)== 2026:
       #userage = str(2026-int(birthyear))
        #return"How are you even typing this?"+"\n"+"You are "+userage+" years old."+" Just a couple of months old"
    #if int(birthyear) < 2026:
    # userage = str(2026-int(birthyear))
    #return("You are currently "+ userage +" years old.")
  

#Run=user(input("Your birth year: "))
#print(Run)

#Number 8
#def Shopping_calculator(item_price,quantity):
    #itm = int(item_price) 
    #qnt = int(quantity)
    #Total_cost = itm*qnt
    #Totalcost=str(Total_cost)
    #return("The total cost is "+"$"+Totalcost)

#Run = Shopping_calculator( input("Item price: "),input("Quantity: "))
#print(Run)

#Number 9
#def Temperature(temp_deg_celsius):
    #temp=float(temp_deg_celsius)
    #Temp_in_Fahrenheit = ((9/5)*temp)+32
    #Converted_temp = str(Temp_in_Fahrenheit)
    #return("That is "+Converted_temp+"F")

#Run = Temperature(input("Type in the temperature value in degree celsius: "))
#print(Run)

#Number 10
#def Number_Analyzer(integer):
    
    #while True:
      #if integer=="Start":
       #User_input = input("Type in integer value: ")
       #X = int(User_input)
       #print(X^2)
       #print(X^3)
       #print(X/2)
       #print(X*2)
       #Y = int(input("Give a divisor: "))
       #remainder = (X % Y)
       #print(remainder)
      #else:
        #print("Type in ""Start""")
        #integer = input()

#Number_Analyzer(input())

#Number 11
#def Number_Analyzer2(integer):
    #while True:
     #if integer == "Start":
       #print("Starting...")
      
       #User_input = input("Type in integer value: ")
       #User_input2 = input("Give a divisor: ")
       #X = int(User_input)
       #Y = int(User_input2)
       #print(X/Y)
       #print(X//Y)
       #print(X%Y)
     #else:
      #print("Type in 'Start'")
      #integer = input()

#Run= Number_Analyzer2(input("Type in 'Start': "))
#print(Run)

#Number 12
#import time
#def Age_checker( begin):
 #while True:
    #if begin =="Start":
         #print("Starting...")
         #time.sleep(2)
         #age = input(" Type in your age: ")
         #if int(age) < 13:
           #print(" You are below the age of 13. You are not allowed to use this app.")
         #if int(age)>17:
           #print("You are above 17. You are beyond the required age range.")
         #if 13<=int(age)<=17:
           #print("You are in the required age range.")
           #time.sleep(2)
           #print("Validation in progress...")
           #time.sleep(2)
           #print("please wait...")
           #time.sleep(3)
           #print ("Validation complete")
           #time.sleep(2)
           #print("Welcome.")
           #print("Type in Start")
         #begin = input()
    #else:
     #print("Type in 'Start'.")
     #begin = input()

#Run = Age_checker(input())
#print(Run)

#Number 13
#def Even_odd_numbers(begin):
    #while True:
      #if begin == "Start":
        #print("Type in integer ")
        #integer = int(input())
        #if integer % 2 == 0:
            #print("The integer is even ")
        #else:
             #print("The integer is odd ")
      #else:
         #print("Type in 'Start'")
         #begin = input()

#Run = Even_odd_numbers(input("Type in 'Start' "))
#print(Run)

#Number 14
##def Number_comparison(X,Y):

    #while True:
     
      #if float(X)-float(Y)>0:
            #print(str(X)+" is greater than "+str(Y))
      #if float(Y)-float(X)>0:
            #print(str(Y)+" is greater than "+str(X))
      #if float(X)-float(Y) == 0:
            #print("The values are equal.")
      #else:
            #print("The values are not equal.")
      #if float(X)%float(Y) == 0:
            #print(str(X)+" is divisible by "+str(Y))
      #else:
            #print(str(X)+" is not divisible by "+str(Y))
                
      #X = input("Lets try again with another X value: ")
      #Y = input("Lets try again with another Y value: ")
    





#Number_comparison(input("Input your desired X value: "),input("Input your desired Y value: "))

#Number 15
#import time
#def User(username,password):
    #while True:
        #X = username
        #Y = password
        #print("Confirm username and passowrd")
        #confirmX = input ("Retype username:  ")
        #confirmY = input ("Retype password : ")
        #if X == confirmX and Y == confirmY:
            #print("Login complete") 
        #else:
            #print("Incorrect username or password")
            #time.sleep(2)
        #username = input("Type in username: ")
        #password = input("Type in password: ")

#Run = User(input("Type in username: "),input("Type in password: "))
#print(Run)

#Number 16: Calculator gives output for only single row of record data taken in:
#def Calculator(Subject,score):
 #while True:
    #if Subject.isdigit() == False or score.isdigit() == True:
     #X = float(score)
     #first_letter = Subject[:1].upper()
     #remainder = Subject[1:len(Subject)].lower()
     #subject = first_letter + remainder
     #if X>100:
        #print("INPUTED SCORE IS ABOVE 100. PLEASE RECHECK SCORE.")
     #if 70<=X<=100:
        #grade = "A"
        #print(subject+": "+"Score: "+str(X)+" Grade: "+grade)
     #if 60<=X<=69:
        #grade = "B"
        #print(subject+": "+"Score: "+str(X)+" Grade: "+grade)
     #if 50<=X<= 59:
        #grade = "C"
        #print(subject+": "+"Score: "+str(X)+" Grade: "+grade)
     #if 45<=X<=49:
        #grade = "D"
        #print(subject+": "+"Score: "+str(X)+" Grade: "+grade)
     #if 0<=X<=39:
        #grade = "F"
        #print(subject+": "+"Score: "+str(X)+" Grade: "+grade)
     #if X<0:
        #print("INPUTED SCORE IS BELOW ZERO. PLEASE RECHECK SCORE. ")

     #Subject = input("ENTER NEXT SUBJECT: ")
     #score = input("ENTER NEXT SCORE: ")
    #else:
     #print("ENTER SUBJECT AND SCORE: ")
     #Subject = input("ENTER NEXT SUBJECT: ")
     #score = input("ENTER NEXT SCORE: ")


#Run = Calculator(input("ENTER SUBJECT HERE: "),input("ENTER SCORE HERE: "))
#print(Run)

#Number 17
def Calculator(first_number,Operand1,second_number):
  operand = str(Operand1)
  Operand = ["+","-","*","/"]
  digit1 = first_number.isdigit()
  digit2 = second_number.isdigit()
  X = float(first_number)
  Y = float(second_number)
  if digit1 and digit2 == True:
    for operand in Operand:
      if operand == "+":
        output = X + Y
        print(str(output))
       
      elif operand == "-":
         output = X - Y
         print(str(output))
        
      elif operand == "*":
         output = X * Y
         print(str(output))
        
      elif operand == "/":
         output = X/Y
         print(str(output))
      
      first_number = input("Enter digit: ")
      Operand1 = input("Enter operand: ")
      second_number = input("Enter digit: ")
    else:
      print("Operand is not recognized")
      first_number = input("Enter digit: ")
      Operand1 = input("Enter operand: ")
      second_number = input("Enter digit: ")

Run = Calculator(input("Enter first digit: "),input("Enter operand: "),input("Enter second digit: "))
print(Run)

