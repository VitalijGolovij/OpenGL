import numpy as np
from OpenGL.GL import *
import glfw
import random
import math

glfw.init()
window = glfw.create_window(900, 700, "PyOpenGL Triangle", None,None)
glfw.set_window_pos(window, 600, 300)
glfw.make_context_current(window)


# Now we will pour color for the animation's background
glClearColor(0.0, 0.0, 0.0,0.0)
def exemple1():
    while not glfw.window_should_close(window):
# this while loop will keep iterating all the functions below until the window is not closed
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
# creating rotation animated motion
        glColor3f(0.32,0.44,0.12)
        glPointSize(15)
        glEnable(GL_POINT_SMOOTH)
        glBegin(GL_POINTS)
        glVertex2f(-1,-1)
        glVertex2f(-1,1)
        glVertex2f(0,0)
        glVertex2f(1,-1)
        glVertex2f(1,1)
        glEnd()
        glfw.swap_buffers(window)

def exemple2():
    while not glfw.window_should_close(window):
# this while loop will keep iterating all the functions below until the window is not closed
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
# creating rotation animated motion
        glPointSize(3)
        glBegin(GL_POINTS)
        for i in range(1,100):
                glColor3f(random.random(),random.random(),random.random())
                glVertex2f(random.random()*2-1,random.random()*2-1)
        glEnd()
        glfw.swap_buffers(window)

def exemple3():
    while not glfw.window_should_close(window):
# this while loop will keep iterating all the functions below until the window is not closed
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
# creating rotation animated motion
        glLineWidth(2.5)
        glBegin(GL_LINES)
        glVertex2f(-1,1)
        glVertex2f(1,-1)
        glVertex2f(-1,-1)
        glVertex2f(1,1)
        glEnd()
        glfw.swap_buffers(window)

def exemple4():
    while not glfw.window_should_close(window):
# this while loop will keep iterating all the functions below until the window is not closed
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
# creating rotation animated motion
        glLineWidth(2.5)
        glLineStipple(2,0x1C47)
        glEnable(GL_LINE_STIPPLE)
        glBegin(GL_LINES)
        glVertex2f(0.5,-1)
        glVertex2f(0.5,1)
        glEnd()
        glLineStipple(2,0x0101)
        glBegin(GL_LINES)
        glVertex2f(0,-1)
        glVertex2f(0,1)
        glEnd()
        glLineStipple(2,0x00FF)
        glBegin(GL_LINES)
        glVertex2f(-0.5,-1)
        glVertex2f(-0.5,1)
        glEnd()
        glfw.swap_buffers(window)

def exemple5():
    while not glfw.window_should_close(window):
# this while loop will keep iterating all the functions below until the window is not closed
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
# creating rotation animated motion
        glLineWidth(2.5)
        glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
        glBegin(GL_TRIANGLES)
        for i in range(0,6):
                glVertex2f(0,0)
                glVertex2f(0.5*math.cos(2*math.pi*i/6),0.5*math.sin(2*math.pi*i/6))
                glVertex2f(0.5 * math.cos(2 * math.pi * (i+1) / 6), 0.5 * math.sin(2 * math.pi * (i+1) / 6))
        glEnd()
        glfw.swap_buffers(window)

def exemple6():
    while not glfw.window_should_close(window):
# this while loop will keep iterating all the functions below until the window is not closed
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
# creating rotation animated motion
        glLineWidth(2.5)
        glBegin(GL_TRIANGLE_STRIP)
        glVertex2f(1,1)
        glVertex2f(-1,1)
        glVertex2f(-1,-1)
        glVertex2f(1,-1)
        glEnd()
        glfw.swap_buffers(window)

def exemple7():
    while not glfw.window_should_close(window):
# this while loop will keep iterating all the functions below until the window is not closed
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
# creating rotation animated motion
        glLineWidth(2.5)
        glBegin(GL_TRIANGLE_STRIP)
        glVertex2f(random.random()*2-1,random.random()*2-1)
        for i in range(0,10):
                glColor3f(random.random(),random.random(),random.random())
                glVertex2f(random.random()*2-1,random.random()*2-1)
                glVertex2f(random.random() * 2 - 1, random.random() * 2 - 1)
        glEnd()
        glfw.swap_buffers(window)

