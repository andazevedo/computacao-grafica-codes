from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window_height = 300
window_width = 300
window_title = b"Renderizar ponto com OpenGL"

roof = [
    [0,0.8],
    [-0.3,0.3],
    [0.3,0.3],
    ]
base = [
    [-0.3, 0.3],
    [0.3, 0.3],
    [0.3, -0.3],
    [-0.3, -0.3],
    ]
door = [
    [-0.1, -0.1],
    [0.1, -0.1],
    [0.1,-0.3],
    [-0.1, -0.3]
    ]

def init():
    glClearColor(0, 0, 0, 1)
    glPointSize(5)

def render():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.0, 0.9)
    glEnd()

    glBegin(GL_LINE_LOOP)
    for v in roof:
     glVertex2fv(v)
    glEnd()

    glBegin(GL_LINE_LOOP)
    for v in base:
        glVertex2fv(v)
    glEnd()

    glBegin(GL_LINE_LOOP)
    for v in door:
        glVertex2fv(v)
    glEnd()



    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow(window_title)
    init()
    glutDisplayFunc(render)
    glutMainLoop()

if __name__ == "__main__":
    main()
