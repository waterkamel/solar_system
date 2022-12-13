# Author: Emmanuel Makau
# Date: 10/22/2022
# Purpose: Body class
# Kasuti Kreations

from cs1lib import *

class Body:
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.pixel_radius = pixel_radius
        self.r = r
        self.g = g
        self.b = b

    #Updates the position of the body
    def update_position(self, timestep):
        self.x = self.x + self.vx * timestep
        self.y = self.y + self.vy * timestep

    #Updates the velocities on acceleration
    def update_velocity(self, ax, ay, timestep):
        self.vx = self.vx + ax * timestep
        self.vy = self.vy + ay * timestep

    #Draws the body
    def draw(self, cx, cy, pixels_per_meter):
        pixel_x = cx + (self.x * pixels_per_meter)
        pixel_y = cy + (self.y * pixels_per_meter)
        pixel_r = self.pixel_radius

        set_fill_color(self.r, self.g, self.b)
        draw_circle(pixel_x, pixel_y, pixel_r)
