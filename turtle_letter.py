import turtle

t = turtle.Turtle()
t.width(3) 
t.speed(3) 

# Setar o inicio da caneta
def set_start(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Pular para a próxima linha
def next_letter():
    t.color("white")
    t.forward(30)
    t.color("black")

# Letra A
def draw_a():
    t.left(75)
    t.forward(150)
    t.right(150)
    t.forward(150)
    t.backward(75)
    t.right(105)
    t.forward(40)
    t.right(180)
    t.forward(40)
    t.right(75)
    t.forward(75)
    t.left(75)

# Letra B
def draw_b():
    t.left(90)
    t.forward(150)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(75)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(75)
    t.right(90)
    t.forward(65)
    t.right(90)
    t.forward(75)
    t.left(180)
    t.forward(75)

# Letra C
def draw_c():
    t.color("white")
    t.forward(75)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.color("black")
    t.circle(75, 180)

# Letra D
def draw_d():
    t.left(90)
    t.forward(150)
    t.left(90)
    t.circle(75, -180)
    t.pen(pencolor=None)
    t.forward(75)

# Letra E
def draw_e():
    t.left(90)
    t.forward(150)
    t.right(90)
    t.forward(75)
    t.right(180)
    t.forward(75)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(75)
    t.left(180)
    t.forward(75)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(75)

# Letra F
def draw_f():
    t.left(90)
    t.forward(150)
    t.right(90)
    t.forward(75)
    t.right(180)
    t.forward(75)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(75)
    t.left(180)
    t.forward(75)
    t.left(90)
    t.pen(pencolor=None)
    t.forward(75)
    t.left(90)
    t.forward(75)

def draw_g():
    t.circle(50, -180) 
    t.forward(100)  
    t.right(90)
    t.circle(50, 180)  
    t.left(90)
    t.forward(50) 

# Letra I
def draw_i():
    t.left(90)
    t.forward(145)
    t.left(180)
    t.forward(145)
    t.left(90)

# Letra L
def draw_l():
    t.left(90)
    t.forward(150)
    t.left(180)
    t.forward(150)
    t.left(90)
    t.forward(75)

# Letra N
def draw_n():
    t.left(90)
    t.forward(145)
    t.right(160)
    t.forward(155)
    t.left(160)
    t.forward(145)
    t.left(180)
    t.forward(145)
    t.left(90)

# Letra P
def draw_p():
    t.left(90)
    t.forward(150)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(75)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.color("white")
    t.forward(75)
    t.color("black")

# Letra T
def draw_t():
    t.color("white")
    t.forward(37.5)
    t.color("black")
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(37.5)
    t.left(180)
    t.forward(75)
    t.left(180)
    t.forward(37.5)
    t.left(90)
    t.pen(pencolor=None)
    t.forward(150)
    t.pen(pencolor="white")
    t.left(90)
    t.forward(37.5)

# Letra Z
def draw_z():
    t.forward(75)
    t.left(180)
    t.forward(75)
    t.right(117)
    t.forward(165)
    t.left(117)
    t.forward(75)
    t.left(180)
    t.forward(75)
    t.right(117)
    t.forward(165)
    t.left(117)
    t.forward(75)