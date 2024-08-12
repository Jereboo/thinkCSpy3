#A program that tells the path of a drunk pirate
import turtle

wn = turtle.Screen()
drunk_pirate = turtle.Turtle()
drunk_pirate.speed(10)

for i in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    drunk_pirate.left(i)
    drunk_pirate.forward(100)

print(drunk_pirate.towards(0,0))

turtle.exitonclick()