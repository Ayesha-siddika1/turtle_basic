import turtle

# Create and configure turtle
t = turtle.Turtle()
t.speed(2)  # Slower speed for nicer drawing
t.pensize(6)  # Thicker lines for better visibility
t.penup()
t.goto(-250, 0)
t.pendown()

# Function to draw 'A'
def draw_a(color):
    t.color(color)
    t.setheading(70)
    t.forward(120)
    t.right(140)
    t.forward(120)
    t.backward(60)
    t.right(110)
    t.forward(40)

# Function to draw 'Y'
def draw_y(color):
    t.color(color)
    t.setheading(90)
    t.forward(60)
    t.right(30)
    t.forward(70)
    t.backward(70)
    t.left(60)
    t.forward(70)

# Function to draw 'E'
def draw_e(color):
    t.color(color)
    t.setheading(90)
    t.forward(120)
    t.right(90)
    t.forward(60)
    t.backward(60)
    t.right(90)
    t.forward(60)
    t.left(90)
    t.forward(50)
    t.backward(50)
    t.right(90)
    t.forward(60)
    t.left(90)
    t.forward(60)

# Function to draw 'S'
def draw_s(color):
    t.color(color)
    t.setheading(180)
    t.circle(30, 180)
    t.circle(-30, 180)

# Function to draw 'H'
def draw_h(color):
    t.color(color)
    t.setheading(90)
    t.forward(120)
    t.backward(60)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(60)
    t.backward(120)

# Draw first time with gradient colors
positions = [(-250, 0), (-150, 0), (-50, 0), (30, 100), (100, 0), (180, 0)]
colors = ["#FF0000", "#FF4500", "#FF8C00", "#FFD700", "#FFA500", "#FF6347"]
functions = [draw_a, draw_y, draw_e, draw_s, draw_h, draw_a]

for pos, color, func in zip(positions, colors, functions):
    t.penup()
    t.goto(pos)
    t.pendown()
    func(color)

# Add decorative elements
t.penup()
for x in range(-250, 200, 40):
    t.goto(x, -30)
    t.color("#FFD700")  # Golden color for dots
    t.dot(12)

# Move to new position for second drawing
t.penup()
t.goto(-250, -200)

# Draw second time with different gradient colors
positions = [(-250, -200), (-150, -200), (-50, -200), (30, -100), (100, -200), (180, -200)]
colors = ["#4B0082", "#6A5ACD", "#483D8B", "#7B68EE", "#9370DB", "#8A2BE2"]

for pos, color, func in zip(positions, colors, functions):
    t.penup()
    t.goto(pos)
    t.pendown()
    func(color)

# Add decorative elements for second drawing
t.penup()
for x in range(-250, 200, 40):
    t.goto(x, -230)
    t.color("#6A5ACD")  # Purple color for dots
    t.dot(12)

# Final touches
t.hideturtle()
turtle.done()



