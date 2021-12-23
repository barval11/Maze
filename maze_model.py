from OpenGL.GL import *
from OpenGL.GLUT import *


#Warna
GREEN = (0.0, 1.0, 0.0)
BLUE = (0.0, 0.0, 1.0)

#Perputaran arah mobil
degrees = {
    0: 0,
    1: 90,
    2: 180,
    3: 270,
}

# Mencerminkan objek
def mirror(iterable):
    return iterable + [(-v[0], v[1]) for v in iterable[::-1]]


class Object(object):
    mode = GL_POLYGON

    def centroide(self):
        x_total = 0
        y_total = 0
        len_ = len(self.vertices)
        for x, y in self.vertices:
            x_total += x
            y_total += y
        return  (x_total / len_, y_total / len_)

    def draw(self):
        if hasattr(self, 'color'):
            glColor3f(*self.color)
        if hasattr(self, 'vertices'):
            glBegin(self.mode)
            for x, y in self.vertices:
                glVertex3f(x, y, 0)
            glEnd()
        if hasattr(self, 'objects'):
            for item, x, y in self.objects:
                glTranslated(x, y, 0)
                item.draw()


class Obstacle(Object):
    color = GREEN
    vertices = [
        (0, 40), 
        (0, 100), 
        (80, 100), 
        (80, 40)
    ]


class Obstacle2(Object):
    color = GREEN
    vertices = [
        (40, 140),
        (200, 140),
        (200, 300),
        (40, 300)
    ]


class Obstacle3(Object):
    color = GREEN
    vertices = [
        (120, 0),
        (400, 0),
        (400, 100),
        (120, 100)
    ]


class Obstacle4(Object):
    color = GREEN
    vertices = [
        (440, 40),
        (560, 40),
        (560, 200),
        (440, 200)
    ]


class Obstacle5(Object):
    color = GREEN
    vertices = [
        (240, 140),
        (400, 140),
        (400, 260),
        (240, 260)
    ]


class Obstacle6(Object):
    color = GREEN
    vertices = [
        (500, 240),
        (600, 240),
        (600, 400),
        (500, 400)
    ]


class Obstacle7(Object):
    color = GREEN
    vertices = [
        (350, 240),
        (460, 240),
        (460, 400),
        (350, 400)
    ]


class Obstacle8(Object):
    color = GREEN
    vertices = [
        (460, 440),
        (600, 440),
        (600, 560),
        (460, 560)
    ]


class Obstacle9(Object):
    color = GREEN
    vertices = [
        (240, 300),
        (310, 300),
        (310, 400),
        (240, 400)
    ]


class Obstacle10(Object):
    color = GREEN
    vertices = [
        (240, 340),
        (100, 340),
        (100, 560),
        (240, 560)
    ]


class Obstacle11(Object):
    color = GREEN
    vertices = [
        (280, 440),
        (420, 440),
        (420, 600),
        (280, 600)
    ]


class Obstacle12(Object):
    color = GREEN
    vertices = [
        (0, 340),
        (60, 340),
        (60, 420),
        (0, 420)
    ]


class Obstacle13(Object):
    color = GREEN
    vertices = [
        (0, 460),
        (60, 460),
        (60, 600),
        (0, 600)
    ]


class Wheel(Object):
    color = (1, 1, 1)
    vertices = mirror([
        (-2.5, 5),
        (-5, 2.5),
        (-5, -2.5),
        (-2.5, -5),
    ])


class Car(Object):
    vertices = mirror([
        (-10, 25),
        (-15, 15),
        (-30, 15),
        (-30, 5),
    ])
    
    #Posisi roda
    objects = [
        (Wheel(), -20, 5),
        (Wheel(), 40, 0),
    ]
    rotate = 0
    mirror = False

    def __init__(self, x, y, color = BLUE):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        c = self.centroide()
        glLoadIdentity()
        glTranslated(self.x + c[0], self.y + c[1], 0)
        if self.mirror:
            glScaled(-1, 1, 1)
        glRotate(degrees[self.rotate], 0, 0, 1)
        glTranslated(-c[0], -c[1], 0)
        super(Car, self).draw()

        
