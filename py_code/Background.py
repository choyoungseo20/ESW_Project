import numpy as np

class Flower:
    def __init__(self, x, y):
        self.position = np.array([x, y])
        self.pixel_map = [
            ".r.",
            "ryr",
            "srs",
            ".s.",
            ]

    
    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "r":
                    x0 = x_start + x * 6
                    y0 = y_start + y * 6
                    draw_tool.rectangle([x0, y0, x0 + 6, y0 + 6], fill = (203, 218, 218)) # (255, 30, 39)
                if pixel == "s":
                    x0 = x_start + x * 6
                    y0 = y_start + y * 6
                    draw_tool.rectangle([x0, y0, x0 + 6, y0 + 6], fill = (148, 200, 70))
                if pixel == "y":
                    x0 = x_start + x * 6
                    y0 = y_start + y * 6
                    draw_tool.rectangle([x0, y0, x0 + 6, y0 + 6], fill = (255, 242, 0))


class Grass:
    def __init__(self, x, y):
        self.position = np.array([x, y])
        self.pixel_map = [
            ".....g.",
            ".g..g..",
            "..g.g.s",
            "s.g.ss.",
            ".ss....",
            ]

    
    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "g":
                    x0 = x_start + x * 6
                    y0 = y_start + y * 6
                    draw_tool.rectangle([x0, y0, x0 + 6, y0 + 6], fill = (16, 168, 87))
                if pixel == "s":
                    x0 = x_start + x * 6
                    y0 = y_start + y * 6
                    draw_tool.rectangle([x0, y0, x0 + 6, y0 + 6], fill = (148, 200, 70))


class Dot1:
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
                    draw_tool.rectangle([x0, y0, x0 + 6, y0 + 6], fill = (208, 242, 116))


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

