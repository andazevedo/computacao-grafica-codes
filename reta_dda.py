import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def init():
    glClearColor(0, 0, 0, 1)
    glPointSize(3)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 10, 0, 10)


def render_line_dda():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINE_STRIP)
    glColor(1, 1, 1)
    step = 0
    k = 0
    dx = 0
    dy = 0
    x1 = 2
    y1 = 3
    x2 = 8
    y2 = 6
    inc_x, inc_y, x, y = 0, 0, 0, 0

    dx = x2 - x1
    dy = y2 - y1

    if x1 == x2:
        dx = 1

    if y1 == y2:
        dy = 1

    if abs(dx) > abs(dy):
        step = abs(dx)
    else:
        step = abs(dy)

    inc_x = dx / step
    inc_y = dy / step

    x = x1
    y = y1

    glVertex2f(float(x), float(y))

    for _ in range(1, step + 1, 1):
        x += inc_x
        y += inc_y
        glVertex2f(float(x), float(y))

    glEnd()
    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Line Drawing using DDA Algorithm")
    init()
    glutDisplayFunc(render_line_dda)
    glutMainLoop()


main()