"""Snake, classic arcade game.
Exercises
1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.
"""
#
from turtle import *
import random
from freegames import square, vector

saltos=[10,0,-10]

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors=['green','magenta','purple', 'orange','blue']
colorSnake=random.choice(colors)
colorFood=random.choice(colors)
while(colorSnake==colorFood):
    colorFood=random.choice(colors)
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190
tiempo = 0
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = random.randrange(-15, 15) * 10
        food.y = random.randrange(-15, 15) * 10
        square(food.x, food.y, 9, colorFood)
    else:
        snake.pop(0)

    clear()
    global tiempo
    tiempo += 1
    for body in snake:
        square(body.x, body.y, 9, colorSnake)
    if (tiempo == 5):
        if (food.x < 180 and food.x > -180):
            food.x = food.x + random.choice(saltos)
        elif (food.y < 180 and food.y > -180):
            food.y = food.y + random.choice(saltos)
        elif (food.x > 180):
            food.x = food.x - saltos[0]
        elif (food.x < -180):
            food.x = food.x + saltos[0]
        elif (food.y > 180):
            food.x = food.x - saltos[0]
        elif (food.y < -180):
            food.x = food.x + saltos[0]
        tiempo = 0
    square(food.x, food.y, 9, colorFood)
    update()
    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()