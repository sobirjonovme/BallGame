

# Kichik o'yin


import turtle 
from random import randint
from tkinter import *


def funk1():
	global kop_hajm
	koptok.hideturtle()
	if kop_hajm < 3:
		kop_hajm += 0.2

	
	funk10(kop_hajm, ran4, x, y)



def funk2():
	global kop_hajm

	koptok.hideturtle()

	if kop_hajm > 0.5:
		kop_hajm -= 0.2
	
	funk10(kop_hajm, ran4, x, y)
	


def funk3():
	a,b = kv.position()
	if a+100 < 200:
		kv.goto(a+40, b)
	else:
		kv.goto(140, b)


def funk4():
	a,b = kv.position()
	if a-100 > -200:
		kv.goto(a-40, b)
	else:
		kv.goto(-140, b)


def funk5():
	global p, step_y, step_x, xp, yp
	p += 1	
	if p % 2 == 1:
		xp = step_x
		yp = step_y
		step_x = 0
		step_y = 0
	if p % 2 == 0:
		step_x = xp
		step_y = yp

	

def funk6():
	ranglar=['yellow','green', 'black', 'grey', 'orange', 'white', 'brown', 'pink', 'magenta']
	global ran1
	global ran2
	global ran3
	global ran4 
	while True:
		ran0 = ranglar[randint(0,8)]
		ran1 = ranglar[randint(0,8)]
		ran2 = ranglar[randint(0,8)]
		ran3 = ranglar[randint(0,8)]
		ran4 = ranglar[randint(0,8)] 
		if ran3 != ran2 and ran4 != ran2 and ran0 != ran1:
			break
			
	main(ran0, ran1, ran2, ran3, ran4, kop_hajm, x, y, step_x, step_y, p, natk)
	

def funk7():
	global step_x, step_y
	step_x *= 1.1
	step_y *= 1.1
	
def funk8():
	global step_x, step_y
	step_x /= 1.1
	step_y /= 1.1

def funk9(txt, n1, m1):

	gap = turtle.Turtle()
	gap.penup()
	gap.speed(0)
	gap.hideturtle()
	gap.goto(n1, m1)
	gap.pencolor('blue')
	gap.write(txt, font=('Arial', 12, 'normal'))


def funk10( k1, rang4, a1, b1):
	global koptok, kop_hajm

	koptok = turtle.Turtle()
	koptok.speed(0)


	koptok.shape('circle')
	
	kop_hajm = k1
	koptok.shapesize(kop_hajm)
	koptok.penup()
	
	koptok.color(rang4)

	koptok.goto(a1, b1)


def funk11():
	main('green', 'yellow', 'red', 'black', 'blue', 1.5, 0, 0, 3, 2, 0, 0)




def main(rang0, rang1, rang2, rang3, rang4, k1, a1, b1, x1, x2, pk, nat):
#def main(rang0, rang1, rang2, rang3, rang4, k1, a1, b1, step_x, step_y):

	global oyna
	global kv, p, natk

	global step_x, step_y, x, y, kop_hajm, ran4


	oyna = turtle.Screen()
	oyna.clear()
	oyna.setup(620,700)

	oyna.title('My_Game-0.1.1')
	oyna.bgcolor(rang0)


	ramka1 = turtle.Turtle()
	ramka1.shape('square')
	ramka1.penup()
	ramka1.speed(0)
	ramka1.shapesize(5.4, 29)
	ramka1.goto(-10, 280)
	ramka1.color("black")

	ramka1 = turtle.Turtle()
	ramka1.shape('square')
	ramka1.penup()
	ramka1.speed(0)
	ramka1.shapesize(5,28.6)
	ramka1.goto(-10, 280)
	ramka1.color("white")

	ramka1 = turtle.Turtle()

	ramka1.shape('square')
	ramka1.penup()
	ramka1.speed(0)
	ramka1.shapesize(5, 0.2)
	ramka1.goto(25, 280)
	ramka1.color("black")



	
	funk9("+ va –  ➟  Koptok tezligini o'zgartirish", -285, 300)
	funk9("A  ➟  Koptokni kattalashtirish", -285, 270)
	funk9("D  ➟  Koptokni kichiklashtirish", -285, 240)
	funk9("P  ➟  Pause / Continue",  40, 300)
	funk9("O  ➟  Rangni o'zgartirish", 40, 270)
	funk9("N  ➟  Yangi o'yin boshlash", 40, 240)



	ramka1 = turtle.Turtle()
	ramka1.shape('square')
	ramka1.shapesize(21)
	ramka1.color(rang1)

	chiziq=turtle.Turtle()
	chiziq.shape('square')
	chiziq.shapesize(20)
	chiziq.color(rang2)


	kv = turtle.Turtle()
	kv.shape('square')
	kv.shapesize(1,6)
	kv.penup()
	kv.speed(0)
	kv.color(rang3)
	kv.goto(0, -190)
	#kv.goto(0,0)
	#kv.shearfactor(-0.5)
	#kv.shapetransform()
	#(4.0, -1.0, -0.0, 2.0)
	#kop_hajm = k1
	ran4 = rang4
	#x = a1
	#y = b1
	natk = nat
	natija = Label(text='Natija: {}'.format(natk), bg='grey', font=13)
	natija.place(x=258, y=570, width=110, height=32)
	#natija.config(text=natk)


	#funk10(kop_hajm, ran4, x, y)
	funk10(k1, rang4, a1, b1)
	#oyna.onkey(funk1, "Right")
	#oyna.onkey(funk2, "Left")
	#oyna.listen()

	step_x = x1
	step_y = x2
	p = pk


	while True:

		
		oyna.onkey(funk3, "Right")
		oyna.onkey(funk4, "Left")
		oyna.onkey(funk5, "p")
		oyna.onkey(funk1, "a")
		oyna.onkey(funk2, "d")
		oyna.onkey(funk6, "o")
		oyna.onkey(funk7, "+")
		oyna.onkey(funk8, "-")
		oyna.onkey(funk11, "n")
		oyna.listen()

			

	
		a, b = kv.position()

		x, y=koptok.position()

		if x >= 200 or x <= -200:
			step_x = -step_x
			koptok.goto(x+step_x, y+step_y)
		if y >= 200: # or y <= -200:
			step_y = -step_y
			koptok.goto(x+step_x, y+step_y)
		if x <= a+60 and x >= a-60 and y <= -170:
			step_y = -step_y
			koptok.goto(x+step_x, y+step_y)
			natk += 1
			natija.config(text="Natija: {}".format(natk))

		if y <= -200:
			break


		koptok.goto(x+step_x, y+step_y)

	
		
	oyna.mainloop()



main('green', 'yellow', 'red', 'black', 'blue', 1.5, 0, 0, 3, 2, 0, 0)
