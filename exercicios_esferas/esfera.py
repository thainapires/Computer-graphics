from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import random

def esfera(raio):
    r = raio
    theta = -(math.pi/2.0)
    phi = 0
    j = 0
    cont = math.pi/6.0
    cores = [[0, 0.4, 0.4], [0.7, 0.3, 0.3], [0, 0, 1]]
    
    def s(u,v):
        return ((r * math.cos(u)) * math.cos(v), r * math.sin(u), (r*math.cos(u)) * math.sin(v))

    for i in range(0, 6):
        glBegin(GL_TRIANGLE_STRIP)
        phi = 0
        for i in range(0,18):
            glColor3fv(cores[j])
            j+=1
            if j== len(cores)-1:
                j=0
            glVertex3fv(s(theta,phi))
            glVertex3fv(s(theta+cont,phi))
            phi += cont
        glEnd()
        theta += cont
		
def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(2, 1, 3, 0)
    esfera(2)
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(5, timer, 1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Esfera")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(65,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()