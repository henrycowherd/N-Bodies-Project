#Henry Cowherd
#CS UY 1114
#April 24 2019
#n-bodies


# CS-UY 1114
# Final project

import turtle
import time
import random
# gravitional constant (to be read from file)
G = 0

# current state of all bodies (to be read from file)
# each entry in the list is a tuple consisting of:
#   body name
#   body position (x,y)
#   body velocity (x,y)
#   body mass
# This value is updated at each step of the simulation
# by the update_positions and update_velocities functions.
# sig: list(tuple(str, float, float, float, float, float))
bodies = [("Sun", 500.0, 500.0, 0.0, 0.0, 100000000.0), 
          ("Splat", 255.0, 255.0, 2.0, 0.0, 1.0)]

def readfile(filename):
    """
    signature: str -> tuple(float, list(tuple(str, float, float, float, float, float)))
    This function is called only once, when your
    program first starts. It should read the file
    named in its argument, which contains the correct value
    of the gravitional constant and the initial
    data about the planets. It should return a tuple
    consisting of two values: the value of the
    gravitational constant G, and a list of all
    the bodies read from the file.
    This function should not modify any global
    variables.
    """
    f = open(filename, "r")
    bodies = []
    G = float(f.readline())
    bodiestuple = ()
    for lines in f:
        line = lines.strip().split(" ")
        for i in range(1,len(line)):
            line[i] = float(line[i])
        bodiestuple = tuple(line)
        bodies.append(bodiestuple)                   
    tuple1 = (G,bodies)
    return tuple1

print(readfile("bodies.txt"))
    
G, bodies = readfile("bodies.txt")

def draw_frame():
    """
    signature: () -> NoneType
    Given the current state of the game in
    the global variables, draw all visual
    elements on the screen: the planets
    and their labels, and their current positions.
    Please note that this is your only function
    where drawing should happen (i.e. the only
    function where you call functions in the
    turtle module). Other functions in this
    program merely update the state of global
    variables.
    This function also should not modify any
    global variables.
    """
    global G,bodies
    for body in bodies:
        x = body[1]
        y = body[2]
        mass = (body[5])
        turtle.penup()
        turtle.hideturtle()
        turtle.setpos(x,y)
        turtle.dot(25, 'blue')
        turtle.pencolor('white')
        turtle.write(body[0], font = ("Arial", 14, "normal"))
        turtle.setpos(0,0)
        

draw_frame()


def update_velocities():
    """
    signature: () -> NoneType
    This function updates the global bodies variable
    with the updated velocities of the bodies, as
    described above.
    That is, given the current velocities and
    positions of each body, calculate their velocity
    at the next frame.
    """
    global G, bodies
    
    
    for i in range(len(bodies)):
        xnetforce = 0
        ynetforce = 0
        body = tuple(bodies[i]) 
        x1 = body[1]
        y1 = body[2]
        M1 = body[5]       
        for body2 in bodies:
            x2 = body2[1]
            y2 = body2[2]
            dx = (x2-x1)
            dy = (y2-y1)
            d = (((x1-x2)**2)+((y1-y2)**2))**(1/2)
            M2 = body2[5]
            if d != 0:
                xforce = G*(M1*M2*dx)/(d**3)
                yforce = G*(M1*M2*dy)/(d**3)
                xnetforce += xforce
                ynetforce += yforce
#VELOCITY
        xnetacceleration = xnetforce/M1
        ynetacceleration = ynetforce/M1
        xnetvelocity = body[3] + xnetacceleration
        ynetvelocity = body[4] + ynetacceleration
        bodies[i] = (body[0],body[1],body[2],xnetvelocity,ynetvelocity,body[5])
            
def update_positions():
    """
    signature: () -> NoneType
    This function updates the global bodies variable
    with the updated positions of the bodies, as
    described above.
    That is, given the current velocities and
    positions of each body, calculate their position
    at the next frame.
    """
    global G, bodies
    
    for i in range(len(bodies)):
        body = tuple(bodies[i])
        x = body[1] + body[3]
        y = body[2] + body[4]
        bodies[i] = (body[0],x,y,body[3],body[4],body[5])
             
def main():
    """
    signature: () -> NoneType
    Run the simulation. You shouldn't
    need to modify this function.
    """
    global G, bodies
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.setworldcoordinates(0,0,1000,1000)
    while True:
        update_velocities()
        update_positions()
        turtle.clear()
        draw_frame()
        turtle.update()
        time.sleep(0.05)
turtle.bgcolor("black")

main()
