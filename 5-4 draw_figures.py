import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle
pen.speed(5)

# Rysowanie kwadratów
figures.draw_square(100)

pen.penup()
pen.goto(-150, 150)
pen.pendown()

figures.draw_square(80)

#Rysowanie trójkątów
pen.penup()
pen.goto(-150, -150)
pen.pendown()

figures.draw_triangle(100)

pen.penup()
pen.goto(50, -150)
pen.pendown()

figures.draw_triangle(70)

#Rysowanie prostokątów
pen.penup()
pen.goto(150, 150)
pen.pendown()

figures.draw_rectangle(100, 60)

pen.penup()
pen.goto(150, 0)
pen.pendown()

figures.draw_rectangle(70, 30)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()