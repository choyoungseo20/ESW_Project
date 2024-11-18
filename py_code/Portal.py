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
        '''
        두개의 사각형(bullet position, enemy position)이 겹치는지 확인하는 함수
        좌표 표현 : [x1, y1, x2, y2]
        
        return :
            True : if overlap
            False : if not overlap
        '''
        # if ego_position[0] + 36 < other_position[0] or ego_position[0] > other_position[0] or ego_position[1] + 36 < other_position[1] or ego_position[1] > other_position[1]:
        #     return False  # 겹치지 않음
        # return True  # 겹침

        if (ego_position[0] - other_position[0])**2 + (ego_position[1] - other_position[1])**2 >= (12 + 12)**2:
            return False  # 겹치지 않음
        return True  # 겹침