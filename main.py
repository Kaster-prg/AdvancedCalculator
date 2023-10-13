import random
from os import system
import time


def welcome():
	global name
	print(
	    "(Please note: Final outputs of each calculation are stored to a external file)"
	)
	f = open("Adv_Cal_Data.txt", "a")
	name = input("Hello there user, please enter your name:\n")
	if name == "":
		name = "~DEFAULT~"
	f.write("\n")
	f.write(name)
	f.close()
	print("Hello", name+".\nPress enter to continue")
	input()
	system('clear')
	menu()


def menu():
	charBank = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
	print("Here are some options you can choose from:")
	print("1. Addition")
	print("2. Multiplication")
	print("3. Division")
	print("4. Subtraction")
	print("5. Converting Distance")
	print("6. Converting Speed")
	print("7. Converting File Sizes")
	print("8. Converting Binary to Decimal (or Decimal to Binary)")
	print("9. Converting Binary to Hexadecimal (or Hexadecimal to Binary)")
	print("10. Converting Decimal to Hexadecimal (or Hexadecimal to Decimal)")
	print("11. Password Generation")
	print("12. Quit")
	print(
	    "(Please enter the number of the operation you would wish to perform.)"
	)
	choice = input()
	if choice == "12":
		quit
	elif choice == "1":
		add()
	elif choice == "2":
		mult()
	elif choice == "3":
		div()
	elif choice == "4":
		sub()
	elif choice == "5":
		dist()
	elif choice == "6":
		speed()
	elif choice == "7":
		fize()
	elif choice == "8":
		bindec()
	elif choice == "9":
		binhex()
	elif choice == "10":
		hexdec()
	elif choice == "11":
		passGen(charBank)
	else:
		print("Input Unrecognised, try again")
		time.sleep(3)
		system('clear')
		menu()


def add():
	f = open("Adv_Cal_Data.txt", "a")
	system('clear')
	counter = 0
	calcout = 0
	print(
	    "You can add as many numbers together as you wish, yet when you are finished, please press ENTER without any numbers to finish the calculation."
	)
	calcout = float(input())
	while counter != 99:
		num = input()
		if num == "":
			counter = 98
		else:
			num = float(num)
			calcout += num
		counter += 1
	print("The Final output of the calculation is:", calcout,
	      "\nReturning to menu...")
	f.write(" ")
	f.write(str(calcout))
	f.close()
	time.sleep(5)
	system('clear')
	menu()


def mult():
	f = open("Adv_Cal_Data.txt", "a")
	system('clear')
	counter = 0
	calcout = 1
	print(
	    "You can multiply as many numbers together as you wish, yet when you are finished, please press ENTER without any numbers to finish the calculation."
	)
	calcout = float(input())
	while counter != 99:
		num = input()
		if num == "":
			counter = 98
			num = 1
		else:
			num = float(num)
			calcout = calcout * num
		counter += 1
	print("The Final output of the calculation is:", calcout,
	      "\nReturning to menu...")
	f.write(" ")
	f.write(str(calcout))
	f.close()
	time.sleep(5)
	system('clear')
	menu()


def div():
	f = open("Adv_Cal_Data.txt", "a")
	system('clear')
	counter = 0
	calcout = 1
	print(
	    "You can divide as many numbers together as you wish, yet when you are finished, please press ENTER without any numbers to finish the calculation."
	)
	print("(Please note, the everything will be divided from the first value)")
	calcout = float(input())
	while counter != 99:
		num = input()
		if num == "":
			counter = 98
			num = 1
			num = float(num)
		else:
			num = float(num)
			calcout = calcout / num
		counter += 1
	print("The Final output of the calculation is:", calcout,
	      "\nReturning to menu...")
	f.write(" ")
	f.write(str(calcout))
	f.close()
	time.sleep(5)
	system('clear')
	menu()


def sub():
	f = open("Adv_Cal_Data.txt", "a")
	system('clear')
	counter = 0
	calcout = 0
	print(
	    "You can subtract as many numbers together as you wish, yet when you are finished, please press ENTER without any numbers to finish the calculation."
	)
	print(
	    "(Please note, the everything will be subtracted from the first value)"
	)
	calcout = float(input())
	while counter != 99:
		num = input()
		if num == "":
			counter = 98
			num = 0
			num = float(num)
		else:
			num = float(num)
			calcout = calcout - num
		counter += 1
	print("The Final output of the calculation is:", calcout,
	      "\nReturning to menu...")
	f.write(" ")
	f.write(str(calcout))
	f.close()
	time.sleep(5)
	system('clear')
	menu()


