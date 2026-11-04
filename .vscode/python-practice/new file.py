#Number 12
def Seconds_converter(seconds):
    while True:
        if seconds == "Start":
          print("Starting...")
          Seconds = input("Type in number of seconds: ")
          X = int(Seconds)
          sec_hours = str(X//3600)
          rem_hours = str(X % 3600)
          sec_mins = str(X//60)
          rem_mins = str(X % 60)
          print(X)
          print(sec_hours+" hours and "+rem_hours+" minutes.")
          print(sec_mins+" minutes and "+rem_mins+" seconds.")
        else:
           print("Type 'Start' ")
           seconds = input()

Run = Seconds_converter(input())
print(Run)

  

    
    