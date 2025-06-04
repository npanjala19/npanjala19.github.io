

# Niha Panjala
# Project Variation #10 
# This refactored version of my Project 4 uses functions to improve readability and modularity.
# I created parameterized functions for repeated patterns like clouds and balloons, allowing for different
# sizes and colors. I also grouped drawing logic into logical sections to make the code easier to manage and extend.


import turtle
import math

def setup_turtle():
    t = turtle.Turtle()
    t.speed(0) # Fastest speed
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")
    return t, screen

def draw_rectangle(t, width, height, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()

def draw_square(t, size, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
     t.forward(size)
     t.right(90)
    if fill_color:
        t.end_fill()
    
def draw_triangle(t, size, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
     t.end_fill()

def draw_circle(t, radius, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
        t.circle(radius)
    if fill_color:
        t.end_fill()

def draw_polygon(t, sides, size, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)
    if fill_color:
        t.end_fill()


def draw_curve(t, length, curve_factor, segments=10, fill_color=None):

    ### Draw a curved line using small line segments Parameters:
    # t: turtle object
    # length: total length of the curve
    # curve_factor: positive for upward curve, negative for downward curve
    # segments: number of segments (higher = smoother curve)
    # fill_color: optional color to fill if creating a closed shape ##

    if fill_color:
     t.fillcolor(fill_color)
     t.begin_fill()
    segment_length = length / segments
    # Save the original heading
    original_heading = t.heading()

    for i in range(segments):
    # Calculate the angle for this segment
        angle = curve_factor * math.sin(math.pi * i / segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle) # Reset the angle for the next segment


    # Reset to original heading
    t.setheading(original_heading)
    if fill_color:
        t.end_fill()


def jump_to(t, x, y):
# Move turtle without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_hill(t):
    draw_circle(t, 475, fill_color="green")

def draw_single_balloon(t,x,y, balloon_sizes, balloon_color): # creates size and color changeable function
    offset = 0
    for size in balloon_sizes:
        jump_to(t, x + offset, y)
        draw_circle(t, size, fill_color= balloon_color) #draw balloon

    #draw basket
    jump_to(t, (x-70), (y-40))
    draw_rectangle(t, 140, 110, fill_color="brown")

    #draw strings
    jump_to(t, x-70, y-40)
    draw_curve(t, 75, -60, 7)
    jump_to(t, x+15, y+3)
    draw_curve(t, 76, 60,7)

def draw_cloud(t, x, y, sizes): 
    #x,y = starting position (cloud center) sizes = list of circle radii
    offset = 0
    for size in sizes:
        jump_to(t, x + offset, y)
        draw_circle(t, size, fill_color="white")
        offset += size // 2 # spaces based on radius

def draw_all_clouds (t): # simplify implementation
    draw_cloud(t, -150, 200, [90, 80, 50])
    draw_cloud(t, 350, 225, [80, 50, 60])
    draw_cloud(t, -350, 50, [40, 70, 65])
    draw_cloud(t, -350, -200, [90, 50, 70])

def draw_scene(t):

    # draw hills
    jump_to(t, -20, -1200)
    draw_hill(t)
    jump_to(t, 200, -1100)
    draw_hill(t)

    #draw hot air balloons
    draw_single_balloon(t, 150, 150, [90], balloon_color="Red")
    draw_single_balloon(t, -90, -70, [70], balloon_color="Yellow")
    
    # draw clouds
    draw_all_clouds(t)

    # Set background color
    screen = t.getscreen()
    screen.bgcolor("skyblue")

def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()

if __name__ == "__main__":
    main()