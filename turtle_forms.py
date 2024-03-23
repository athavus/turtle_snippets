import turtle

t = turtle.Turtle()
t.width(3) 
t.speed(3) 

def draw_heart():
    t.color("white")
    t.goto(-50, -225)
    t.color("black")
    t.fillcolor('red')  
    t.begin_fill() 
    t.left(140)
    t.forward(100)
    t.circle(-50, 200)
    t.left(120)
    t.circle(-50, 200)
    t.forward(100)
    t.end_fill()