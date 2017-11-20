from turtle import Turtle,colormode
import turtle
import random

class Square(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shape('square')
		self.shapesize(size)

	def random_color(self):
		colormode(255)
		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)
		self.color(r, g, b)


square = Square(50)
square.random_color()
turtle.mainloop()

