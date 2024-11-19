import numpy as np

class GreatNote:
    def __init__(self):
        self.state = None
        self.position = None
        self.center = None
        self.pixel_map = [
            "bbbbbbbbbbbbb..",
            "byyyyyyyyyyybb.",
            "byyyyyyyyyyybwb",
            "byyyyybyyyyybwb",
            "byyyybybyyyybwb",
            "byyybyyybyyybwb",
            "byyybyyybyyybwb",
            "byyyyyyyyyyybwb",
            "byybbbbbbbyybwb",
            "byyyyybyyyyybwb",
            "byyyyybyyyyybwb",
            "byyyyyyyyyyybwb",
            "byyyyyyyyyyybwb",
            "bbbbbbbbbbbbbwb",
            ".bwwwwwwwwwwwwb",
            "..bbbbbbbbbbbbb",
        ]

    def run(self, x, y):
        self.state = 'alive'
        self.position = np.array([x, y])
        self.center = np.array([self.position[0] + 16, self.position[1] + 16])

    
    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "y":
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (255, 242, 0))
                if pixel == "b":
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (0, 0, 0))
                if pixel == "w":
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (255, 255, 255))

    def collision_check(self, user):
        collision = self.overlap(self.center, user.center)
            
        if collision:
            self.state = 'die'

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

        if (ego_position[0] - other_position[0])**2 + (ego_position[1] - other_position[1])**2 >= (12 + 16)**2:
            return False  # 겹치지 않음
        return True  # 겹침


class PastExam:
    def __init__(self):
        self.state = None
        self.position = None
        self.center = None
        self.pixel_map = [
            "...bbbbbbbbbbbb",
            "..bgggggrgggrgb",
            ".bgggggrgrgrrrb",
            "bggggggrrrggrgb",
            "bggggggrgrggggb",
            "bgggggggggggggb",
            "bgggggggggggggb",
            "bgbbbbbbbbrbbgb",
            "bggggggggrrgggb",
            "bggrggggrrggggb",
            "bgbrrbbrrbbbbgb",
            "bgggrrrrggggggb",
            "bggggrrgggggggb",
            "bgbbbbbbbbbbbgb",
            "bgggggggggggggb",
            "bbbbbbbbbbbbbbb",
        ]

    def run(self, x, y):
        self.state = 'alive'
        self.position = np.array([x, y])
        self.center = np.array([self.position[0] + 16, self.position[1] + 16])

    
    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "r":
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (255, 0, 0))
                if pixel == "b":
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (0, 0, 0))
                if pixel == "g":
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (255, 255, 255))

    def collision_check(self, user):
        collision = self.overlap(self.center, user.center)
            
        if collision:
            self.state = 'die'

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

        if (ego_position[0] - other_position[0])**2 + (ego_position[1] - other_position[1])**2 >= (12 + 16)**2:
            return False  # 겹치지 않음
        return True  # 겹침