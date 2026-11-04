def Calculator(Subject,score):
 while True:
    if Subject.isdigit() == False or score.isdigit() == True:
     X = float(score)
     first_letter = Subject[:1].upper()
     remainder = Subject[1:len(Subject)].lower()
     subject = first_letter + remainder
     if X>100:
        print("INPUTED SCORE IS ABOVE 100. PLEASE RECHECK SCORE.")
     if 70<=X<=100:
        grade = "A"
        print(subject+": "+"Score: "+str(X)+" Grade: "+grade)
     if 60<=X<=69:
        grade = "B"
        print(subject+": "+"Score: "+str(X)+" Grade: "+grade)
     if 50<=X<= 59:
        grade = "C"
        print(subject+": "+"Score: "+str(X)+" Grade: "+grade)
     if 45<=X<=49:
        grade = "D"
        print(subject+": "+"Score: "+str(X)+" Grade: "+grade)
     if 0<=X<=39:
        grade = "F"
        print(subject+": "+"Score: "+str(X)+" Grade: "+grade)
     if X<0:
        print("INPUTED SCORE IS BELOW ZERO. PLEASE RECHECK SCORE. ")

     Subject = input("ENTER NEXT SUBJECT: ")
     score = input("ENTER NEXT SCORE: ")
    else:
     print("ENTER SUBJECT AND SCORE: ")
     Subject = input("ENTER NEXT SUBJECT: ")
     score = input("ENTER NEXT SCORE: ")


Run = Calculator(input("ENTER SUBJECT HERE: "),input("ENTER SCORE HERE: "))
Run

