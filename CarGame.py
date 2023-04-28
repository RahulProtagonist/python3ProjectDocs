# Sample Car Game

command = ""
Started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if Started:
            print("Car is already started")
        else:
            Started = True
            print("Car is started")
    elif command == "stop":
        if not Started:
            print("Car is already stopped")
        else :
            Started = False
            print("Car is stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit the program
        """)
    elif command == "quit" :
        print("Exited the vehicle ")
        break
    else:
        print("You cannot do that")




