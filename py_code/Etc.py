import numpy as np

class GameStart:
    def __init__(self):
        self.position = np.array([3, 20])
        self.pixel_map = [
            "........................................",
            "...aaaaaabcccccccccccccccccccccccd......",
            "..caaaaaabcccccccccccccccccccccccdd.....",
            ".ccceeeeeebfffffffffffffeeeeeeeeebddd...",
            "ccceeeeeeeebfffffffffffeeeeeeeeeeebddd..",
            "aceeeebbbeeeebbbbbfffbbbbbeeeeebeeebdg..",
            "aaeeebeeebeeebfffffffeeeebeeeebebeebgg..",
            ".aaeebeeebeeebefffffeeeeebeeeebebeebgg..",
            ".aaeeebbbeeefbbbbbfefeeeebeeebeeebffbgg.",
            ".aaeeeeeeefffffffeffffeeebeeebeefbffbgg.",
            "..aabbbbbbbfbbbbbbbffffbeeeeeeffffffbgg.",
            "..aaceefffffffebfffffffbeeeebbbbbbbfbgg.",
            "..ccfbfffffhhbhbhhhhfffbfeeffffbffffbgg.",
            ".ccffbfffhhhhbhhhhhhhhhbhhhffffbffffbgg.",
            "ccfffbbbbbiiibbbbbhhbbbbbbbffffbffffbgg.",
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


class InfoCharacter:
    def __init__(self):
        self.position = np.array([5, 140])
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
            "ddssbbbsspppsssssddssssspppssbbbsssd",
            "ddssbbbsspppsssssddssssspppssbbbsssd",
            "ddssbbbbbsssssddddddddsssssbbbbbsssd",
            "ddssbbbbbsssssddddddddsssssbbbbbsssd",
            "ddssbbddbbbssssssssssssssbbbbbbbsssd",
            "ddssbbddbbbssssssssssssssbbbbddbsssd",
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

    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "d":
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (0, 0, 0))
                if pixel == "b":
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (219, 188, 130))
                if pixel == "s":
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (254, 224, 172))
                if pixel == "g":
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (34, 177, 76))
                if pixel == "p":
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (255, 174, 201))


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


class GameEnd2:
    def __init__(self):
        self.position = np.array([3, 20])
        self.pixel_map = [
            "........................................",
            "...aaaaaabcccccccccccccccccccccccd......",
            "..caaaaaabcccccccccccccccccccccccdd.....",
            ".ccceeeeeebfffffffffffffeeeeeeeeebddd...",
            "ccceeeeeeeebfffffffffffeeeeeeeeeeebddd..",
            "aceebbbbeebbbbbfbbbbbfbbbbeebeeebeebdg..",
            "aaeebeeebebeeeffffbffebeeebebeeebeebgg..",
            ".aaebeeebebeeeefffbfeebeeebebeeebeebgg..",
            ".aaebeeebebeffffffbefebeeebebeeebeffbgg.",
            ".aaebbbbeebbbbbffebfffbbbbeeebbbffffbgg.",
            "..aabbeeffbffffeffbfffbbeeeeeebfffffbgg.",
            "..aabebfffbfffefffbfffbfbeeeefbfffffbgg.",
            "..ccbffbffbhhhhhhhbhffbffbefffbfffffbgg.",
            ".ccfbfffbhbhhhhhhhbhhhbhhhbfffbfffffbgg.",
            "ccffbffibibbbbbiihbhhhbhhhbfffbfffffbgg.",
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


class EndingCharacter1:
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
            ".ddbbbbbdddddddddddddddddddddbbbdd..",
            ".ddbbbbssddddddddssddddddddssbbbdd..",
            ".dddbbbsssddddddssssddddddsssbbbbdd.",
            "ddssbbbsspppsssssddssssspppssbbbsssd",
            "ddssbbbsspppsssssddssssspppssbbbsssd",
            "ddssbbbbbsssssddddddddsssssbbbbbsssd",
            "ddssbbbbbsssssddddddddsssssbbbbbsssd",
            "ddssbbddbbbssssssssssssssbbbbbbbsssd",
            "ddssbbddbbbssssssssssssssbbbbddbsssd",
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


class Stone:
    def __init__(self):
        self.position = np.array([3, 20])
        self.pixel_map = [
            "........................................",
            "...aaaaaabcccccccccccccccccccccccd......",
            "..caaaaaabcccccccccccccccccccccccdd.....",
            ".ccceeeeeebfffffffffffffeeeeeeeeebddd...",
            "ccceeeeeeeebfffffffffffeeeeeeeeeeebddd..",
            "aceeeeeeeeeeefffffffffeeeeeeeeeeeeebdg..",
            "aaeeeeeeeeeeeefffffffeeeeeeeeeeeeeebgg..",
            ".aaeeeeeeeeeeeefffffeeeeeeeeeeeeeeebgg..",
            ".aaeeeeeeeeefffffffefeeeeeeeeeeeeeffbgg.",
            ".aaeeeeeeefffffffeffffeeeeeeeeeeffffbgg.",
            "..aaeeeefffffffefffffffeeeeeeeffffffbgg.",
            "..aaceefffffffefffffffffeeeeefffffffbgg.",
            "..ccfffffffhhhhhhhhhfffffeefffffffffbgg.",
            ".ccffffffhhhhhhhhhhhhhhhhhhfffffffffbgg.",
            "ccfffffiiiiiiiiiihhhhhhhhhhfffffffffbgg.",
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