def dist():
	f = open("Adv_Cal_Data.txt", "a")
	system('clear')
	print(
	    "Would you like to convert: \n1. Miles into Kilometres\n2.Kilometres into Miles\n3.Metres into Yards\n4.Yards into Metres\n5.Centimetres into Inches\n6.Inches into Centimetres\n7. Quit"
	)
	print(
	    "(Please enter the number of the calculation you would like to perform)\n"
	)
	choice = input()
	if choice == "1":
		miles = float(input("Please enter the amount of miles: "))
		calcout = miles * 1.60934
		print(miles, "mile(s) is(/are)", calcout, "kilometres.")
	elif choice == "2":
		km = float(input("Please enter the amount of Kilometres: "))
		calcout = km * 0.621371
		print(km, "kilometre(s) is(/are)", calcout, "miles.")
	elif choice == "3":
		m = float(input("Please enter the amount of metres: "))
		calcout = m * 1.09361
		print(m, "metre(s) is(/are)", calcout, "yards.")
	elif choice == "4":
		yard = float(input("Please enter the amount of yards: "))
		calcout = yard * 0.9144
		print(yard, "yard(s) is(/are)", calcout, "metre(s).")
	elif choice == "5":
		cm = float(input("Please enter the amount of centimetres: "))
		calcout = cm * 0.393701
		print(cm, "centimetre(s) is(/are)", calcout, "inch(es).")
	elif choice == "6":
		inches = float(input("Please enter the amount of inches: "))
		calcout = inches * 2.54
		print(inches, "inch(es) is(/are)", calcout, "centimetre(s).")
	elif choice == "7":
		print("Returning to menu...")
		time.sleep(5)
		system('clear')
		menu()

	f.write(" ")
	f.write(str(calcout))
	f.close()
	print("Returning to menu...")
	time.sleep(5)
	system('clear')
	dist()


def speed():
	f = open("Adv_Cal_Data.txt", "a")
	system('clear')
	print(
	    "Would you like to convert: \n1. km/h into mph\n2. mph into km/h\n3. m/s into km/h\n4. km/h into m/s\n5. Quit"
	)
	print(
	    "(Please enter the number of the calculation you would like to perform)\n"
	)
	choice = input()
	if choice == "1":
		speed = float(input("Please enter the speed in km/h: "))
		calcout = speed * 0.621371
		print("The speed", speed, "in km/h is", calcout, "in mph.")
	elif choice == "2":
		speed = float(input("Please enter the speed in mph: "))
		calcout = speed * 1.60934
		print("The speed", speed, "in mph is", calcout, "in km/h.")
	elif choice == "3":
		speed = float(input("Please enter the speed in m/s: "))
		calcout = speed * 3.6
		print("The speed", speed, "in m/s is", calcout, "in km/h.")
	elif choice == "4":
		speed = float(input("Please enter the speed in km/h: "))
		calcout = speed * 0.277778
		print("The speed", speed, "in km/s is", calcout, "in m/s.")
	elif choice == "5":
		print("Returning to menu...")
		time.sleep(5)
		system('clear')
		menu()
	f.write(" ")
	f.write(str(calcout))
	f.close()
	print("Returning to menu...")
	time.sleep(5)
	system('clear')
	speed()


def fize():
	f = open("Adv_Cal_Data.txt", "a")
	system('clear')
	print(
	    "Would you like to convert: \n1. Bits into Bytes \n2. Bytes into Bits \n3. Bytes into Kilobytes \n4. Kilobytes into bytes \n5. Kilobytes into bits \n6.Bits into kilobytes \n7. Quit"
	)
	print(
	    "(Please enter the number of the calculation you would like to perform)\n"
	)
	choice = input()
	if choice == "1":
		num = float(input("Amount of bits: "))
		calcout = num / 8
		print("This amount of bits, creates", calcout, "bytes.")
	elif choice == "2":
		num = float(input("Amount of bytes: "))
		calcout = num * 8
		print("This amount of bytes, creates", calcout, "bits.")
	elif choice == "3":
		num = float(input("Amount of bytes: "))
		calcout = num / 1000
		print("This amount of bytes, creates", calcout, "kilobytes.")
	elif choice == "4":
		num = float(input("Amount of kilobytes: "))
		calcout = num * 1000
		print("This amount of kilobytes, creates", calcout, "bytes.")
	elif choice == "5":
		num = float(input("Amount of kilobytes: "))
		calcout = num * 8000
		print("This amount of kilobytes, creates", calcout, "bits.")
	elif choice == "6":
		num = float(input("Amount of bits: "))
		calcout = num / 8
		calcout = num / 1000
		print("This amount of bits, creates", calcout, "kilobytes.")
	elif choice == "7":
		print("Returning to menu...")
		time.sleep(5)
		system('clear')
		menu()
	f.write(" ")
	f.write(str(calcout))
	f.close()
	print("Returning to menu...")
	time.sleep(5)
	system('clear')
	fize()


