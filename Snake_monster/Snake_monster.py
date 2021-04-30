import random
import turtle
from time import time

BOUNDAYR_POINTS = [[-250, -290], [250, -290], [250, 290], [-250, 290], [-250, 210], [250, 210]]
p_snake_status = {"Direction": "", "Motive": "active"}
DIRECTION = {'Up': 90, 'Down':270, 'Left': 180, 'Right': 0}
g_food_location = {
    1: [0, 0], 2: [0, 0], 3: [0, 0], 
    4: [0, 0], 5: [0, 0], 6: [0, 0], 
    7: [0, 0], 8: [0, 0], 9: [0, 0] 
    }
FOOD_EATEN = { # If the food be eaten, it's location would be set to [9999, 9999]
    1: [9999, 9999], 2: [9999, 9999], 3: [9999, 9999], 
    4: [9999, 9999], 5: [9999, 9999], 6: [9999, 9999], 
    7: [9999, 9999], 8: [9999, 9999], 9: [9999, 9999]
    }
g_tails_length, g_tails_location = 5, []
g_body_contact = 0
COLLISION_DISTANCE, MOVE_DISTANCE= 14, 20  # 10*sqrt(2) = 14
DELAY_TIME, g_coff = 200, 1 # Contorl the speed
SNAKE_HEAD_COLOR, SNAKE_TAIL_COLOR, MOSTER_COLOR = "pink", "gold", "red"

def initTurtle(p_turtle, p_x, p_y, p_speed, p_shape=None, p_color="black"): # Initialize Turtle, incluidng coordinate, speed, shape and color
    p_turtle.penup()
    p_turtle.setposition(p_x, p_y)
    p_turtle.speed(p_speed)
    p_turtle.shape(p_shape)
    p_turtle.color(p_color)

def assignFood():
    for food in g_food_location:
        initTurtle(foodPen, g_food_location[food][0], g_food_location[food][1], 0)
        foodPen.write(food)
#------Change the movement of the snake-------#
def turnUp():
    p_snake_status["Direction"] = "Up"
    p_snake_status["Motive"] = "active"

def turnDown():
    p_snake_status["Direction"] = "Down"
    p_snake_status["Motive"] = "active"

def turnLeft():
    p_snake_status["Direction"] = "Left"
    p_snake_status["Motive"] = "active"

def turnRight():
    p_snake_status["Direction"] = "Right"
    p_snake_status["Motive"] = "active"

def pause():
    if p_snake_status["Motive"] == "active":
        p_snake_status["Motive"] = "Pause"
    else:
        p_snake_status["Motive"] = "active"
#----------------------------------------------#
# Display snake's movement status
def displayStatus():
    if p_snake_status["Motive"] == "Pause":
        return "Pause"
    else:
        return p_snake_status["Direction"]

def move():
    global g_tails_length, g_coff
    if abs(snake.xcor()) > 230 or snake.ycor() < -270 or snake.ycor() > 190:
        snakeScreen.tracer(0)
        snake.backward(MOVE_DISTANCE)

    if (p_snake_status["Direction"] != "" 
        and p_snake_status["Motive"] == "active" 
        and g_food_location != FOOD_EATEN 
        and snake.distance(monster) >= COLLISION_DISTANCE):
            snake.setheading(DIRECTION[p_snake_status["Direction"]])
            snake.forward(MOVE_DISTANCE)
            # Make snake's tails
            snake.fillcolor(SNAKE_TAIL_COLOR)
            ungrown_tails = g_tails_length - len(g_tails_location) + 1
            if ungrown_tails > 0:
                snake.stamp()
                ungrown_tails -= 1
                g_tails_location.append(snake.position())
                g_coff = 2 # Snake should be slower when ie generate its tails
            elif ungrown_tails == 0:
                snake.stamp()
                g_tails_location.append(snake.position())
                snake.clearstamps(1)
                del g_tails_location[0] # Since there is not ungrown tails
                g_coff = 1
            snake.color(SNAKE_HEAD_COLOR)
            snakeScreen.update()
    snakeScreen.ontimer(move, int(g_coff*DELAY_TIME)) # Adjust the speed of snake movement

def eat():
    global g_tails_length
    for food in g_food_location:
        if snake.distance(g_food_location[food][0], g_food_location[food][1]) <= COLLISION_DISTANCE:
            g_food_location[food] = [9999, 9999] # Remove food. In fact, it is outside the screen. If you delete it directly it will cause traversal error
            g_tails_length += food # Food increases the length of the snake's tail
            foodPen.clear() ## Remove all food and reassign them
            assignFood()    ##
    snakeScreen.ontimer(eat, DELAY_TIME)

