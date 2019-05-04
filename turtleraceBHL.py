import sys  
import os
import random
import turtle


"""
def namechange():
	playername=input("What is your name? ")
	exists = os.path.exists('/players/playername')
	if exists:
		fh = open('/players/playername', 'r')
		contents = playername.read()
		creds = contents
		print ("Welcome back " + playername + "You have " + creds + " credits in your account")
	else:
		print("File does not exists")
		print ("Welcome " + playername + ", you have been gifted 100 credits")
		creds = 100
"""

def race():
	creds = 100
	turtle_firstname_list = ['Thundering', 'Shooting', 'Riviting', 'Calming', 'Rushing', 'Soothing', 'Speeding', 'Flowing', 'Running', 'Moving', 'Seizing', 'Trying', 'Limping', 'Sparkling', 'Electric', 'Blundering', 'Glowing', 'Glistening', 'Sharp', 'Cutting', 'Smoldering', 'Fierce', 'Firey', 'Blowing', 'Silver', 'Gold', 'Golden', 'Vital', 'Grasping', 'Releasing']

	turtle_lastname_list = ['Force', 'Torrent' ,'River', 'Wind', 'Flood', 'Party', 'Stampede', 'Rush', 'Blast', 'Star', 'Moon', 'Rampage', 'Spark', 'Thunder', 'Rain', 'Shower', 'Arrival', 'Gift', 'Blessing', 'Field', 'Stream', 'Mountain', 'Air', 'Water', 'Fire', 'Earth', 'Spirit', 'Chariot', 'Nova', 'Mystery']

	tfirstname1 = (random.choice(turtle_firstname_list))
	tlastname1 = (random.choice(turtle_lastname_list))

	tfirstname2 = (random.choice(turtle_firstname_list))
	tlastname2 = (random.choice(turtle_lastname_list))

	tfirstname3 = (random.choice(turtle_firstname_list))
	tlastname3 = (random.choice(turtle_lastname_list))

	tfirstname4 = (random.choice(turtle_firstname_list))
	tlastname4 = (random.choice(turtle_lastname_list))

	turtle1name = tfirstname1 + " " + tlastname1
	turtle2name = tfirstname2 + " " + tlastname2
	turtle3name = tfirstname3 + " " + tlastname3
	turtle4name = tfirstname4 + " " + tlastname4

	turtle1oddgen = random.randint(1,21)
	turtle1odds = str (turtle1oddgen)
	turtle2oddgen = random.randint(1,21)
	turtle2odds = str (turtle2oddgen)
	turtle3oddgen = random.randint(1,21)
	turtle3odds = str (turtle3oddgen)
	turtle4oddgen = random.randint(1,21)
	turtle4odds = str (turtle4oddgen)
	
	turtle1stats = turtle1name + " (" + turtle1odds + " to 1 odds)"
	turtle2stats = turtle2name + " (" + turtle2odds + " to 1 odds)"
	turtle3stats = turtle3name + " (" + turtle3odds + " to 1 odds)"
	turtle4stats = turtle4name + " (" + turtle4odds + " to 1 odds)"
	
	ans=True
	while ans:
		print ("1. RED: " + turtle1stats +"\n")
		print ("2. BLUE: " + turtle2stats +"\n")
		print ("3. YELLOW: " + turtle3stats +"\n")
		print ("4. GREEN: " + turtle4stats +"\n")

		ans=input("Which turle to bet on? ")
		if ans=="1":
			print ("You are wagering on number " + ans + " ")
			wager = ans
			wagerodds = turtle1odds
			ans = None
		elif ans=="2":
			print ("You are wagering on number " + ans + " ")
			wager = ans
			wagerodds = turtle2odds
			ans = None
		elif ans=="3":
			print ("You are wagering on number " + ans + " ")
			wager = ans
			wagerodds = turtle3odds
			ans = None
		elif ans=="4":
			print ("You are wagering on number " + ans + " ")
			wager = ans
			wagerodds = turtle4odds
			ans = None
		else:
			print("\n Not a Valid Choice - Please choose 1-4")

	bet=input("How much to bet? ")

	print ("AND THERE OFF!")
	
	screen = turtle.Screen()
	screen.bgcolor("#00ee00")
	screen.setup(750,500)

	turtle1 = turtle.Turtle()
	turtle1.color("red")
	turtle1.shape("turtle")
	turtle1.pensize(3)
	turtle1.width(3)
	turtle1.penup()
	turtle1.goto(-300,-95)
	turtle1.write (turtle1stats)
	turtle1.goto(-300,-75)
	turtle1.pendown()

	turtle2 = turtle.Turtle()
	turtle2.color("blue")
	turtle2.shape("turtle")
	turtle2.pensize(3)
	turtle2.width(3)
	turtle2.penup()
	turtle2.goto(-300,-45)
	turtle2.write (turtle2stats)
	turtle2.goto(-300,-25)
	turtle2.pendown()

	turtle3 = turtle.Turtle()
	turtle3.color("yellow")
	turtle3.shape("turtle")
	turtle3.pensize(3)
	turtle3.width(3)
	turtle3.penup()
	turtle3.goto(-300,5)
	turtle3.write (turtle3stats)
	turtle3.goto(-300,25)
	turtle3.pendown()

	turtle4 = turtle.Turtle()
	turtle4.color("green")
	turtle4.shape("turtle")
	turtle4.pensize(3)
	turtle4.width(3)
	turtle4.penup()
	turtle4.goto(-300,55)
	turtle4.write (turtle4stats)
	turtle4.goto(-300,75)
	turtle4.pendown()
	
	poolbest = 0
	winner = 300	
	while poolbest < winner:
 
		if turtle1.xcor() >= turtle2.xcor() and turtle1.xcor() >= turtle3.xcor() and turtle1.xcor() >= turtle4.xcor():
			poolbest = turtle1.xcor()
			leader = "1"
		elif turtle2.xcor() >= turtle1.xcor() and turtle2.xcor() >= turtle3.xcor() and turtle2.xcor() >= turtle4.xcor():
			poolbest = turtle2.xcor()
			leader = "2"
		elif turtle3.xcor() >= turtle1.xcor() and turtle3.xcor() >= turtle2.xcor() and turtle3.xcor() >= turtle4.xcor():
			poolbest = turtle3.xcor()
			leader = "3"
		elif turtle4.xcor() >= turtle1.xcor() and turtle4.xcor() >= turtle2.xcor() and turtle4.xcor() >= turtle3.xcor():
			poolbest = turtle4.xcor()
			leader = "4"
		
		move1 = random.randint(1,11)
		turtle1.forward(move1)

		move2 = random.randint(1,11)
		turtle2.forward(move2)
		
		move3 = random.randint(1,11)
		turtle3.forward(move3)
		
		move4 = random.randint(1,11)
		turtle4.forward(move4)

	turtle.exitonclick()
	
	print ("And the winner is: ")
	print ("Number ", leader)
	if leader == wager:
		print ("YOU WIN!")
		mycredits = int (creds)
		myodds = int (wagerodds)
		mybet = int (bet)
		winnings = (mycredits + (int (mybet * myodds)))
		strbet = str (bet)
		strwagerodds = str (wagerodds)
		strwinnings = str (winnings)
		print ("Your bet of " + strbet + " credits at " + strwagerodds + " to 1 wins you " + strwinnings + " credits!")
		file = open("playername","w")
		file.write(strwinnings)
		file.close()
	else:
		print ("BUMMER!")
		mybet = int (bet)
		mycredits = int (creds)
		losses = (mycredits - mybet)
		mylosses = str (losses)
		print ("You lost!  Down to " + mylosses + " credits")
		
		file = open("playername","w")
		file.write(mylosses)
		file.close()
	
ans=True
while ans:
	print("""
	1.Change player
	2.Race
	3.Leaderboard
	9.Exit/Quit
	""")
	ans=input("What would you like to do? ")
	if ans=="1":
		print("\n change name function")
		namechange()
	elif ans=="2":
		print("\n Race Time!")
		race()
	elif ans=="3":
		print("\n Leaderboard function")
	elif ans=="9":
		print("\n Quit") 
		ans = None
	else:
		print("\n Not Valid Choice Try again")

