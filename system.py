# Author: Emmanuel Makau
# Date: 11/1/2022
# Purpose: System class
# Kasuti Kreations

from body import Body
from math import sqrt

#Global value
G = 6.67384e-11

class System:
    #Create instance body_list
    def __init__(self, body_list):
        self.body_list = body_list

    #Updates bodies in the list
    def update(self, timestep):

        for body in self.body_list:
            (ax, ay) = self.acceleration(body)     # uses returned values from acceleration
            body.update_velocity(ax, ay, timestep) # Updates velocity of each body
            body.update_position(timestep)         # Updates position of each body

    # Calculates acceleration between bodies j and n and return their total acceleration towards x and y
    def acceleration(self, n):
        global G
        total_ax = 0
        total_ay = 0
        for j in self.body_list:
            if j != n:
                dx = j.x - n.x               # x distance between two bodies
                dy = j.y - n.y               # y distance between two bodies
                r = sqrt(dx * dx + dy * dy)  # total distance between the two planets
                a = G * j.mass / (r * r)     # total acceleration
                ax = a * dx / r
                ay = a * dy / r
                total_ax = total_ax + ax     # total acceleration for x
                total_ay = total_ay + ay     # total acceleration for y
        return (total_ax, total_ay)

    # Draws the bodies
    def draw(self, cx, cy, pixel_per_meter):
        for body in self.body_list:
            body.draw(cx, cy, pixel_per_meter)
