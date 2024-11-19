import numpy as np

class Term1_1:
    def __init__(self):
        self.position = None
        self.size = None
        self.pixel_map = [
            "..d.........d..",
            ".dd........dd..",
            "..d.........d..",
            "..d...ddd...d..",
            "..d.........d..",
            "..d.........d..",
            ".ddd.......ddd.",
            ]
    
    def setSize(self, x, y, size):
        self.position = np.array([x, y])
        self.size = size

    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "d":
                    x0 = x_start + x * self.size
                    y0 = y_start + y * self.size
                    draw_tool.rectangle([x0, y0, x0 + self.size, y0 + self.size], fill = (100, 100, 100))


class Term1_2:
    def __init__(self):
        self.position = None
        self.size = None
        self.pixel_map = [
            "..d........ddd.",
            ".dd.......d...d",
            "..d...........d",
            "..d...ddd....d.",
            "..d.........d..",
            "..d........d...",
            ".ddd......ddddd",
            ]

    def setSize(self, x, y, size):
        self.position = np.array([x, y])
        self.size = size

    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "d":
                    x0 = x_start + x * self.size
                    y0 = y_start + y * self.size
                    draw_tool.rectangle([x0, y0, x0 + self.size, y0 + self.size], fill = (100, 100, 100))


class Term2_1:
    def __init__(self):
        self.position = None
        self.size = None
        self.pixel_map = [
            ".ddd........d..",
            "d...d......dd..",
            "....d.......d..",
            "...d..ddd...d..",
            "..d.........d..",
            ".d..........d..",
            "ddddd......ddd.",
            ]

    def setSize(self, x, y, size):
        self.position = np.array([x, y])
        self.size = size

    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "d":
                    x0 = x_start + x * self.size
                    y0 = y_start + y * self.size
                    draw_tool.rectangle([x0, y0, x0 + self.size, y0 + self.size], fill = (100, 100, 100))


class Term2_2:
    def __init__(self):
        self.position = None
        self.size = None
        self.pixel_map = [
            ".ddd.......ddd.",
            "d...d.....d...d",
            "....d.........d",
            "...d..ddd....d.",
            "..d.........d..",
            ".d.........d...",
            "ddddd.....ddddd",
            ]

    def setSize(self, x, y, size):
        self.position = np.array([x, y])
        self.size = size

    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "d":
                    x0 = x_start + x * self.size
                    y0 = y_start + y * self.size
                    draw_tool.rectangle([x0, y0, x0 + self.size, y0 + self.size], fill = (100, 100, 100))


class Term3_1:
    def __init__(self):
        self.position = None
        self.size = None
        self.pixel_map = [
            ".ddd........d..",
            "d...d......dd..",
            "....d.......d..",
            "..dd..ddd...d..",
            "....d.......d..",
            "d...d.......d..",
            ".ddd.......ddd.",
            ]

    def setSize(self, x, y, size):
        self.position = np.array([x, y])
        self.size = size

    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "d":
                    x0 = x_start + x * self.size
                    y0 = y_start + y * self.size
                    draw_tool.rectangle([x0, y0, x0 + self.size, y0 + self.size], fill = (100, 100, 100))


class Term3_2:
    def __init__(self):
        self.position = None
        self.size = None
        self.pixel_map = [
            ".ddd.......ddd.",
            "d...d.....d...d",
            "....d.........d",
            "..dd..ddd....d.",
            "....d.......d..",
            "d...d......d...",
            ".ddd......ddddd",
            ]

    def setSize(self, x, y, size):
        self.position = np.array([x, y])
        self.size = size

    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "d":
                    x0 = x_start + x * self.size
                    y0 = y_start + y * self.size
                    draw_tool.rectangle([x0, y0, x0 + self.size, y0 + self.size], fill = (100, 100, 100))


class Term4_1:
    def __init__(self):
        self.position = None
        self.size = None
        self.pixel_map = [
            "...d........d..",
            "..dd.......dd..",
            ".d.d........d..",
            "d..d..ddd...d..",
            "ddddd.......d..",
            "...d........d..",
            "...d.......ddd.",
            ]

    def setSize(self, x, y, size):
        self.position = np.array([x, y])
        self.size = size

    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "d":
                    x0 = x_start + x * self.size
                    y0 = y_start + y * self.size
                    draw_tool.rectangle([x0, y0, x0 + self.size, y0 + self.size], fill = (100, 100, 100))


class Term4_2:
    def __init__(self):
        self.position = None
        self.size = None
        self.pixel_map = [
            "...d.......ddd.",
            "..dd......d...d",
            ".d.d..........d",
            "d..d..ddd....d.",
            "ddddd.......d..",
            "...d.......d...",
            "...d......ddddd",
            ]

    def setSize(self, x, y, size):
        self.position = np.array([x, y])
        self.size = size

    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "d":
                    x0 = x_start + x * self.size
                    y0 = y_start + y * self.size
                    draw_tool.rectangle([x0, y0, x0 + self.size, y0 + self.size], fill = (100, 100, 100))