def bindec():
	f = open("Adv_Cal_Data.txt", "a")
	print(
	    "(For now, this program only supports 8 bit binary for the binary-decimal conversion)\n\n"
	)
	print(
	    "Would you like to: \n1. Convert Binary into Decimal \n2. Convert Decimal into Binary \n3. Quit \n"
	)
	print(
	    "(Please enter the number of the calculation you would like to perform)\n"
	)
	choice = input()
	if choice == "1":
		binary = input(
		    "Please enter your 8 bit binary value (include all of the 0's): ")
		counter = 0
		if binary[0] == "1":
			counter += 128
		if binary[1] == "1":
			counter += 64
		if binary[2] == "1":
			counter += 32
		if binary[3] == "1":
			counter += 16
		if binary[4] == "1":
			counter += 8
		if binary[5] == "1":
			counter += 4
		if binary[6] == "1":
			counter += 2
		if binary[7] == "1":
			counter += 1
		print("The binary value", binary, "is", counter, "in decimal.")
		f.write(str(counter))
		f.close()
	elif choice == "2":
		decimal = int(input("Please enter your integer: "))
		decimal1 = converting(decimal)
		f.write(" ")
		f.write(str(decimal1))
		f.close()
	elif choice == "3":
		print("Returning to menu...")
		time.sleep(5)
		system('clear')
		menu()
	print("\nReturning to menu...")
	time.sleep(5)
	system('clear')
	bindec()


def converting(num):
	if num > 1:
		converting(num // 2)
	print(num % 2, end='')
	return num


def binhex():
	f = open("Adv_Cal_Data.txt", "a")
	system('clear')
	print(
	    "Would you like to convert: \n1. Binary into Hex \n2. Hexadecimal into Binary \n3. Quit"
	)
	print(
	    "(Please enter the number of the calculation you would like to perform)\n"
	)
	choice = input()
	if choice == "1":
		binary = input(
		    "Enter your binary value you would like in hexadecimal: ")
		calcout = hex(int(binary, 2))
		print("This is your binary value in hex:", hex(int(binary, 2)))
	elif choice == "2":
		hexadecimal = input(
		    "Enter your hexadecimal value you would like in binary: ")
		decimal = int(hexadecimal, 16)
		calcout = bin(decimal)
		print("Your hexadecimal value has returned as:", str(calcout),
		      "in binary.")
	elif choice == "3":
		print("Returning to menu...")
		time.sleep(5)
		system('clear')
		menu()
	f.write(" ")
	f.write(str(calcout))
	f.close()
	print("Returning to menu...")
	time.sleep(5)
	system('clear')
	binhex()


def hexdec():
	f = open("Adv_Cal_Data.txt", "a")
	system('clear')
	print(
	    "Would you like to convert: \n1. Decimal into Hex \n2. Hexadecimal into Decimal\n3. Return to menu")
	print(
	    "(Please enter the number of the calculation you would like to perform)\n"
	)
	choice = input()
	if choice == "1":
		try:
			decimal = int(input("Please enter your integer: "))
			#decimal1 = converting(decimal)
			calcout = hex(decimal)
			print(decimal,"is",calcout,"in Hexidecimal")
			hexdec = 0
			f.write(" ")
			f.write(str(calcout))
			f.write(str(hexdec))
			f.close()
		except:
			print("The input is not recognised\nPress enter to return to menu")
			input()
			menu()
	elif choice == "2":
		hexadecimal = input(
		    "Enter your hexadecimal value you would like in decimal: ")
		try:
			decimal = int(hexadecimal, 16)
			calcout = bin(decimal)
			hexdec = int(calcout, 2)
			print("Your hexadecimal value has returned as:", str(hexdec), "in decimal.")
			f.write(" ")
			f.write(str(calcout))
			f.write(str(hexdec))
			f.close()
		except:
			print("The input is not in base 16\nPress enter to return to menu")
			input()
			menu()
	elif choice == "3":
		print("Returning to menu...")
		time.sleep(2)
		system('clear')
		menu()
	else:
		print("Invalid Input, try again")
	print("Press enter to continue")
	input()
	system('clear')
	menu()


def passGen(charBank):
	size = input("Please enter the desired length of the password: ")
	size = int(size)
	password = str()
	i = 0
	while i != size:
		password = password+str(charBank[randNumGen(61)])
		i = i + 1
	print("Generated password is:",password,"\nPress enter to return to the menu")
	input()
	menu()


def randNumGen(size):
	numb = random.randint(0,size)
	return numb


welcome()