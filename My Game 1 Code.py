""" My First Project/Game #Snake Water and Gun Game!!!!"""

import random
def GameWon(computer,human):
	if computer==human:
		return None
	elif computer=="s" and human=="w":
		return computer
	elif computer=='w' and human=='s':
		return human
	elif computer=='g' and human=='w':
		return human
	elif computer=='w' and human=='g':
			return computer
	elif computer=='g' and human=='s':
			return computer
	elif computer=='s' and human=='g':
			return human

computer_score=0

human_score=0

rounds=int(input("How Many Rounds You Want to Play - "))
print("\n")

for i in range(1,rounds+1):
	print("Computer Turn-snake(s=1)water(w=2)gun(g=2)-??\n")

	x=random.randint(1,3)
	if x==1:
		computer="s"
	elif x==2:
		computer='w'
	elif x==3:
		computer='g'

	human=input("Human Turn-snake(s)water(w)gun(g)- ",)
	if human =="w":
		pass
	elif human =="s":
		pass
	elif human =="g":
		pass
	else:
		print("Please Choose a Value out of s,w,g")
		break
	print("\n")
	print("ROUND",i,"\n")
	print(f"Computer Chooses- {computer}\n")
	print(f"Human Chooses- {human}\n")

	a = GameWon(computer,human)
	if a==None:
		print("Match Tie \n")
	elif a==human:
		print("Human Won \n")
		human_score+=1
	elif a==computer:
		print("Computer Won \n")
		computer_score+=1
	i+=1

	if i==rounds+1:
			print(f"Computer Score is {computer_score}\n")
			print(f"Human Score is {human_score}\n")

			if computer_score>human_score:
				print("Computer Won the Series by",computer_score,"-",human_score,"\n")
			elif human_score>computer_score:
				print("Human Won the Series by",human_score,"-",computer_score,"\n")
			else:
				print("Series Draw with Score",human_score,"-",computer_score)
