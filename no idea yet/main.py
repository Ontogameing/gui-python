from tkinter import *
import time

CLICKHOMECOLOR = "gray"

root = Tk()
root.config(bg = CLICKHOMECOLOR)
root.geometry("500x500")

def addMoney():
	global money
	global amount
	money += amount
	moneyLabel.config(text = "$" + str(money))

def buy1():
	global money
	global amount

	if money >= 50:
		money -= 50
		amount = 2
		buy1Button.place_forget()
		moneyLabel.config(text = "Bought for $50")
	elif money < 50:
		moneyLabel.config(text = "You need at least $50")

def buy2():
	global money
	global amount

	if money >= 100:
		money -= 100
		amount = 4
		buy2Button.place_forget()
		moneyLabel.config(text = "Bought for $100")
	elif money < 100:
		moneyLabel.config(text = "You need at least $100")

def buy3():
	global money
	global amount

	if money >= 200:
		money -= 200
		amount = 8
		buy3Button.place_forget()
		moneyLabel.config(text = "Bought for $200")
	elif money < 200:
		moneyLabel.config(text = "You need at least $200")

def buy4():
	global money
	global amount

	if money >= 400:
		money -= 400
		amount = 16
		buy4Button.place_forget()
		moneyLabel.config(text = "Bought for $400")
	elif money < 400:
		moneyLabel.config(text = "You need at least $400")

money = 0
amount = 1

moneyLabel = Label(root, text = "Start clicking", bg = CLICKHOMECOLOR)
clickerButton = Button(root, text = "Click me!", bg = CLICKHOMECOLOR, command = addMoney)
shopLabel = Label(root, text = "Shop", bg = CLICKHOMECOLOR)
buy1Button = Button(root, text = "Upgrade 1", bg = CLICKHOMECOLOR, command = buy1)
buy2Button = Button(root, text = "Upgrade 2", bg = CLICKHOMECOLOR, command = buy2)
buy3Button = Button(root, text = "Upgrade 3", bg = CLICKHOMECOLOR, command = buy3)
buy4Button = Button(root, text = "Upgrade 4", bg = CLICKHOMECOLOR, command = buy4)

moneyLabel.place(x = 0, y = 0)
clickerButton.place(x = 75, y = 175)
shopLabel.place(x = 88, y = 205)
buy1Button.place(x = 0, y = 235)
buy2Button.place(x = 70, y = 235)
buy3Button.place(x = 140, y = 235)
buy4Button.place(x = 210, y = 235)

root.mainloop()