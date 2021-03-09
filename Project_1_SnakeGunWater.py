import random

def gameWin(computer,human):
	if computer==human:
		return None
	elif computer=="s":
		if human=="w":
			return False
		elif human=="g":
			return True
	elif computer=="w":
		if human=="g":
			return False
		elif human=="s":
			return True
	elif computer=="g":
		if human=="s":
			return False
		elif human=="w":
			return True
print("Computer turn snake(s=1)water(w=2)gun(g=2)-- ??")
x=random.randint(1,3)
if x==1:
	computer ='s'
elif x==2:
	computer ='w'
elif x==3:
	computer ='g'
human=input("Your Turn snake(s=1)water(w=2)gun(g=2)-- ")
a = gameWin(computer,human)
print(f"Computer choose- {computer}")
print(f"Human choose- {human}")
if a == None:
	print("Game Tie")
elif a== True:
	print("You Won")
else:
	print("Computer Won")


