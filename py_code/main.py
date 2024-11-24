from PIL import Image, ImageDraw, ImageFont
import time
import random
import numpy as np
from colorsys import hsv_to_rgb

from Character import Character
from Background import Dot1
from Background import Dot2
from Background import Flower
from Background import Grass
from Etc import GameStart
from Etc import InfoCharacter
from Etc import Info
from Etc import GameEnd1
from Etc import GameEnd2
from Etc import EndingCharacter1
from Etc import EndingCharacter2
from Etc import GameScore
from Etc import GameScoreBoard
from Etc import Stone
from Exam import Exam
from FinalExam import FinalExam
from Item import GreatNote
from Item import PastExam
from Joystick import Joystick
from Game import Game
from GameArrow import GameArrow
from Portal import Portal
from Score import ScoreAPlus
from Score import ScoreA
from Score import ScoreBPlus
from Score import ScoreB
from Score import ScoreCPlus
from Score import ScoreC
from Term import Term1_1
from Term import Term1_2
from Term import Term2_1
from Term import Term2_2
from Term import Term3_1
from Term import Term3_2
from Term import Term4_1
from Term import Term4_2

def main():
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height)) 
    my_draw = ImageDraw.Draw(my_image)

    gameStart = GameStart()
    info = Info()
    info_character = InfoCharacter()
    my_character = Character(joystick.width, joystick.height)
    exam = Exam()
    finalExam = FinalExam()
    greateNote = GreatNote()
    pastExam = PastExam()
    portal = Portal()

    dots1 = [
        Dot1(10, 220), Dot1(11, 95), Dot1(12, 11), Dot1(19, 50),
        Dot1(41, 87), Dot1(48, 52), Dot1(49, 104), Dot1(56, 152),
        Dot1(60, 41), Dot1(67, 14), Dot1(70, 80), Dot1(93, 205),
        Dot1(96, 101), Dot1(159, 183), Dot1(163, 160), Dot1(171, 36),
        Dot1(180, 84), Dot1(184, 154), Dot1(218, 118), Dot1(223, 103)
        ]
    dots2 = [
        Dot2(1, 169), Dot2(6, 76), Dot2(29, 12), Dot2(35, 220),
        Dot2(60, 92), Dot2(61, 57), Dot2(62, 111), Dot2(97, 137),
        Dot2(120, 160), Dot2(140, 129), Dot2(149, 122), Dot2(150, 18),
        Dot2(171, 165), Dot2(181, 40), Dot2(184, 60), Dot2(185, 199),
        Dot2(195, 45), Dot2(200, 210), Dot2(201, 15), Dot2(227, 119)
        ]
    flowers = [
        Flower(10, 100), Flower(30, 180), Flower(40, 40), 
        Flower(110, 90), Flower(150, 30), Flower(160, 190), 
        Flower(200, 70), Flower(210, 210), Flower(220, 140)
        ]   
    grass = [
        Grass(25, 120), Grass(70, 30), Grass(100, 200), Grass(150, 120),Grass(190, 10)
        ]
    games = [
        Game(0, 0), Game(30, 0), Game(90, 0), Game(150, 0), Game(210, 0), 
        Game(240, 0), Game(240, 30), Game(240, 90), Game(240, 150), Game(240, 210),
        Game(240, 240), Game(210, 240), Game(150, 240), Game(90, 240), Game(30, 240), 
        Game(0, 240), Game(0, 210), Game(0, 150), Game(0, 90), Game(0, 30), 
        ]
    gameArrows = [
        GameArrow(), GameArrow(), GameArrow(), GameArrow(), GameArrow(), 
        GameArrow(), GameArrow(), GameArrow(), GameArrow(), GameArrow(), 
        GameArrow(), GameArrow(), GameArrow(), GameArrow(), GameArrow(), 
        GameArrow(), GameArrow(), GameArrow(), GameArrow(), GameArrow(),   
        GameArrow(), GameArrow(), GameArrow(), GameArrow(), GameArrow(),
        ]
    score = [
        ScoreAPlus(), ScoreA(), ScoreBPlus(), ScoreB(), ScoreCPlus(), ScoreC(), 
        ]
    terms = [
        Term1_1(), Term1_2(), Term2_1(), Term2_2(), Term3_1(), Term3_2(), Term4_1(), Term4_2(),
        ]

    while True:
        if not joystick.button_A.value: # A pressed
            break

        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (155, 219, 71))
        for d1 in dots1:
            d1.draw(my_draw)
        for d2 in dots2:
            d2.draw(my_draw)
        for f in flowers:
            f.draw(my_draw)
        for g in grass:
            g.draw(my_draw)

        gameStart.draw(my_draw)
        info_character.draw(my_draw)
        info.draw(my_draw)

        joystick.disp.image(my_image)

    arrows = []
    last_time1 = time.time()
    last_time2 = time.time()
    last_time3 = time.time()
    exam_time = time.time()
    item1_time = time.time()
    item1_active_time = None
    item2_time = time.time()
    item2_active_time = None
    portal_time = time.time()
    stage_flag = [False, False, False, False, False, False, False, False, False]
    i = 0
    clear = True
    color = (155, 219, 71)
    while True:
        command = {'move': False, 'up_pressed': False , 'down_pressed': False, 'left_pressed': False, 'right_pressed': False}
        
        if not joystick.button_U.value:  # up pressed
            command['up_pressed'] = True
            command['move'] = True

        if not joystick.button_D.value:  # down pressed
            command['down_pressed'] = True
            command['move'] = True

        if not joystick.button_L.value:  # left pressed
            command['left_pressed'] = True
            command['move'] = True

        if not joystick.button_R.value:  # right pressed
            command['right_pressed'] = True
            command['move'] = True

        if my_character.term % 2 == 0:
            color = (255, 250, 250)
        else:
            color = (155, 219, 71)

        
        
        # 다음 단계 진입 시
        if stage_flag[my_character.term - 1] == False:
            if stage_flag[7] == True:
                break
            my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = color)
            for d1 in dots1:
                d1.draw(my_draw)
            for d2 in dots2:
                d2.draw(my_draw)
            for f in flowers:
                f.draw(my_draw)
            for g in grass:
                g.draw(my_draw)

            terms[my_character.term - 1].setSize(100, 10, 3)
            terms[my_character.term - 1].draw(my_draw)

            joystick.disp.image(my_image)

            my_character.reset(joystick.width, joystick.height)
            last_time1 = time.time()
            last_time2 = time.time()
            last_time3 = time.time()
            exam_time = time.time()
            item1_time = time.time()
            item1_active_time = None
            item2_time = time.time()
            item2_active_time = None
            portal_time = time.time()
            exam.state = None
            finalExam.state = None
            greateNote.state = None
            pastExam.state = None
            portal.state = None
            for gameArrow in arrows:
                gameArrow.state = None
            arrows = []
            i = 0

            stage_flag[my_character.term - 1] = True


        if my_character.term >= 1:
            current_time = time.time()  # 현재 시간
            if current_time - last_time1 >= 1:  # 1초가 경과하면
                random_number = random.randint(0, 19)
                for j in range(1):  # 1번 반복
                    offset = 10 * j  # 각 화살의 offset
                    arrow = gameArrows[i]
                    start_position = games[(random_number + offset) % 20].position
                    gameArrows[i].run(start_position, my_character.center)
                    i = (i + 1) % 25
                    arrows.append(arrow)
                last_time1 = current_time

        if my_character.term >= 5:
            current_time = time.time()  # 현재 시간
            if current_time - last_time2 >= 2:  # 2초가 경과하면
                random_number = random.randint(0, 19)
                for j in range(3):  # 3번 반복
                    offset = 7 * j  # 각 화살의 offset
                    arrow = gameArrows[i]
                    start_position = games[(random_number + offset) % 20].position
                    gameArrows[i].run(start_position, my_character.center)
                    i = (i + 1) % 25
                    arrows.append(arrow)
                last_time2 = current_time

        if my_character.term >= 7:
            current_time = time.time()  # 현재 시간
            if current_time - last_time3 >= 5:  # 5초가 경과하면
                random_number = random.randint(0, 19)
                for j in range(3):  # 4번 반복
                    offset = 8 * j  # 각 화살의 offset
                    arrow = gameArrows[i]
                    start_position = games[(random_number + offset) % 20].position
                    gameArrows[i].run(start_position, my_character.center)
                    i = (i + 1) % 25
                    arrows.append(arrow)
                last_time3 = current_time

        if my_character.term >= 3:
            current_time = time.time()  # 현재 시간
            if current_time - exam_time >= 15 and exam.state != 'alive':  # 30초가 경과하면
                random_number = random.randint(0, 3)
                if random_number == 0:
                    exam.run(0, 0, 3)
                elif random_number == 1:
                    exam.run(0, 224, 3)
                elif random_number == 2:
                    exam.run(224, 0, 3)
                else:
                    exam.run(224, 224, 3)
                
                exam_time = current_time

        if my_character.term == 8:
            if finalExam.state != 'alive':
                finalExam.run(224, 224, 4)

        if my_character.term >= 1:
            current_time = time.time()  # 현재 시간
            if current_time - item1_time >= 15: # 30초가 경과하면
                if greateNote.state == 'alive' or greateNote.state == 'use':
                    item1_time = current_time
                else:
                    random_number1 = random.randint(0, 214)
                    random_number2 = random.randint(40, 214)
                    greateNote.run(random_number1, random_number2)
                
                    item1_time = current_time

        if my_character.term >= 3:
            current_time = time.time()  # 현재 시간
            if current_time - item2_time >= 25: # 30초가 경과하면
                if pastExam.state == 'alive' or pastExam.state == 'use':
                    item2_time = current_time
                else:
                    random_number1 = random.randint(80, 214)
                    random_number2 = random.randint(0, 214)
                    pastExam.run(random_number1, random_number2)
                
                    item2_time = current_time

        

        current_time = time.time()  # 현재 시간
        if current_time - portal_time >= 30 and portal.state != 'alive':  # 30초가 경과하면
            random_number = random.randint(0, 3)
            if random_number == 0:
                portal.run(20, 60)
            elif random_number == 1:
                portal.run(20, 220)
            elif random_number == 2:
                portal.run(220, 20)
            else:
                portal.run(220, 220)
            
            
            portal_time = current_time

        



        my_character.move(command)

        if exam.state == 'alive':
            exam.move(my_character.center)
            exam.collision_check(my_character)
            if exam.state == 'die' and pastExam.state == 'use':
                pastExam.state = 'die'

        if finalExam.state == 'alive':
            finalExam.move(my_character.center)
            finalExam.collision_check(my_character)
            if finalExam.state == 'die' and pastExam.state == 'use':
                pastExam.state = 'die'

        for gameArrow in arrows:
            if gameArrow.state == 'alive':
                gameArrow.move()
                gameArrow.collision_check(my_character)
                if gameArrow.state == 'die' and pastExam.state == 'use':
                    pastExam.state = 'die'

        arrows = [gameArrow for gameArrow in arrows if 0 <= gameArrow.position[0] <= 240 and 0 <= gameArrow.position[1] <= 240 and gameArrow.state == 'alive']


        if greateNote.state == 'alive':
            greateNote.collision_check(my_character)
            if greateNote.state == 'use':
                item1_active_time = time.time()

        current_time = time.time()
        if greateNote.state == 'use':
            if current_time - item1_active_time >= 5:
                greateNote.state = 'die'
            else:
                for gameArrow in arrows:
                    gameArrow.item1 = True

        if greateNote.state == 'die':
            for gameArrow in arrows:
                gameArrow.item1 = False
            item1_active_time = None
            greateNote.state = None
            

        if pastExam.state == 'alive':
            pastExam.collision_check(my_character)
            if pastExam.state == 'use':
                item2_active_time = time.time()

        current_time = time.time()
        if pastExam.state == 'use':
            if current_time - item2_active_time >= 5:
                pastExam.state = 'die'
            else:
                exam.item2 = True

        if pastExam.state == 'die':
            exam.item2 = False
            item2_active_time = None
            pastExam.state = None
            

        if portal.state == 'alive':
            portal.collision_check(my_character)

        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = color)
        for d1 in dots1:
            d1.draw(my_draw)
        for d2 in dots2:
            d2.draw(my_draw)
        for f in flowers:
            f.draw(my_draw)
        for g in grass:
            g.draw(my_draw)

        if portal.state != 'die':
            terms[my_character.term - 1].draw(my_draw)

        if my_character.grade < 6:
            if greateNote.state == 'use':
                my_draw.ellipse((my_character.center[0] - 16, my_character.center[1] - 16, my_character.center[0] + 16, my_character.center[1] + 16), outline = (255, 242, 0), width = 2)
            if pastExam.state == 'use':
                my_draw.ellipse((my_character.center[0] - 16, my_character.center[1] - 16, my_character.center[0] + 16, my_character.center[1] + 16), outline = (255, 0, 0), width = 2)
            my_character.draw(my_draw)
        else:
            clear = False

        if greateNote.state == 'alive':
            greateNote.draw(my_draw)
        
        if pastExam.state == 'alive':
            pastExam.draw(my_draw)

        if portal.state == 'alive':
            my_draw.ellipse((portal.position[0] - 18, portal.position[1] - 18, portal.position[0] + 18, portal.position[1] + 18), outline = (35, 73, 165), width = 3)
            my_draw.ellipse((portal.position[0] - 16, portal.position[1] - 16, portal.position[0] + 16, portal.position[1] + 16), outline = (255, 255, 255), width = 2)
            my_draw.ellipse((portal.position[0] - 14, portal.position[1] - 14, portal.position[0] + 14, portal.position[1] + 14), outline = (23, 221, 233), width = 3)
            my_draw.ellipse((portal.position[0] - 11, portal.position[1] - 11, portal.position[0] + 11, portal.position[1] + 11), fill = (0, 0, 0))

        if exam.state == 'alive':
            exam.draw(my_draw)

        if finalExam.state == 'alive':
            finalExam.draw(my_draw)

        for gameArrow in arrows:
            my_draw.ellipse((gameArrow.position[0] - 4, gameArrow.position[1] - 4, gameArrow.position[0] + 4, gameArrow.position[1] + 4), fill = (255, 0, 0))
            # my_draw.ellipse((gameArrow.position[0] - 1, gameArrow.position[1] - 1, gameArrow.position[0] + 1, gameArrow.position[1] + 1), fill = (255, 255, 255))

        if my_character.grade < 6:    
            score[my_character.grade].draw(my_draw)

        joystick.disp.image(my_image)

        while clear == False:
            gameEnd2 = GameEnd2()
            ec2 = EndingCharacter2()

            my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = color)
            for d1 in dots1:
                d1.draw(my_draw)
            for d2 in dots2:
                d2.draw(my_draw)
            for f in flowers:
                f.draw(my_draw)
            for g in grass:
                g.draw(my_draw)

            ec2.move(80, 140, 2)
            ec2.draw(my_draw)
            gameEnd2.draw(my_draw)

            joystick.disp.image(my_image)

            if not joystick.button_A.value:
                my_character.retry(joystick.width, joystick.height)
                last_time1 = time.time()
                last_time2 = time.time()
                last_time3 = time.time()
                exam_time = time.time()
                item1_time = time.time()
                item1_active_time = None
                item2_time = time.time()
                item2_active_time = None
                portal_time = time.time()
                exam.state = None
                finalExam.state = None
                greateNote.state = None
                pastExam.state = None
                portal.state = None
                for gameArrow in arrows:
                    gameArrow.state = None
                arrows = []
                stage_flag = [False, False, False, False, False, False, False, False, False]
                i = 0
                clear = True

    if clear:
        stone = Stone()
        gameEnd1 = GameEnd1()
        ec1 = EndingCharacter1()
        gameScore = GameScore()
        gameScoreBoard = GameScoreBoard()

        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 250, 250))
        for d1 in dots1:
            d1.draw(my_draw)
        for d2 in dots2:
            d2.draw(my_draw)
        for f in flowers:
            f.draw(my_draw)
        for g in grass:
            g.draw(my_draw)

        ec1.move(5, 140, 2)
        ec1.draw(my_draw)
        stone.draw(my_draw)

        joystick.disp.image(my_image)

        time.sleep(1)

        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 250, 250))
        for d1 in dots1:
            d1.draw(my_draw)
        for d2 in dots2:
            d2.draw(my_draw)
        for f in flowers:
            f.draw(my_draw)
        for g in grass:
            g.draw(my_draw)

        ec1.move(80, 120, 2)
        ec1.draw(my_draw)
        stone.draw(my_draw)

        joystick.disp.image(my_image)

        time.sleep(1)

        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 250, 250))
        for d1 in dots1:
            d1.draw(my_draw)
        for d2 in dots2:
            d2.draw(my_draw)
        for f in flowers:
            f.draw(my_draw)
        for g in grass:
            g.draw(my_draw)

        ec1.move(100, 80, 1)
        ec1.draw(my_draw)
        stone.draw(my_draw)

        joystick.disp.image(my_image)

        time.sleep(1)

        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 250, 250))
        for d1 in dots1:
            d1.draw(my_draw)
        for d2 in dots2:
            d2.draw(my_draw)
        for f in flowers:
            f.draw(my_draw)
        for g in grass:
            g.draw(my_draw)

        stone.draw(my_draw)

        joystick.disp.image(my_image)

        time.sleep(1)

        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 250, 250))
        for d1 in dots1:
            d1.draw(my_draw)
        for d2 in dots2:
            d2.draw(my_draw)
        for f in flowers:
            f.draw(my_draw)
        for g in grass:
            g.draw(my_draw)

        ec1.move(80, 15, 2)
        ec1.draw(my_draw)
        gameEnd1.draw(my_draw)


        # my_draw.ellipse((75, 119, 175, 219), fill = (102, 204, 255))
        # my_draw.ellipse((70, 114, 170, 214), fill = (179, 230, 255))
        gameScoreBoard.draw(my_draw)
        gameScore.draw(my_character.grade, my_draw)

        joystick.disp.image(my_image)

    
    

if __name__ == '__main__':
    main()