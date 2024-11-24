import numpy as np

class Portal:
    def __init__(self):
        self.state = None
        self.position = None

    def run(self, x, y):
        self.state = 'alive'
        self.position = np.array([x, y])

    def collision_check(self, user):
        collision = self.overlap(self.position, user.center)
            
        if collision:
            self.state = 'die'
            user.term += 1

    def overlap(self, ego_position, other_position):

        if (ego_position[0] - other_position[0])**2 + (ego_position[1] - other_position[1])**2 >= (12 + 14)**2:
            return False  # 겹치지 않음
        return True  # 겹침