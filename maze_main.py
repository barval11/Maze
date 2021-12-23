from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from maze_model import *


obs = Obstacle()
obs2 = Obstacle2()
obs3 = Obstacle3()
obs4 = Obstacle4()
obs5 = Obstacle5()
obs6 = Obstacle6()
obs7 = Obstacle7()
obs8 = Obstacle8()
obs9 = Obstacle9()
obs10 = Obstacle10()
obs11 = Obstacle11()
obs12 = Obstacle12()
obs13 = Obstacle13()
car = Car(40, 5) #Start position


def Obstcl():

    glLoadIdentity()
    glTranslated(0, 0, 0)

    obs.draw()
    obs2.draw()
    obs3.draw()
    obs4.draw()
    obs5.draw()
    obs6.draw()
    obs7.draw()
    obs8.draw()
    obs9.draw()
    obs10.draw()
    obs11.draw()
    obs12.draw()
    obs13.draw()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    Obstcl()
    car.draw()

    glutSwapBuffers()


def reshape(width, height):
    glClearColor(0.4, 0.2, 0.0, 0.0)
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)


def keyboard(k, x, y):
    if ord(k) == 27:
        sys.exit()


def special(k, x, y):
    global car

    mirror = False
    rotate = 0

    if k == GLUT_KEY_UP:
        if car.y < 565: #Ke atas
            car.y += 5
            rotate = 1
       
        elif car.y >= 570: #Batas atas
            car.y = 570

    elif k == GLUT_KEY_DOWN:
        if car.y > 5: #Ke bawah
            car.y -= 5.0
            rotate = 3

        elif car.y <= 5: #Batas bawah
            car.y = 5
            rotate = 3
        
    elif k == GLUT_KEY_LEFT:
        if car.x > 40: #Ke kiri
            car.x -= 5.0
            mirror = True

        if car.x <= 40: #Batas kiri
            car.x = 20
            mirror = True
            
    elif k == GLUT_KEY_RIGHT:
        if car.x <= 575: #Ke kanan
            car.x += 5.0
            mirror = False

        if car.x >= 580: #Batas kanan
            car.x = 580
    else:
        return
    car.rotate = rotate
    car.mirror = mirror
    glutPostRedisplay()


if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)

    glutInitWindowPosition(0, 0)
    glutInitWindowSize(600, 600)
    glutCreateWindow('Maze Car')

    #callbacks
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special)

    #mainloop
    glutMainLoop()
