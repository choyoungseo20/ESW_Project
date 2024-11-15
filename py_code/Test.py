import numpy as np

class Test:
    def __init__(self):
        self.appearance = 'retro'
        self.state = None
        self.position = np.array([0, 0])
        self.center = np.array([self.position[0] + 18, self.position[1] + 18])
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
            ".ddbbbbbssssddssssssssddsssssbbbdd..",
            ".ddbbbbsssssddssssssssddsssssbbbdd..",
            ".dddbbbsssssddssssssssddsssssbbbbdd.",
            "ddssbbbsspppsssssddssssspppssbbbssdd",
            "ddssbbbsspppsssssddssssspppssbbbssdd",
            "ddssbbbbbsssssddddddddsssssbbbbbssdd",
            "ddssbbbbbsssssddddddddsssssbbbbbssdd",
            "ddssbbddbbbssssssssssssssbbbbbbbssdd",
            "ddssbbddbbbssssssssssssssbbbbddbssdd",
            ".dddbbbbbbbbbbbbbbbbbbbbbbbbbddbddd.",
            "..ddbbbbddbbbbbbbbbbbbbbbbddbbbbdd..",
            "...ddbbbddbbbbbbbbbbbbbbbbddbbbdd...",
            "....ddbbbbbbbbbbbbbbbbbbbbbbbbdd....",
            ".....ddbbbbbbbbbbbbbbbbbbbbbbdd.....",
            "......ddbbbbbbbbbbbbbbbbbbbbdd......",
            "........ddsssssddddddsssssdd........",
            "........ddsssssdd..ddsssssdd........",
            ".........ddddddd....ddddddd.........",
            "..........ddddd......ddddd..........",
        ]

    def move(self, pos):
        if self.center[1] >= pos[1]:
            if self.center[1] - pos[1] >= 3:
                self.position[1] -= 3
            else:
                self.position[1] -= self.center[1] - pos[1]
        else:
            if pos[1] - self.center[1] >= 3:
                self.position[1] += 3
            else:
                self.position[1] += pos[1] - self.center[1]

        if self.center[0] >= pos[0]:
            if self.center[0] - pos[0] >= 3:
                self.position[0] -= 3
            else:
                self.position[0] -= self.center[0] - pos[0]
        else:
            if pos[0] - self.center[0] >= 3:
                self.position[0] += 3
            else:
                self.position[0] += pos[0] - self.center[0]
        
        self.center = np.array([self.position[0] + 18, self.position[1] + 18])

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