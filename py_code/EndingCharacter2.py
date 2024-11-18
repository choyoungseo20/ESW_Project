import numpy as np

class EndingCharacter2:
    def __init__(self):
        self.position = None
        self.size = None
        self.pixel_map = [
            "...............ddddddd..............",
            "..............ddddddddd.............",
            ".............ddgggggggdd............",
            ".............ddgggggggdd............",
            "............ddgggggggdd.............",
            "..........dddgggggggdddd............",
            ".........ddbbbbbbbbbbbbbdd..........",
            "........ddbbbbbbbbbbbbbbbdd.........",
            ".......ddbbbbbbbbbbbbbddbbdd........",
            "......ddbbbbbbbbbbbbbbddbbbdd.......",
            ".....ddbbbbbbbbbbbbddbbbbbbbdd......",
            "....ddbbddbbbbbbbbbddbbbddbbbdd.....",
            "...ddbbbddbbbbbbbbbbbbbbddbbbbdd....",
            "...ddbbbbbbbbbbsssssssssbbbbbbdd....",
            "..ddbbbbbbbbsssssssssssssbbbbbdd....",
            "..ddbbbbbbbsssssssssssssssbbbbdd....",
            "..ddbbbbbbsssssssssssssssssbbbbdd...",
            ".ddbbbwwwwsssssssssssssssswwwwbbdd..",
            ".ddbbwwwwwddddssssssssddddwwwwwbdd..",
            ".dddwwwwwwwwddssssssssddwwwwwwwwbdd.",
            "ddswwwwsspppsssssddssssspppsswwwwssd",
            "ddwwwwbsspppsssssddssssspppssbwwwwsd",
            "dwwwwwbbbsssssddddddddsssssbbbwwwwwd",
            "dwwwwwbbbsssssddddddddsssssbbbwwwwwd",
            "dwwwwwddbbbssssssssssssssbbbbbwwwwwd",
            "dwwwwwddbbbssssssssssssssbbbbdwwwwwd",
            ".wwwwwbbbbbbbbbbbbbbbbbbbbbbbdwwwww.",
            ".wwwwwbbddbbbbbbbbbbbbbbbbddbbwwwww.",
            ".wwwwwbbddbbbbbbbbbbbbbbbbddbbwwwww.",
            ".wwwwwbbbbbbbbbbbbbbbbbbbbbbbbwwwww.",
            ".wwwwwdbbbbbbbbbbbbbbbbbbbbbbdwwwww.",
            ".wwwwwddbbbbbbbbbbbbbbbbbbbbddwwwww.",
            ".wwwww..ddsssssddddddsssssdd..wwwww.",
            ".wwwww..ddsssssdd..ddsssssdd..wwwww.",
            "wwwwww.wwddddddd....dddddddww.wwwwww",
            "wwwwwwww..ddddd......ddddd..wwwwwwww",
        ]

    def move(self, x, y, size):
        self.position = np.array([x, y])
        self.size = size

    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "d":
                    x0 = x_start + x * self.size
                    y0 = y_start + y * self.size
                    draw_tool.rectangle([x0, y0, x0 + self.size, y0 + self.size], fill = (0, 0, 0))
                if pixel == "b":
                    x0 = x_start + x * self.size
                    y0 = y_start + y * self.size
                    draw_tool.rectangle([x0, y0, x0 + self.size, y0 + self.size], fill = (219, 188, 130))
                if pixel == "s":
                    x0 = x_start + x * self.size
                    y0 = y_start + y * self.size
                    draw_tool.rectangle([x0, y0, x0 + self.size, y0 + self.size], fill = (254, 224, 172))
                if pixel == "g":
                    x0 = x_start + x * self.size
                    y0 = y_start + y * self.size
                    draw_tool.rectangle([x0, y0, x0 + self.size, y0 + self.size], fill = (34, 177, 76))
                if pixel == "p":
                    x0 = x_start + x * self.size
                    y0 = y_start + y * self.size
                    draw_tool.rectangle([x0, y0, x0 + self.size, y0 + self.size], fill = (255, 174, 201))
                if pixel == "w":
                    x0 = x_start + x * self.size
                    y0 = y_start + y * self.size
                    draw_tool.rectangle([x0, y0, x0 + self.size, y0 + self.size], fill = (83, 176, 231))