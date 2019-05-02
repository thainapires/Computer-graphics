from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

xo, yo = -2,-2
xf, yf = 2, 2
px, py = 5.0, 5.0
a,b = 1,1

def funcao():
    dx = (xf - xo)/px
    dy = (yf - yo)/py
    y = yo
    while(y < yf):
        glBegin(GL_QUAD_STRIP)
        x = xo
        while(x < xf):
            glVertex3f(x, y, fun(x,y))
            glVertex3f(x, y+dy, fun(x,y+dy))
            x += dx
        glEnd()
        y += dy
    
def fun(x, y):
    return ((x**2)/a - (y**2)/b)
    #return ((x**2)/a + (y**2)/b)


def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(2, 1, 3, 0)
    funcao()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("funcao")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()