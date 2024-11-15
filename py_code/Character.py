import numpy as np

class Character:
    def __init__(self, width, height):
        self.appearance = 'retro'
        self.state = None
        self.position = np.array([width//2 - 18, height//2 - 18])
        self.center = np.array([self.position[0] + 16, self.position[1] + 16])
        self.pixel_map = [
            ".........ddddddddd......",
            "........dgggggggggd.....",
            "........dgggggggggd.....",
            ".......dgggggggggd......",
            "......dddddddddddd......",
            "....ddbbbbbbbbbbbbdd....",
            "..ddbbbbddbbbbbbbbbbdd..",
            ".ddbbbbbddbbbbbbbddbbdd.",
            ".dbbddbbbbbbbbbbbddbbbd.",
            "dbbbddbbbbbbbbbbbbbbbbbd",
            "dbbbbbbsssssssssssbbbbbd",
            "dbbbbsssssssssssssssbbbd",
            "dbbbsssssssssssssssssbbd",
            "dbssssddssssssssddssssbd",
            "dbssssddssssssssddssssbd",
            "dbssssddssssssssddssssbd",
            "dbspppsssssddssssspppsbd",
            "dbspppsssssddssssspppsbd",
            "dbssssssddddddddssssssbd",
            "dbssssssddddddddssssssbd",
            ".dssssssssssssssssssssd.",
            "..ddssssssssssssssssdd..",
            "....ddssssssssssssdd....",
            "......dddddddddddd......",
        ]

    def move(self, command = None):
        if command['move'] == False:
            self.state = None
        
        else:
            self.state = 'move'

            if command['up_pressed']:
                if self.position[1] - 10 > 0:
                    self.position[1] -= 10
                else:
                    self.position[1] = 0

            if command['down_pressed']:
                if self.position[1] + 10 < 200:
                    self.position[1] += 10
                else:
                    self.position[1] = 208

            if command['left_pressed']:
                if self.position[0] > 0:
                    self.position[0] -= 10
                else:
                    self.position[0] = 0
                
            if command['right_pressed']:
                if self.position[0] < 200:
                    self.position[0] += 10
                else:
                    self.position[0] = 208
    
    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "d":
                    x0 = x_start + x
                    y0 = y_start + y
                    draw_tool.rectangle([x0, y0, x0 + 1, y0 + 1], fill = (0, 0, 0))
                if pixel == "b":
                    x0 = x_start + x
                    y0 = y_start + y
                    draw_tool.rectangle([x0, y0, x0 + 1, y0 + 1], fill = (219, 188, 130))
                if pixel == "s":
                    x0 = x_start + x
                    y0 = y_start + y
                    draw_tool.rectangle([x0, y0, x0 + 1, y0 + 1], fill = (254, 224, 172))
                if pixel == "g":
                    x0 = x_start + x
                    y0 = y_start + y
                    draw_tool.rectangle([x0, y0, x0 + 1, y0 + 1], fill = (34, 177, 76))
                if pixel == "p":
                    x0 = x_start + x
                    y0 = y_start + y
                    draw_tool.rectangle([x0, y0, x0 + 1, y0 + 1], fill = (255, 174, 201))