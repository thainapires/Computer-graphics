from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

cores = [[1,0,0],[1,1,0],[0,1,0]]

def PiramedeBaseN(tamBase):

    baseTamanho = tamBase
    raio = 0.8 

    #base N
    glBegin(GL_POLYGON)
    for i in range(0, baseTamanho):
        glColor3fv(cores[i % len(cores)])
        glVertex3fv([(math.cos(2 * math.pi * i / baseTamanho)*raio), -1, (math.sin(2 * math.pi * i / baseTamanho)*raio)])
    glEnd()

    #Triangulos
    glBegin(GL_TRIANGLE_FAN)
    glColor3fv(cores[0])
    glVertex3fv([0, 1, 0]) #comecando no ponto mais alto da piramide para comecar a ligar aos pontos da base
    for i in range(0,baseTamanho + 1):
        glColor3fv(cores[i % len(cores)])
        glVertex3fv([(math.cos(2 * math.pi * i / baseTamanho)*raio), -1, (math.sin(2 * math.pi * i / baseTamanho)*raio)])
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    PiramedeBaseN(10)
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

#PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PiramideBaseN")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