def chase():
    global g_body_contact
    if (snake.distance(monster) >= COLLISION_DISTANCE  ##
        and g_food_location != FOOD_EATEN              ## Make sure the beast moves after the snake moves
        and p_snake_status["Direction"] != ""):        ##
            for single_tail in g_tails_location:
                if monster.distance(single_tail[0], single_tail[1]) < COLLISION_DISTANCE: # Determine if contact
                    g_body_contact += 1
            x_snake_mon_dis = snake.xcor() - monster.xcor()  ## Determine the horizontal and vertical distances,
            y_snake_mon_dis = snake.ycor() - monster.ycor()  ## which one is bigger to move to which side first.
            if abs(x_snake_mon_dis) > abs(y_snake_mon_dis):  ## Use abs(distance)/distance choose the direction(+ or -)
                monster.goto(monster.xcor() + MOVE_DISTANCE*(abs(x_snake_mon_dis)/(x_snake_mon_dis)), monster.ycor())
            elif abs(y_snake_mon_dis) >= abs(x_snake_mon_dis):
                monster.goto(monster.xcor(), monster.ycor() + MOVE_DISTANCE*(abs(y_snake_mon_dis)/(y_snake_mon_dis)))         
    snakeScreen.ontimer(chase, random.randint(200, 500))  # Random velocity
 
def main(p_1, p_2): # turtle.onclick return 2 arg, as xcor and ycor.
    startTime = time()
    assignFood()
    informationPen.clear()
    while True:
        statusPen = turtle.Turtle() 
        statusPen.hideturtle()
        initTurtle(statusPen, -180, 235, 0) # Header's status information
        statusPen.write("Body Contact: " + str(g_body_contact) + "    " + "Time: " + str(int(time() - startTime)) + "    " + "Motion: " + displayStatus(), font=("Arial", 14, "normal"))
        snakeScreen.update() # Update header's game status
        statusPen.clear()
        # Determine if the game is over(win or lose)
        if g_food_location == FOOD_EATEN:
            snake.write("Winner!!", font = ("Arial", 12, "normal"))
            break
        elif snake.distance(monster) < COLLISION_DISTANCE:
            snake.write("Game Over!!", font = ("Arial", 12, "normal"))
            break
        
#------------Initialize the game------------#
# Set up game area
snakeScreen = turtle.Screen() 
snakeScreen.title("Snake Game by weilin")
snakeScreen.setup(660, 740)
# Draw boundary
boundaryPen = turtle.Turtle()
initTurtle(boundaryPen, -250, 290, 0)
boundaryPen.ht()
boundaryPen.pd()
for boundaryPoint in BOUNDAYR_POINTS:
    boundaryPen.goto(boundaryPoint[0], boundaryPoint[1])
# Print game information
informationPen = turtle.Turtle()
informationPen.hideturtle()
initTurtle(informationPen, -230, 70, 0)
informationPen.write("Welcome to weilin's Snake Game... \n\n" + "You are going to use the 4 arrow keys to move the snake \n" + "around the screen, trying to consume all food items\n" + "before the monster catches you... \n\n" + "Click anywhere on the screen to start the game!!", font=("Arial", 12, "normal"))
# Making snake's head
snake = turtle.Turtle()
initTurtle(snake, 0, -40, 0, "square", SNAKE_HEAD_COLOR)
# Assign food
foodPen = turtle.Turtle()
foodPen.hideturtle()
food_x_list, food_y_list = random.sample(list(set(range(-240, 240))-set(range(-20, 20))), 10), random.sample(list(set(range(-280, 200))-set(range(-50, -30))), 10)
for food in g_food_location:
    g_food_location[food] = [food_x_list[food-1], food_y_list[food-1]]
# Make monster
monster = turtle.Turtle()
monster_x, monster_y = random.randint(-240, 240), random.randint(-280, 200)
while snake.distance(monster_x, monster_y) <= COLLISION_DISTANCE*3:       # Keep monster start further away from snake
    monster_x, monster_y = random.randint(-240, 240), random.randint(-280, 200)
initTurtle(monster, monster_x, monster_y, 2, "square", MOSTER_COLOR)
#------------------------------------------#

# Monitor and control the game
snakeScreen.tracer(0)
snakeScreen.onclick(main)
snakeScreen.listen()
snakeScreen.onkey(turnUp, "Up")
snakeScreen.onkey(turnDown, "Down")
snakeScreen.onkey(turnLeft, "Left")
snakeScreen.onkey(turnRight, "Right")
snakeScreen.onkeypress(pause, "space")
# The snake and the monster begin to move
move()
eat()
chase()
snakeScreen.mainloop()