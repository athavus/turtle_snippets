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

# Letra G
def draw_g():
    t.color("white")
    t.left(90)
    t.forward(60)
    t.left(90)
    t.color("black")
    t.forward(45)
    t.left(180)
    t.forward(90)
    t.left(180)
    t.forward(45)
    t.right(90)
    t.circle(75, -270) 

# Letra H
def draw_h():
    t.left(90)
    t.forward(150)
    t.left(180)
    t.forward(75)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(75)
    t.left(180)
    t.forward(150)
    t.left(90)

# Letra I
def draw_i():
    t.left(90)
    t.forward(145)
    t.left(180)
    t.forward(145)
    t.left(90)

# Letra J
def draw_j():
    t.color("white")
    t.left(90)
    t.forward(40)
    t.right(180)
    t.color("black")
    t.circle(50, 180)
    t.forward(110)
    t.left(90)
    t.forward(45)
    t.left(180)
    t.forward(90)
    t.color("white")
    t.right(90)
    t.forward(150)
    t.left(90)

# Letra K
def draw_k():
    t.left(90)
    t.forward(150)
    t.left(180)
    t.forward(75)
    t.left(135)
    t.forward(105)
    t.left(180)
    t.forward(105)
    t.left(90)
    t.forward(110)
    t.left(45)

# Letra L
def draw_l():
    t.left(90)
    t.forward(150)
    t.left(180)
    t.forward(150)
    t.left(90)
    t.forward(75)

# Letra M
def draw_m(): 
    t.left(90)
    t.forward(150)
    t.right(135)
    t.forward(105)
    t.left(90)
    t.forward(105)
    t.right(135)
    t.forward(150)
    t.left(90)

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

# Letra O
def draw_o():
    t.color("white")
    t.forward(37.5)
    t.color("black")
    t.circle(75, 360)
    t.pen(pencolor=None)
    t.forward(75)

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

# Letra Q
def draw_q():
    t.color("white")
    t.forward(37.5)
    t.color("black")
    t.circle(70, 360)
    t.circle(70, 45)
    t.left(90)
    t.forward(30)
    t.left(180)
    t.forward(60)
    t.left(180)
    t.forward(30)
    t.right(90)
    t.circle(70, 315)
    t.pen(pencolor=None)
    t.forward(75)

# Letra R
def draw_r():
    t.left(90)
    t.forward(150)
    t.right(90)
    t.forward(50)
    t.pen(pencolor=None)
    t.right(90)
    t.forward(75)
    t.left(90)
    t.color("black")
    t.circle(37.5, 180)
    t.forward(50)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(50)
    t.left(180)
    t.forward(50)
    t.left(138)
    t.forward(115)
    t.left(42)

# Letra S
def draw_s():
    t.forward(25)
    t.circle(40, 180)  
    t.circle(-35, 180)
    t.forward(30)
    t.left(180)
    t.forward(30)
    t.circle(35, 180)
    t.circle(-40, 180)
    t.forward(25)
    t.pen(pencolor=None)
    t.left(180)
    t.forward(75)

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

def draw_u():
    t.pen(pencolor=None)
    t.forward(37.5)
    t.color("black")
    t.circle(37.5, 90)
    t.forward(110)
    t.left(180)
    t.forward(110)
    t.circle(-37.5, 90)
    t.circle(-37.5, 90)
    t.forward(110)
    t.left(180)
    t.forward(110)
    t.circle(37.5, 90)
    t.pen(pencolor=None)
    t.forward(37.5)

# Letra V
def draw_v():
    t.pen(pencolor=None)
    t.forward(37.5)
    t.color("black")
    t.left(75)
    t.forward(150)
    t.left(180)
    t.forward(150)
    t.right(150)
    t.forward(150)
    t.left(180)
    t.forward(150)
    t.left(75)
    t.pen(pencolor=None)
    t.forward(37.5)

# Letra W
def draw_w():
    t.pen(pencolor=None)
    t.forward(37.5)
    t.color("black")
    t.left(115)
    t.forward(150)
    t.left(180)
    t.forward(150)
    t.left(135)
    t.forward(75)
    t.right(140)
    t.forward(75)
    t.left(135)
    t.forward(155)
    t.left(180)
    t.forward(155)
    t.right(135)
    t.forward(75)
    t.left(160)
    t.pen(pencolor=None)
    t.forward(75)
    t.left(90)
    t.forward(80)

# Letra X
def draw_x():
    t.left(60)
    t.forward(170)
    t.left(180)
    t.forward(85)
    t.right(120)
    t.forward(85)
    t.left(180)
    t.forward(170)
    t.left(60)

# Letra Y
def draw_y():
    t.left(90)
    t.forward(75)
    t.left(45)
    t.forward(90)
    t.right(180)
    t.forward(90)
    t.left(90)
    t.forward(90)
    t.left(180)
    t.forward(90)
    t.left(45)
    t.forward(75)
    t.left(90)
    t.pen(pencolor=None)
    t.forward(65)

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