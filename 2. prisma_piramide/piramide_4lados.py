from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

vertices = (
    (0,1,0),
    (1,-1,1),
    (1,-1,-1),
    (-1,-1,-1),
    (-1,-1,1)
    )

linhas = (
    (0,1),
    (0,2),
    (0,3),
    (0,4),
    (1,2),
    (1,4),
    (2,3),
    (3,4)
)

facesTRI = (
    (0,1,2),
    (0,1,4),
    (0,3,4),
    (0,2,3)    
)

faceQUA = (1,2,3,4)

cores = [[1,0,0],[1,1,0],[0,1,0],[0,1,1],[0,0,1],[1,0,1],[0.5,1,1],[1,0,0.5],[1,0,0.2],[0.2,1,0.5]]

def Piramide():

    #base
    glBegin(GL_QUADS)
    glVertex3fv(vertices[1])
    glVertex3fv(vertices[2])
    glVertex3fv(vertices[3])
    glVertex3fv(vertices[4])
    glEnd()

    #triangulos 
    glBegin(GL_TRIANGLE_FAN)
    glColor3fv(cores[1])
    glVertex3fv(vertices[0])
    glColor3fv(cores[1])
    glVertex3fv(vertices[2])
    glColor3fv(cores[2])
    glVertex3fv(vertices[3])
    glColor3fv(cores[3])
    glVertex3fv(vertices[4])
    glColor3fv(cores[4])
    glVertex3fv(vertices[1])
    glColor3fv(cores[5])
    glVertex3fv(vertices[2])
    glEnd()

    glColor3fv(cores[4])
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()
      
def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Piramide()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

#PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PIRAMIDE")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()


