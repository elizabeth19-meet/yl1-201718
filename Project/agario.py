import turtle
turtle.bgcolor("black")
import time
import random
from ball import Ball

turtle.tracer(0)
turtle.hideturtle()
RUNNING=True
SLEEP=0.06
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2


#create myball


MY_BALL=Ball(0, 0, 0, 0, 40, "white")

NUMBER_OF_BALLS=18
MINIMUM_BALL_RADIUS=5
MAXIMUM_BALL_RADIUS=25
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5

BALLS=[]

for i in range(NUMBER_OF_BALLS):
	x=random.randint(round(-SCREEN_WIDTH)+MAXIMUM_BALL_RADIUS, round(SCREEN_WIDTH)-MAXIMUM_BALL_RADIUS)
	y=random.randint(round(-SCREEN_HEIGHT)+MAXIMUM_BALL_RADIUS, round(SCREEN_HEIGHT)-MAXIMUM_BALL_RADIUS)
	dx=random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	while dx==0:
		dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy=random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	while dy==0:
		dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	r=random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color=(random.random(), random.random(), random.random())
	new_ball=Ball(x,y,dx,dy,r,color)
	BALLS.append(new_ball)


def move_all_balls():
	for ball in BALLS:
		ball.move(SCREEN_WIDTH, SCREEN_HEIGHT)


def collide(ball_a, ball_b):
 	if ball_a==ball_b:
 		return False
 	distance = ((ball_a.xcor() - ball_b.xcor())**2 + (ball_a.ycor() - ball_b.ycor()) ** 2 )**0.5
 	print(distance)
 	if distance + 10 <= ball_a.r + ball_b.r:
 		return True
 	else:
 		return False

def check_myball_collision():
	for ball in BALLS:
		if  collide(ball, MY_BALL)==True:
			a_radius = ball.r
			b_radius = MY_BALL.r
			X_COORDINATE = random.randint(round(-SCREEN_WIDTH), round(SCREEN_WIDTH))
			Y_COORDINATE = random.randint(round(-SCREEN_HEIGHT), round(SCREEN_HEIGHT))
			dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
			dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
			while dx == 0 or dy==0:
		 		dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
		 		dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
			RADIUS = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
			Color = (random.random(), random.random(), random.random())

			if MY_BALL.r>ball.r:
				ball.goto(X_COORDINATE, Y_COORDINATE)
				ball.r = RADIUS
				ball.x = X_COORDINATE
				ball.y = Y_COORDINATE
				ball.dx = dx
				ball.dy = dy
				ball.color(Color)
				ball.shapesize(ball.r/10)
				MY_BALL.r += 1
				MY_BALL.shapesize(MY_BALL.r/10)
			else:
				return False
	return True

def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if  collide(ball_a, ball_b)==True:
				a_radius = ball_a.r
				b_radius = ball_b.r
				X_COORDINATE = random.randint(round(-SCREEN_WIDTH), round(SCREEN_WIDTH))
				Y_COORDINATE = random.randint(round(-SCREEN_HEIGHT), round(SCREEN_HEIGHT))
				dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				while dx == 0 or dy==0:
			 		dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
			 		dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				RADIUS = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				Color = (random.random(), random.random(), random.random())

				if ball_b.r>ball_a.r:
					ball_a.goto(X_COORDINATE, Y_COORDINATE)
					ball_a.r = RADIUS
					ball_a.x = x
					ball_a.y = y
					ball_a.dx = dx
					ball_a.dy = dy
					ball_a.color(Color)
					ball_a.shapesize(ball_a.r/10)
					ball_b.r = ball_b.r+1
					ball_b.shapesize(ball_b.r/10)
				else:
					ball_b.goto(X_COORDINATE, Y_COORDINATE)
					ball_b.r = RADIUS
					ball_b.x = X_COORDINATE
					ball_b.y = Y_COORDINATE
					ball_b.dx = dx
					ball_b.dy = dy
					ball_b.color(Color)
					ball_b.shapesize(ball_b.r/10)
					ball_a.r = ball_a.r+1
					ball_a.shapesize(ball_a.r/10)

def movearound(event):
	MY_BALL.goto(event.x - SCREEN_WIDTH, SCREEN_HEIGHT - event.y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.getscreen().listen()




while (RUNNING==True):
	if (SCREEN_WIDTH!=turtle.getcanvas().winfo_width()/2 or SCREEN_HEIGHT!=turtle.getcanvas().winfo_height()/2):
		SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
		SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2
	move_all_balls()
	check_all_balls_collision()
	RUNNING = check_myball_collision()
	turtle.getscreen().update()
	time.sleep(SLEEP)


 