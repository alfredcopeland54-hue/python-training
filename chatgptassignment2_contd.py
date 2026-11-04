#Number 18
#def Electricity_bill(Units):
 #while True:
    #units = float(Units)
    #First100_Units = float(units*50)
    #Next100_Units1 = float(units*75)
    #Next100_Units2 = float(units*120)
    #Above300_Units = float(units*150)
    #if units <= 100:
        #print("TOTAL BILL: "+str(First100_Units))
    #elif 100<units<=200:
       #print("TOTAL BILL: "+str(Next100_Units1))
    #elif 200<units<=300:
       #print("TOTAL BILL: "+str(Next100_Units2))
    #if units>300:
       #print("TOTAL BILL: "+str(Above300_Units))
    #Units = input("Enter Units: ")

#Number 19
#Run = Electricity_bill(input("Enter Units: "))
#print(Run)

#import random
#def Guessing_game(Your_guess):
 #while True:
   #Computers_choice = [1,2,3,4,5,6,7,8,9,10]
   #your_guess = float(Your_guess)
   #for computer_choice in Computers_choice:
      #computer_choice = float(random.choice(Computers_choice))
      #if computer_choice == your_guess:
         #print("YOU WON !!!")
      
      #else:
         #print("YOU LOST.")
   
      #Your_guess = input("Wanna continue? Lets play again: ")
   
#Run = Guessing_game(input("I'm thinking of a number. make a guess: "))
#print(Run)
    #Number 19
  #Advanced project-- may or may not be completed today
def Income_record(Date,Individual,Debit,Credit,):
   while True:
    date = str(Date)
    first_letter = Individual[:1].upper()
    remainder = Individual[1:len(Individual)].upper()
    individual = first_letter + remainder
    if Debit.isdigit() == True and Credit.isdigit() == True:
      debit = float(Debit)
      credit = float(Credit)
      Balance = credit - debit
      print(f"Date: {date} Individual: {individual} Debit: {debit} Credit: {credit} Balance: {Balance}" )
    else :
      print("Invalid Credit or Debit input! ")
      
    Date = input ("Enter Date: ")
    Individual = input("Enter name of individual: ")
    Debit = input("Debit: ")
    Credit = input("Credit: ")

Run = Income_record(input("Enter Date: "),input("Enter Name of Individual: "), input("Debit: "), input("Credit: "))
print(Run)

    
