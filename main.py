import turtle
import math
import random

#Screen Creation
screen = turtle.Screen()
screen.setup(540, 580)
screen.bgcolor("black")
screen.addshape("X1708.gif")
screen.addshape("Y3508.png")
screen.addshape("Bullet.png")


#Border Creation
border = turtle.Turtle()
border.penup()
border.speed(0)
border.color("#33FF61")
border.pensize(2)
border.goto(-250,-190)
border.pendown()
for side in range(4):
  border.forward(470)
  border.left(90)
border.hideturtle()
border.penup()

#Scoring
score = 0
scorepen = turtle.Turtle()
scorepen.hideturtle()
scorepen.speed(0)
scorepen.color("#FFD133")
scorepen.penup()
scorepen.goto(-240, 250)
scorestring = "Score %s" %score
scorepen.write(scorestring, False, align = "left", font =("Arial", 14, "normal"))

#Create Player Turtle
pilot = turtle.Turtle()
pilot.penup()
pilot.hideturtle()
pilot.shape("X1708.gif")
pilot.left(90)
pilot.setpos(-10, -150)
pilot.speed(0)
pilot.showturtle()
pilotspeed = 15

#Pilot Controls
def pLeft():
  x = pilot.xcor()
  x -= pilotspeed
  if x < -220:
    x = -220
  pilot.setx(x)
  
def pRight():
  x = pilot.xcor()
  x += pilotspeed
  if x > 190:
    x = 190
  pilot.setx(x)
  
def pUp():
  y = pilot.ycor()
  y += pilotspeed
  if y < -220:
    y = -220
  pilot.sety(y)
  
#Create Enemy
enemyspeed = 5

enemies = []
def createEnemies(number):
  enemy = turtle.Turtle()
  enemy.penup()
  enemy.hideturtle()
  for i in range(number):
    enemies.append(turtle.Turtle())
    
  for enemy in enemies:
    enemy.hideturtle()
    enemy.shape("Y3508.png")
    enemy.penup()
    enemy.left(90)
    xpos = random.randint(-200, 100)
    ypos = random.randint(80, 240)
    enemy.showturtle()
    enemy.goto(xpos, ypos)

#Player weapon
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("Bullet.png")
bullet.penup()
bullet.speed(0)
bullet.left(90)
bullet.hideturtle()
bulletspeed = 20
bullet.goto(pilot.xcor(), pilot.ycor())

#Define Bullet State
#ready -  can fire
#fire - fired (moving)
bulletstate = "ready"
def fire():
  global bulletstate
  if bulletstate == "ready":
    bulletstate = "fire"
    x = pilot.xcor()
    y = pilot.ycor()
    bullet.goto(x,y)
    bullet.showturtle()
    
#check for bullet collision
def collision(t1, t2):
  dist = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
  if dist < 19:
    return True
  else:
    return False

#key binding
screen.listen()
screen.onkey(pLeft, "Left")
screen.onkey(pRight, "Right")
screen.onkey(pUp, "Up")
screen.onkey(fire, "Space")

#run create enemies function
createEnemies(5)

#Main Loop
while True:
  for enemy in enemies:
    #Move enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)
    enemyspeed += .0001
    
    #Reverse
    if enemy.xcor() > 190:
      for e in enemies:
        y = enemy.ycor()
        y -= random.randint(5, 20)
        enemy.sety(y)
      enemyspeed *= -1
      
    if enemy.xcor() < -220:
      for e in enemies:
        y = enemy.ycor()
        y -= random.randint(4, 20)
        enemy.sety(y)
      enemyspeed *= -1
          
    #check enemy and bullet collision
    if collision(bullet, enemy) == True:
        bullestate = "ready"
        #reset bullet
        bullet.showturtle()
        x = pilot.xcor()
        y = pilot.ycor()
        bullet.goto(x,y)
        #reset enemy
        enemy.goto(-10, 200)
        score += 1
        scorestring = "Score: %s" %score
        scorepen.clear()
        scorepen.write(scorestring, False, align = "left", font =("Arial", 14, "normal"))
    
    #check pilot and enemy collision
    if collision(pilot, enemy) == True or enemy.ycor() < -240:
      pilot.hideturtle()
      enemy.hideturtle()
      scorepen.clear()
      scorepen.write("GAME OVER", False, align = "left", font =("Arial", 14, "normal"))
      break
    
  #Bullet Movement
  y = bullet.ycor()
  y += bulletspeed
  bullet.sety(y)
    
  #Check if bullet at top
  if bullet.ycor() > 210:
    bullet.hideturtle()
    bulletstate = "ready"
  
