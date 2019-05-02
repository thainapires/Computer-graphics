from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

cores = [[1,0,0],[1,1,0],[0,1,0],[0,1,1],[0,0,1],[1,0,1],[0.5,1,1],[1,0,0.5],[1,0,0.2],[0.2,1,0.5]]

vertices = (
    (-0.4,0,0.4), #0
    (0.4,0,0.4), #1
    (0.4,0,-0.4), #2
    (-0.4,0,-0.4), #3
    (-0.4,1.8,0.4), #4
    (0.4,1.8,0.4), #5
    (0.4,1.8,-0.4), #6
    (-0.4,1.8,-0.4), #7
    )

linhas = (
    (0,1),
    (1,2),
    (2,3),
    (3,0),
    
    (4,5),
    (5,6),
    (6,7),
    (7,4),
    
    (0,4),
    (1,5),
    (2,6),
    (3,7),
)

def PrismaBQuadrada():
    #base de baixo
    glBegin(GL_QUADS)
    glColor3fv(cores[3])
    glVertex3fv(vertices[0])
    glColor3fv(cores[8])
    glVertex3fv(vertices[1])
    glColor3fv(cores[2])
    glVertex3fv(vertices[2])
    glColor3fv(cores[1])
    glVertex3fv(vertices[3])     
    glEnd()

    #base de cima
    glBegin(GL_QUADS)
    glColor3fv(cores[7])
    glVertex3fv(vertices[4])
    glColor3fv(cores[1])
    glVertex3fv(vertices[5])
    glColor3fv(cores[8])
    glVertex3fv(vertices[6])
    glColor3fv(cores[9])
    glVertex3fv(vertices[7])        
    glEnd()

    #Lados do prisma
    glBegin(GL_QUAD_STRIP)
    glColor3fv(cores[0])
    glVertex3fv(vertices[6])
    glColor3fv(cores[1])
    glVertex3fv(vertices[2])
    glColor3fv(cores[2])
    glVertex3fv(vertices[7])
    glColor3fv(cores[3])
    glVertex3fv(vertices[3])
    glColor3fv(cores[4])
    glVertex3fv(vertices[4])
    glColor3fv(cores[5])
    glVertex3fv(vertices[0])
    glColor3fv(cores[6])
    glVertex3fv(vertices[5])
    glColor3fv(cores[7])
    glVertex3fv(vertices[1])
    glColor3fv(cores[8])
    glVertex3fv(vertices[6])
    glColor3fv(cores[9])
    glVertex3fv(vertices[2])
    glEnd()

    glColor3fv([178,133,0])
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    PrismaBQuadrada()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PRISMABQUADRADA")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
