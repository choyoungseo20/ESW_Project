import numpy as np
import math

class AssignmentArrow:
    def __init__(self):
        self.appearance = 'retro'
        self.state = None
        self.speed = 7
        self.position = None
        self.direction = None
        self.magnitude = None
        self.velocity = None

    def run(self, start_position, other_position):
        self.state = 'alive'
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
            user.state = 'die'
            self.state = 'die'

    def overlap(self, ego_position, other_position):
        '''
        두개의 사각형(bullet position, enemy position)이 겹치는지 확인하는 함수
        좌표 표현 : [x1, y1, x2, y2]
        
        return :
            True : if overlap
            False : if not overlap
        '''
        if ego_position[0] + 6 < other_position[0] - 10 or ego_position[0] > other_position[0] + 10 or ego_position[1] + 6 < other_position[1] - 10 or ego_position[1] > other_position[1] + 10:
            return False  # 겹치지 않음
        return True  # 겹침
    

    
    