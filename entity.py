from OpenGL.GL import *
from OpenGL.GLU import *

import config
import models

class Entity:
    def __init__(self, pos, rot=(0, 0, 0, 0),
                 verts=models.cube_verts, edges=models.cube_edges, faces=models.cube_faces,
                 color_e=(1, 1, 1), color_f=(1, 0, 0),
                 radius=models.cube_radius):
        self.verts = verts
        self.edges = edges
        self.faces = faces
        self.color_e = color_e
        self.color_f = color_f
        self.pos = pos
        self.rot = rot
        self.radius = radius

    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1], self.pos[2])
        glRotatef(self.rot[0], self.rot[1], self.rot[2],self.rot[3])

        glBegin(GL_QUADS)
        glColor3fv(self.color_f)
        for face in self.faces:
            for vert in face:
                glVertex3fv(self.verts[vert])
        glEnd()

        glBegin(GL_LINES)
        glColor3fv(self.color_e)
        for edge in self.edges:
            for vert in edge:
                glVertex3fv(self.verts[vert])
        glEnd()
        glPopMatrix()
