import numpy as np

class GameEnd1:
    def __init__(self):
        self.position = np.array([3, 20])
        self.pixel_map = [
            "........................................",
            "...aaaaaabcccccccccccccccccccccccd......",
            "..caaaaaabcccccccccccccccccccccccdd.....",
            ".ccceeeeeebfffffffffffffeeeeeeeeebddd...",
            "ccceeeeeeeebfffffffffffeeeeeeeeeeebddd..",
            "aceeebbbeebeefffbbbbbfebbbeebbbbeeebdg..",
            "aaeebeeebebeeeffbffffebeeebebeeebeebgg..",
            ".aaebeeebebeeeefbfffeebeeebebeeebeebgg..",
            ".aaebeeebebeffffbffefebeeebebeeebeffbgg.",
            ".aaebeeeeebfffffbbbbbfbbbbbebbbbbfffbgg.",
            "..aabeeeffbffffebfffffbeeebebbeeffffbgg.",
            "..aabeefbfbfffefbfffffbfeebebfbfffffbgg.",
            "..ccbfffbfbhhhhhbhhhffbffebfbffbffffbgg.",
            ".ccfbfffbhbhhhhhbhhhhhbhhhbfbfffbfffbgg.",
            "ccfffbbbiibbbbbibbbbbhbhhhbfbfffbfffbgg.",
            ".aaffiiiiiiiiiiiiiiiiiiiiiiiiiiffffbgg..",
            ".aafiiiiiiiiiiiiiiiiiiiiiiiiiiiiiibgg...",
            "..ggbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbgg...",
            "...ggggggggggggggjjjgggggggggggggggg....",
            "....ggggggggggggjjj..gggggggggggggg.....",
            ]

    
    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "a":
                    x0 = x_start + x * 6
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 6, y0 + 4], fill = (168, 168, 168))
                if pixel == "b":
                    x0 = x_start + x * 6
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 6, y0 + 4], fill = (203, 203, 203))
                if pixel == "c":
                    x0 = x_start + x * 6
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 6, y0 + 4], fill = (191, 191, 191))
                if pixel == "d":
                    x0 = x_start + x * 6
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 6, y0 + 4], fill = (140, 140, 140))
                if pixel == "e":
                    x0 = x_start + x * 6
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 6, y0 + 4], fill = (163, 163, 163))
                if pixel == "f":
                    x0 = x_start + x * 6
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 6, y0 + 4], fill = (158, 158, 158))
                if pixel == "g":
                    x0 = x_start + x * 6
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 6, y0 + 4], fill = (100, 100, 100))
                if pixel == "h":
                    x0 = x_start + x * 6
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 6, y0 + 4], fill = (150, 150, 150))
                if pixel == "i":
                    x0 = x_start + x * 6
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 6, y0 + 4], fill = (145, 145, 145))
                if pixel == "j":
                    x0 = x_start + x * 6
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 6, y0 + 4], fill = (90, 90, 90))