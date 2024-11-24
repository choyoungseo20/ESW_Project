import numpy as np
import math

class AssignmentArrow:
    def __init__(self):
        self.state = None
        self.item1 = None
        self.speed = 7
        self.position = None
        self.direction = None
        self.magnitude = None
        self.velocity = None

    def run(self, start_position, other_position):
        self.state = 'alive'
        self.item1 = False
        self.position = np.array([start_position[0], start_position[1]])
        self.direction = np.array([other_position[0] - start_position[0], other_position[1] - start_position[1]])
        self.magnitude = math.sqrt(self.direction[0]**2 + self.direction[1]**2)
        self.velocity = np.array([(self.direction[0] / self.magnitude) * self.speed, (self.direction[1] / self.magnitude) * self.speed])


    def move(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def collision_check(self, user):
        collision = self.overlap(self.position, user.center)
            
        if collision:
            self.state = 'die'
            if self.item1:
                user.grade += 0
            else:
                user.grade += 1

    def overlap(self, ego_position, other_position):

        if (ego_position[0] - other_position[0])**2 + (ego_position[1] - other_position[1])**2 >= (12 + 3)**2:
            return False  # 겹치지 않음
        return True  # 겹침
    

    
    