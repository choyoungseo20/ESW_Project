import numpy as np

class Info:
    def __init__(self):
        self.position = np.array([90, 180])
        self.pixel_map = [
            "ddd..ddd..dddd..dddd..dddd....dd....ddddd.dd....ddd..d.....dd..d...d",
            "d..d.d..d.d....d.....d.......d..d.....d..d..d...d..d.d....d..d.d...d",
            "ddd..ddd..dddd..ddd...ddd....dddd.....d..d..d...ddd..d....dddd..d.d.",
            "d....d.d..d........d.....d...d..d.....d..d..d...d....d....d..d...d..",
            "d....d..d.dddd.dddd..dddd....d..d.....d...dd....d....dddd.d..d...d..",
        ]

    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "d":
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (0, 0, 0))
