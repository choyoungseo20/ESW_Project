import numpy as np

class Dot2:
    def __init__(self, x, y):
        self.position = np.array([x, y])
        self.pixel_map = [
            "."
            ]

    
    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == ".":
                    x0 = x_start + x * 6
                    y0 = y_start + y * 6
                    draw_tool.rectangle([x0, y0, x0 + 6, y0 + 6], fill = (102, 156, 62))