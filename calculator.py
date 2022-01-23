# Python Calculator

print ("  _____      _            _       _             ")
print (" / ____|    | |          | |     | |            ")
print ("| |     __ _| | ___ _   _| | __ _| |_ ___  _ __ ")
print ("| |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|")
print ("| |___| (_| | | (__| |_| | | (_| | || (_) | |   ")
print (" \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   ")
print ("                               Version 1.1      ")
print ("")
l = 0

while l == 0:
	print ("1 - Add")
	print ("2 - Subtract")
	print ("3 - Multiply")
	print ("4 - Divide")
	print ("5 - Quit")
	answer = input("What would you like to do? ")
	if answer == "1": #Addition
		float1 = input("Enter the first number: ")
		float2 = input("Enter the second number: ")
		float3 = float(float1) + float(float2)
		print ("")
		print (float3)
		print ("")
	elif answer == "2": #Subtraction
		float1 = input("Enter the first number: ")
		float2 = input("Enter the second number: ")
		float3 = float(float1) - float(float2)
		print ("")
		print (float3)
		print ("")
	elif answer == "3": #Multiplication
		float1 = input("Enter the first number: ")
		float2 = input("Enter the second number: ")
		float3 = float(float1) * float(float2)
		print ("")
		print (float3)
		print ("")
	elif answer == "4": #Division
		float1 = input("Enter the first number: ")
		float2 = input("Enter the second number: ")
		float3 = float(float1) / float(float2)
		print ("")
		print (float3)
		print ("")
	else:
		l = 1
