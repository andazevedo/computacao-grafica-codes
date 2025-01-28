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


def render_line_bresenham():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINE_STRIP)
    glColor3f(1, 1, 1)

    # Coordenadas da linha
    x1, y1 = 2, 3
    x2, y2 = 8, 6

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)


    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1


    if dx > dy:

        p = 2 * dy - dx
        x, y = x1, y1
        glVertex2f(x, y)
        print(f"Desenhando ponto: ({x}, {y})")

        for i in range(dx):
            x += sx
            if p < 0:
                p += 2 * dy
            else:
                y += sy
                p += 2 * (dy - dx)
            glVertex2f(x, y)
            print(f"Desenhando ponto: ({x}, {y})")
    else:

        p = 2 * dx - dy
        x, y = x1, y1
        glVertex2f(x, y)
        print(f"Desenhando ponto: ({x}, {y})")

        for i in range(dy):
            y += sy
            if p < 0:
                p += 2 * dx
            else:
                x += sx
                p += 2 * (dx - dy)
            glVertex2f(x, y)
            print(f"Desenhando ponto: ({x}, {y})")

    glEnd()
    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Line Drawing using Bresenham Algorithm")
    init()
    glutDisplayFunc(render_line_bresenham)
    glutMainLoop()


main()
