import time
import turtle

turtle.speed(100)

n_iterations = int(input("Enter integer number: "))

for i in range(n_iterations):
    turtle.forward(i * 2)
    turtle.left(119)
    turtle.left(100)

turtle.done()
time.sleep(1000)
