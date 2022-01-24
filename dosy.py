print ("  _____")     
print (" |  __ \ ")
print (" | |  | | ___  ___ _   _")
print (" | |  | |/ _ \/ __| | | |")
print (" | |__| | (_) \__ \ |_| |")
print (" |_____/ \___/|___/\__, |")
print ("                    __/ |")
print ("                   |___/")

print ("Hello! What would you like to do?")
answer = input("play a game, write something or maybe calculate something?")

if answer == "play a game":
    print ("The avabile games are:")
    print ("1. gtngame.py - A guess the number game.")
    print ("2. rollthedice.py - A simple roll the dice game.")

elif answer == "write something":
    print ("The text editor in PyDOS is fsedit.")

elif answer == "write a document":
    print ("The text editor in PyDOS is fsedit")

elif answer == "play games":
    print ("The avabile games are:")
    print ("1. gtngame.py - A guess the number game.")
    print ("2. rollthedice.py - A simple roll the dice game.")

elif answer == "calculate":
    print ("calculator.py is the name of the calculator app.")

elif answer == "calculate something":
    print ("calculator.py is the name of the calculator app.")
else:
    print("Huh?")

