import numpy as np
import math

class Exam:
    def __init__(self):
        self.state = None
        self.item2 = None  
        self.speed = None
        self.position = None
        self.center = None
        self.pixel_map1 = [
            ".bbbbbbbbbbb.",
            "bwwwwwwwwwwwb",
            "bwwwwwrwwwwwb",
            "bwwwwrwrwwwwb",
            "bwwwwrwrwwwwb",
            "bwwwwwrwwwwwb",
            "bwwwwwwbbbbb.",
            "bwbbbwbwwwwwb",
            "bwwwwwbwwbwwb",
            "bwbbbwbwwbwwb",
            "bwwwwwbwwwbwb",
            "bwwwwwbwwwwwb",
            ".bbbbb.bbbbb.",
        ]
        self.pixel_map2 = [
            ".bbbbbbbbbbb.",
            "bwwwwwwwwwwwb",
            "bwrwwrwwwrwwb",
            "bwrwrwrwrwrwb",
            "bwrwrwrwrwrwb",
            "bwrwwrwwwrwwb",
            "bwwwwwwbbbbb.",
            "bwbbbwbwwwwwb",
            "bwwwwwbwwbwwb",
            "bwbbbwbwwbwwb",
            "bwwwwwbwwwbwb",
            "bwwwwwbwwwwwb",
            ".bbbbb.bbbbb.",
        ]

    def run(self, x, y, speed):
        self.state = 'alive'
        self.item2 = False 
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
        if self.item2:
            pixel_map = self.pixel_map2
        else:
            pixel_map = self.pixel_map1
        for y, row in enumerate(pixel_map):
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
            if self.item2:
                if user.grade >= 2:
                    user.grade -= 2
                else:
                    user.grade = 0
            else:
                user.grade += 2

    def overlap(self, ego_position, other_position):

        if (ego_position[0] - other_position[0])**2 + (ego_position[1] - other_position[1])**2 >= (18)**2:
            return False  # 겹치지 않음
        return True  # 겹침