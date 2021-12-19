from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from maze_model import *

arrow = Arrow()
road = Road()
road2 = Road2()
road3 = Road3()
road4 = Road4()
road5 = Road5()
road6 = Road6()
road7 = Road7()
road8 = Road8()
road9 = Road9()
road10 = Road10()
road11 = Road11()
road12 = Road12()
road13 = Road13()
car = Car(40, 5) #Start position

def florest(x, y, rows, columns):
    glLoadIdentity()
    glTranslated(x, y, 0)
    for i in range(rows):
        for _ in range(columns):
            road.draw()
            glTranslated(25, 0, 0)
        glLoadIdentity()
        glTranslated(x, i * 30 + y, 0)

def level():
    #florest(20, 50, 4, 11)
    #florest(20, 140, 8, 1)
    #florest(20, 350, 4, 24)
    #florest(370, 50, 11, 10)

    glLoadIdentity()
    glTranslated(0, 0, 0)
    #arrow.draw()

    #c = arrow.centroide()

    #glLoadIdentity()
    #glTranslated(110 + c[0], 290 + c[1], 0)
    #glRotated(180, 0, 0, 1)
    #glScaled(2, 2, 1)
    #glTranslated(-c[0], -c[1], 0)
    #arrow.draw()
    road.draw()
    road2.draw()
    road3.draw()
    road4.draw()
    road5.draw()
    road6.draw()
    road7.draw()
    road8.draw()
    road9.draw()
    road10.draw()
    road11.draw()
    road12.draw()
    road13.draw()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    level()
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
    # If esc is pressed, exit.
    if ord(k) == 27:
        sys.exit()

def special(k, x, y):
    global car

    mirror = False
    rotate = 0
    if k == GLUT_KEY_UP:
        if car.x < 95: #Road 1
            car.y += 0
        if car.x > 95:
            car.y += 5
            rotate = 1
        #if car.y <= 570: #Ke atas
            #car.y += 5.0
            #rotate = 1
        if car.y >= 570: #Batas atas
            car.y = 570

    elif k == GLUT_KEY_DOWN:
        if car.x < 140 and car.y < 100: #Kotak1
            car.y -= 0
        if car.y >= 10: #Ke bawah
            car.y -= 5.0
            rotate = 3
        if car.y <= 5: #Batas bawah
            car.y = 5
            rotate = 3
        
    elif k == GLUT_KEY_LEFT:
        if car.y > 40 and car.x > 140: #Kotak1
            car.x -= 0
            mirror = True
        if car.x >= 25: #Ke kiri
            #car.x -= 5.0
            #mirror = True
        if car.x <= 20: #Batas kiri
            car.x = 20
            mirror = True
            
    elif k == GLUT_KEY_RIGHT:
        if car.x <= 95: #Kotak1
            car.x += 5
        #if car.x <= 575: #Ke kanan
            #car.x += 5.0
            #mirror = False
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
    glutCreateWindow('Driver')

    #callbacks
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special)

    #mainloop
    glutMainLoop()
