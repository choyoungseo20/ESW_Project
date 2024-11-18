import numpy as np
import math

class Exam:
    def __init__(self):
        self.appearance = 'retro'
        self.state = None      
        self.speed = None
        self.position = None
        self.center = None
        self.pixel_map = [
            ".bbbbbbbbbbb.",
            "bwwwwwwwwwwwb",
            "bwrwwrwwwrwwb",
            "bwrwrwrwrwrwb",
            "bwrwrwrwrwrwb",
            "bwrwwrwwwrwwb",
            "bwwwwwwwwwwwb",
            "bwbbbbwbbbbb.",
            "bwwwwwbwwwwwb",
            "bwbbbwbwwbwwb",
            "bwwwwwbwwbwwb",
            "bwwwwwbwwwwwb",
            ".bbbbb.bbbbb.",
        ]

    def run(self, x, y, speed):
        self.state = 'alive'
        self.speed = speed
        self.position = np.array([x, y])
        self.center = np.array([self.position[0] + 18, self.position[1] + 18])

    def move(self, target_position):
        """
        direction = np.array([target_position[0] - self.center[0], target_position[1] - self.center[1]])
        magnitude = math.sqrt(direction[0]**2 + direction[1]**2)
        velocity = np.array([(direction[0] / magnitude) * self.speed, (direction[1] / magnitude) * self.speed])
        self.position[0] += velocity[0]
        self.position[1] += velocity[1]

        self.center = np.array([self.position[0] + 18, self.position[1] + 18])

        """
        if self.center[1] >= target_position[1]:
            if self.center[1] - target_position[1] >= self.speed:
                self.position[1] -= self.speed
            else:
                self.position[1] -= self.center[1] - target_position[1]
        else:
            if target_position[1] - self.center[1] >= self.speed:
                self.position[1] += self.speed
            else:
                self.position[1] += target_position[1] - self.center[1]

        if self.center[0] >= target_position[0]:
            if self.center[0] - target_position[0] >= self.speed:
                self.position[0] -= self.speed
            else:
                self.position[0] -= self.center[0] - target_position[0]
        else:
            if target_position[0] - self.center[0] >= self.speed:
                self.position[0] += self.speed
            else:
                self.position[0] += target_position[0] - self.center[0]
        
        self.center = np.array([self.position[0] + 18, self.position[1] + 18])
        

    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "r":
                    x0 = x_start + x * 3
                    y0 = y_start + y * 3
                    draw_tool.rectangle([x0, y0, x0 + 3, y0 + 3], fill = (255, 0, 0))
                if pixel == "b":
                    x0 = x_start + x * 3
                    y0 = y_start + y * 3
                    draw_tool.rectangle([x0, y0, x0 + 3, y0 + 3], fill = (0, 0, 0))
                if pixel == "w":
                    x0 = x_start + x * 3
                    y0 = y_start + y * 3
                    draw_tool.rectangle([x0, y0, x0 + 3, y0 + 3], fill = (255, 255, 255))

    def collision_check(self, user):
        collision = self.overlap(self.center, user.center)
            
        if collision:
            self.state = 'die'
            user.grade += 2

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

        if (ego_position[0] - other_position[0])**2 + (ego_position[1] - other_position[1])**2 >= (18)**2:
            return False  # 겹치지 않음
        return True  # 겹침