def exemple8():
    while not glfw.window_should_close(window):
# this while loop will keep iterating all the functions below until the window is not closed
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
# creating rotation animated motion
        glLineWidth(2.5)
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(0,0)
        for i in range(0,101):
                glColor3f(random.random(),random.random(),random.random())
                glVertex2f(0.5*math.cos(2*math.pi*i/100), 0.5*math.sin(2*math.pi*i/100))
        glEnd()
        glfw.swap_buffers(window)

def exemple9():
    while not glfw.window_should_close(window):
# this while loop will keep iterating all the functions below until the window is not closed
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
# creating rotation animated motion
        glLineWidth(2.5)
        glBegin(GL_QUADS)
        glColor3f(random.random(),random.random(),random.random())
        glVertex2f(-0.6,0.2)
        glVertex2f(-0.7,0.7)
        glVertex2f(0.1,0.65)
        glVertex2f(0.25,-0.78)
        glColor3f(random.random(),random.random(),random.random())
        glVertex2f(0.3,-0.6)
        glVertex2f(0.45,0.7)
        glVertex2f(0.8,0.65)
        glVertex2f(0.9,-0.8)
        glEnd()
        glfw.swap_buffers(window)

def exemple10():
    while not glfw.window_should_close(window):
# this while loop will keep iterating all the functions below until the window is not closed
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
# creating rotation animated motion
        glLineWidth(2.5)
        glBegin(GL_POLYGON)
        for i in range(0,7):
                glVertex2f(0.5*math.cos(2*math.pi*i/6),0.5*math.sin(2*math.pi*i/6))
        glEnd()
        glfw.swap_buffers(window)

def flag():
    while not glfw.window_should_close(window):
# this while loop will keep iterating all the functions below until the window is not closed
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
# creating rotation animated motio
        glBegin(GL_QUADS)
        glColor3f(1.0,0.0,0.0)
        glVertex2f(-0.75,0.5)
        glVertex2f(-0.75,-0.15)
        glVertex2f(0.75,-0.15)
        glVertex2f(0.75,0.5)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(0.0,1.0,0.0)
        glVertex2f(-0.75,-0.15)
        glVertex2f(-0.75,-0.5)
        glVertex2f(0.75,-0.5)
        glVertex2f(0.75,-0.15)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.0)
        glVertex2f(-0.75,0.5)
        glVertex2f(-0.75,-0.5)
        glVertex2f(-0.55,-0.5)
        glVertex2f(-0.55,0.5)
        glEnd()
        glLineWidth(5)
        glBegin(GL_LINE_STRIP)
        glColor3f(1.0,0.0,0.0)
        glVertex2f(-0.75,0.5)
        glVertex2f(-0.55,0.5-0.33)
        glVertex2f(-0.75,0.5-0.66)
        glVertex2f(-0.55,-0.5)
        glEnd()
        glBegin(GL_LINE_STRIP)
        glColor3f(1.0,0.0,0.0)
        glVertex2f(-0.55,0.5)
        glVertex2f(-0.75,0.5-0.33)
        glVertex2f(-0.55,0.5-0.66)
        glVertex2f(-0.75,-0.5)
        glEnd()
        glfw.swap_buffers(window)

def lab3exemple1():
        while not glfw.window_should_close(window):
                # this while loop will keep iterating all the functions below until the window is not closed
                glfw.poll_events()
                glClear(GL_COLOR_BUFFER_BIT)
                # creating rotation animated motion
                glPointSize(3)
                glBegin(GL_TRIANGLE_FAN)
                glVertex2f(0,0)
                for i in range(0, 6):
                        glColor3f(random.random(), random.random(), random.random())
                        glVertex2f(0.5 * math.cos(2 * math.pi * 6), 0.5 * math.sin(2 * math.pi * 6))
                glEnd()
                glfw.swap_buffers(window)

lab3exemple1()
glfw.terminate()
