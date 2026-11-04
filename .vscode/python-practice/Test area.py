print("what is your name".upper())
name = input()
name = str(name)
NP = [name]
print(type(NP)==str)
print(isinstance(name,str))


print("What is your age bracket?".upper())
NP.append(input())
print("are you married?".upper())
NP.extend(input())  

age= 3.6
print(isinstance(age,float))

  