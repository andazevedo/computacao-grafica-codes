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

def analytic_function():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINE_STRIP)
    glColor3f(1, 1, 1)
    x, y, ix, iy = 0,0,0,0

    m, b = 0,0

    x1, y1 = 2, 3
    x2, y2 = 8, 6

    if x1 > x2:
        ix = x1
        iy = y1
        x1 = x2
        y1 = y2
        x2 = ix
        y2 = iy

    if x1 == x2:
        for y in range(y1, y2 + 1):
            glVertex2f(x1, y)

    else:  # Tratamento para outras linhas
        m = (y2 - y1) / (x2 - x1)
        b = y2 - (m * x2)
        for x in range(x1, x2 + 1):
            y = math.ceil((m * x) + b)
            glVertex2f(x, y)
    glEnd()
    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Line Drawing Analytic Function")
    init()
    glutDisplayFunc(analytic_function)
    glutMainLoop()


main()


