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
            "aceeeekkkeeeekkkkkfffkkkkkeeeeekeeebdg..",
            "aaeeekeeekeeekfffffffeeeekeeeekekeebgg..",
            ".aaeekeeekeeekefffffeeeeekeeeekekeebgg..",
            ".aaeeekkkeeefkkkkkfefeeeekeeekeeekffbgg.",
            ".aaeeeeeeefffffffeffffeeekeeekeefkffbgg.",
            "..aakkkkkkkfkkkkkkkffffkeeeeeeffffffbgg.",
            "..aaceefffffffekfffffffkeeeekkkkkkkfbgg.",
            "..ccfkfffffhhkhkhhhhfffkfeeffffkffffbgg.",
            ".ccffkfffhhhhkhhhhhhhhhkhhhffffkffffbgg.",
            "ccfffkkkkkiiikkkkkhhkkkkkkkffffkffffbgg.",
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
                if pixel == "k":
                    x0 = x_start + x * 6
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 6, y0 + 4], fill = (230, 230, 230))


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
            "aceeekkkeekeefffkkkkkfekkkeekkkkeeebdg..",
            "aaeekeeekekeeeffkffffekeeekekeeekeebgg..",
            ".aaekeeekekeeeefkfffeekeeekekeeekeebgg..",
            ".aaekeeekekeffffkffefekeeekekeeekeffbgg.",
            ".aaekeeeeekfffffkkkkkfkkkkkekkkkkfffbgg.",
            "..aakeeeffkffffekfffffkeeekekkeeffffbgg.",
            "..aakeefkfkfffefkfffffkfeekekfkfffffbgg.",
            "..cckfffkfkhhhhhkhhhffkffekfkffkffffbgg.",
            ".ccfkfffkhkhhhhhkhhhhhkhhhkfkfffkfffbgg.",
            "ccfffkkkiikkkkkikkkkkhkhhhkfkfffkfffbgg.",
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
                if pixel == "k":
                    x0 = x_start + x * 6
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 6, y0 + 4], fill = (230, 230, 230))


class GameEnd2:
    def __init__(self):
        self.position = np.array([3, 20])
        self.pixel_map = [
            "........................................",
            "...aaaaaabcccccccccccccccccccccccd......",
            "..caaaaaabcccccccccccccccccccccccdd.....",
            ".ccceeeeeebfffffffffffffeeeeeeeeebddd...",
            "ccceeeeeeeebfffffffffffeeeeeeeeeeebddd..",
            "aceekkkkeekkkkkfkkkkkfkkkkeekeeekeebdg..",
            "aaeekeeekekeeeffffkffekeeekekeeekeebgg..",
            ".aaekeeekekeeeefffkfeekeeekekeeekeebgg..",
            ".aaekeeekekeffffffkefekeeekekeeekeffbgg.",
            ".aaekkkkeekkkkkffekfffkkkkeeekkkffffbgg.",
            "..aakkeeffkffffeffkfffkkeeeeeekfffffbgg.",
            "..aakekfffkfffefffkfffkfkeeeefkfffffbgg.",
            "..cckffkffkhhhhhhhkhffkffkefffkfffffbgg.",
            ".ccfkfffkhkhhhhhhhkhhhkhhhkfffkfffffbgg.",
            "ccffkffikikkkkkiihkhhhkhhhkfffkfffffbgg.",
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
                if pixel == "k":
                    x0 = x_start + x * 6
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 6, y0 + 4], fill = (230, 230, 230))


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


class GameScore:
    def __init__(self):
        self.pixel_map1 = [
            ".....kk.......kk..",
            ".....kk.......kk..",
            "....kkkk....kkkkkk",
            "....kkkk....kkkkkk",
            "...kk..kk.....kk..",
            "...kk..kk.....kk..",
            "..kk....kk........",
            "..kkkkkkkk........",
            ".kkkkkkkkkk.......",
            ".kk......kk.......",
            "kk........kk......",
            "kk........kk......",
        ]
        self.pixel_map2 = [
            ".....kk.....",
            ".....kk.....",
            "....kkkk....",
            "....kkkk....",
            "...kk..kk...",
            "...kk..kk...",
            "..kk....kk..",
            "..kkkkkkkk..",
            ".kkkkkkkkkk.",
            ".kk......kk.",
            "kk........kk",
            "kk........kk",
        ]
        self.pixel_map3 = [
            "..kkkkkk......kk..",
            "..kkkkkkk.....kk..",
            "..kk....kk..kkkkkk",
            "..kk....kk..kkkkkk",
            "..kk....kk....kk..",
            "..kkkkkkk.....kk..",
            "..kkkkkkk.........",
            "..kk....kk........",
            "..kk....kk........",
            "..kk....kk........",
            "..kkkkkkk.........",
            "..kkkkkk..........",
        ]
        self.pixel_map4 = [
            "..kkkkkk....",
            "..kkkkkkk...",
            "..kk....kk..",
            "..kk....kk..",
            "..kk....kk..",
            "..kkkkkkk...",
            "..kkkkkkk...",
            "..kk....kk..",
            "..kk....kk..",
            "..kk....kk..",
            "..kkkkkkk...",
            "..kkkkkk....",
        ]
        self.pixel_map5 = [
            "....kkkk......kk..",
            "..kkkkkkkk....kk..",
            ".kkk....kkk.kkkkkk",
            ".kk......kk.kkkkkk",
            "kk............kk..",
            "kk............kk..",
            "kk................",
            "kk................",
            ".kk......kk.......",
            ".kkk....kkk.......",
            "..kkkkkkkk........",
            "....kkkk..........",
        ]
        self.pixel_map6 = [
            "....kkkk....",
            "..kkkkkkkk..",
            ".kkk....kkk.",
            ".kk......kk.",
            "kk..........",
            "kk..........",
            "kk..........",
            "kk..........",
            ".kk......kk.",
            ".kkk....kkk.",
            "..kkkkkkkk..",
            "....kkkk....",
        ]

    
    def draw(self, grade, draw_tool):
        if grade % 2 == 0:
            x_start = 84
            y_start = 160
        else:
            x_start = 96
            y_start = 160

        if grade == 0:
            pixel_map = self.pixel_map1
        if grade == 1:
            pixel_map = self.pixel_map2
        if grade == 2:
            pixel_map = self.pixel_map3
        if grade == 3:
            pixel_map = self.pixel_map4
        if grade == 4:
            pixel_map = self.pixel_map5
        if grade == 5:
            pixel_map = self.pixel_map6
    
        for y, row in enumerate(pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "k":
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 0, 0))

class GameScoreBoard:
    def __init__(self):
        self.position = np.array([55, 105])
        self.pixel_map = [
            ".bbbbbbbb....",
            "bwwwwwwbwb...",
            "bwwwwwwbwwb..",
            "bwwwwwwbwwwb.",
            "bwwwwwwbbbbbb",
            "bwwwwwwwwwwwb",
            "bwwwwwwwwwwwb",
            "bwwwwwwwwwwwb",
            "bwwwwwwwwwwwb",
            "bwwwwwwwwwwwb",
            "bwwwwwwwwwwwb",
            "bwwwwwwwwwwwb",
            ".bbbbbbbbbbb.",
            ]

    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "b":
                    x0 = x_start + x * 10
                    y0 = y_start + y * 10
                    draw_tool.rectangle([x0, y0, x0 + 10, y0 + 10], fill = (50, 50, 50))
                if pixel == "w":
                    x0 = x_start + x * 10
                    y0 = y_start + y * 10
                    draw_tool.rectangle([x0, y0, x0 + 10, y0 + 10], fill = (255, 255, 255))
    


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