import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

######
import random

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 1, 0),
    (1, 1, 1),
    (0, 1, 1),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 0),
    (1, 1, 1),
    (0, 1, 1),
)


floor = (
    (-10,-0.1,20),
(10,-0.1,20),
(-10,-0.1,-300),
(10,-0.1,-300)


)


def set_vertrices(maxDistance):
    xValue = random.randrange(-10,10)
    yValue = 0#random.randrange(-10,10)
    zValue = random.randrange(-1*maxDistance,-20)

    newVertices = []

    for vert in vertices:
        newVert = [vert[0]+xValue ,
                   vert[1]+yValue,
                   vert[2]+zValue]

        newVertices.append(newVert)

    return newVertices


def floor(vertexs):
    glBegin(GL_QUADS)

    for vertex in surfaces[0]:
        glVertex3fv(vertices[vertex])

    glEnd()

def Cube(vertices):
    glBegin(GL_QUADS)

    for surface in surfaces:
        x = 0

        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])

    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50)

    # start further back
    glTranslatef(random.randrange(-5, 5), 0, -30)

    xMove = 0
    yMove = 0

    maxDistance = 300
    cubeDict = {}

    for x in range(75):
        cubeDict[x] = set_vertrices(maxDistance)

    # no more rotate
    # glRotatef(25, 2, 1, 0)

    object_passed = False

    while not object_passed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(0.5, 0, 0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(-0.5, 0, 0)

                if event.key == pygame.K_UP:
                    glTranslatef(0, 1, 0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, -1, 0)
            '''
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1.0)

                if event.button == 5:
                    glTranslatef(0,0,-1.0)
            '''

        x = glGetDoublev(GL_MODELVIEW_MATRIX)  # , modelviewMatrix)

        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]

        # print(camera_x,camera_y,camera_z)

        # slowly move:
        glTranslatef(0, 0, 0.5)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


        floor(floor)

        for cube in cubeDict:

            Cube(cubeDict[cube])



        pygame.display.flip()





main()