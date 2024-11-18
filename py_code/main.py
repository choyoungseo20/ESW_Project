from PIL import Image, ImageDraw, ImageFont
import time
import random
import numpy as np
from colorsys import hsv_to_rgb

from Assignment import Assignment
from AssignmentArrow import AssignmentArrow
from Character import Character
from Dot1 import Dot1
from Dot2 import Dot2
from Flower import Flower
from GameStart import GameStart
from Grass import Grass
from Info import Info
from InfoCharacter import InfoCharacter
from Joystick import Joystick
from ScoreAPlus import ScoreAPlus
from ScoreA import ScoreA
from ScoreBPlus import ScoreBPlus
from ScoreB import ScoreB
from ScoreCPlus import ScoreCPlus
from ScoreC import ScoreC
from Test import Test

def main():
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height)) 
    my_draw = ImageDraw.Draw(my_image)

    gameStart = GameStart()
    info = Info()
    info_character = InfoCharacter()
    my_character = Character(joystick.width, joystick.height)
    test = Test()  

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
        Flower(10, 100), Flower(30, 180), Flower(40, 40), Flower(40, 80),
        Flower(70, 110), Flower(150, 30), Flower(160, 190), Flower(180, 160),
        Flower(200, 70), Flower(210, 210), Flower(220, 140), Flower(220, 180)
    ]   
    grass = [
        Grass(70, 30), Grass(110, 70), Grass(50, 180), Grass(100, 200),
        Grass(150, 120), Grass(25, 120), Grass(190, 10)
    ]
    assignments = [
        Assignment(0, 0), Assignment(30, 0), Assignment(90, 0), Assignment(150, 0), Assignment(210, 0), 
        Assignment(240, 0), Assignment(240, 30), Assignment(240, 90), Assignment(240, 150), Assignment(240, 210),
        Assignment(240, 240), Assignment(210, 240), Assignment(150, 240), Assignment(90, 240), Assignment(30, 240), 
        Assignment(0, 240), Assignment(0, 210), Assignment(0, 150), Assignment(0, 90), Assignment(0, 30), 
    ]
    assignmentArrows = [
        AssignmentArrow(), AssignmentArrow(), AssignmentArrow(), AssignmentArrow(), AssignmentArrow(), 
        AssignmentArrow(), AssignmentArrow(), AssignmentArrow(), AssignmentArrow(), AssignmentArrow(), 
        AssignmentArrow(), AssignmentArrow(), AssignmentArrow(), AssignmentArrow(), AssignmentArrow(), 
        AssignmentArrow(), AssignmentArrow(), AssignmentArrow(), AssignmentArrow(), AssignmentArrow(),   
        AssignmentArrow(), AssignmentArrow(), AssignmentArrow(), AssignmentArrow(), AssignmentArrow(),
    ]
    score = [
        ScoreAPlus(), ScoreA(), ScoreBPlus(), ScoreB(), ScoreCPlus(), ScoreC(), 
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
    last_time = time.time()
    i = 0
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


        current_time = time.time()  # 현재 시간
        if current_time - last_time >= 1:  # 1초가 경과하면
            random_number = random.randint(0, 19)
            for j in range(1):  # n번 반복
                offset = 10 * j  # 각 화살의 offset
                arrow = assignmentArrows[i]
                start_position = assignments[(random_number + offset) % 20].position
                assignmentArrows[i].run(start_position, my_character.center)
                i = (i + 1) % 25
                arrows.append(arrow)
            last_time = current_time
            

        my_character.move(command)

        if test.state == 'alive':
            test.move(my_character.center)
            test.collision_check(my_character)

        for assignmentArrow in arrows:
            if assignmentArrow.state == 'alive':
                assignmentArrow.move()
                assignmentArrow.collision_check(my_character)

        arrows = [assignmentArrow for assignmentArrow in arrows if 0 <= assignmentArrow.position[0] <= 240 and 0 <= assignmentArrow.position[1] <= 240 and assignmentArrow.state == 'alive']


        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (155, 219, 71))
        for d1 in dots1:
            d1.draw(my_draw)
        for d2 in dots2:
            d2.draw(my_draw)
        for f in flowers:
            f.draw(my_draw)
        for g in grass:
            g.draw(my_draw)


        if my_character.grade < 6:    
            my_character.draw(my_draw)
        else:
            break
        if test.state == 'alive':
            test.draw(my_draw)
        for assignmentArrow in arrows:
            my_draw.ellipse((assignmentArrow.position[0] - 3, assignmentArrow.position[1] - 3, assignmentArrow.position[0] + 3, assignmentArrow.position[1] + 3), fill = (255, 0, 0))
            my_draw.ellipse((assignmentArrow.position[0] - 1, assignmentArrow.position[1] - 1, assignmentArrow.position[0] + 1, assignmentArrow.position[1] + 1), fill = (255, 255, 255))

        if my_character.grade < 6:    
            score[my_character.grade].draw(my_draw)

        joystick.disp.image(my_image)
    

if __name__ == '__main__':
    main()