from turtle import *

# Create and set up Tommy:
t = Turtle()
t.shape("turtle")
t.speed(0)
t.color("black")


# Point Tommy upwards and move to bottom of screen:
t.left(90)
t.penup()
t.goto(0, -150)
t.pendown()

def int_to_hexcode(x):
    a = str(hex(x))
    a = a[2:]
    while len(a) < 2:
        a = "O" + a
    return "#" + a*3



def draw_tree(branch_length):
    # Base case: Stop drawing if the branch gets too short
    if branch_length < 5:
        return
      


  
    # Step 1: Draw the current branch
    t.forward(branch_length)
    
    # Step 2: Turn right and draw a smaller right branch
    t.left(30)
    draw_tree(branch_length - 5)
    
    # ----------------------------------------------------
    # TODO 1: Add the code for the LEFT branch!
    # Hint: You need to turn Tommy left (past center),
    # then call draw_tree(...) with a shorter branch length.
    # ----------------------------------------------------
    t.forward(branch_length - 5)
    t.backward(branch_length - 5)
    t.right(60)
    draw_tree(branch_length - 5)
    
    
    # ----------------------------------------------------
    # TODO 2: Backtrack so Tommy returns to where he started!
    # Hint: Reset Tommy's angle to point straight, 
    # then move backward by branch_length.
    # ----------------------------------------------------
    t.forward(branch_length - 5)
    t.backward(branch_length - 5)
    t.left(30)
  
    t.backward(branch_length)


    

# Start drawing the tree with an initial branch length of 70:
draw_tree(50)

# Write a finish message:
t.penup()
t.goto(0, -200)
t.color("black")
t.write("Finish the tree code!", None, "center", "16pt bold")
t.goto(0, -230)
