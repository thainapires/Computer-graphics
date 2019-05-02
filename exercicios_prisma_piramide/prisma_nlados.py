from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import random
 
cores = [[0,1,1],[0,0,1],[1,0,1],[0.8,1,0]]

def PrismadeBaseN(r, tamBase ,alt):
     
    baseTamanho = tamBase
    altura = alt
    raio = r

    #base de baixo
    glBegin(GL_POLYGON)
    for i in range(0, baseTamanho):  
        glColor3fv(cores[i%len(cores)])   
        glVertex3fv([math.cos(2* math.pi * i/baseTamanho) * raio, -1 , math.sin(2 * math.pi * i/baseTamanho) * raio])
    glEnd()

    #lados
    glBegin(GL_TRIANGLE_STRIP)  
    for i in range(0, baseTamanho+1):
        glColor3fv(cores[i%len(cores)])         
        glVertex3fv([math.cos(2* math.pi * i/baseTamanho) * raio, altura, math.sin(2 * math.pi * i/baseTamanho) * raio])    
        glVertex3fv([math.cos(2* math.pi * i/baseTamanho) * raio, -1 , math.sin(2 * math.pi * i/baseTamanho) * raio])
    glEnd()

    #base de cima
    glBegin(GL_POLYGON)
    for i in range(0, baseTamanho):     
        glColor3fv(cores[i%len(cores)])        
        glVertex3fv([math.cos(2* math.pi * i/baseTamanho) * raio, altura, math.sin(2 * math.pi * i/baseTamanho) * raio])
    glEnd()     

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    #glRotatef(math.pi/10,0,1,0)
    PrismadeBaseN(1, 7, 2)
    glutSwapBuffers()
    
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
 
#PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PRISMANBASE")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(40,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
