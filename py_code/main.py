from PIL import Image, ImageDraw, ImageFont
import time
import random
import numpy as np
from colorsys import hsv_to_rgb

from Character import Character
from Dot1 import Dot1
from Dot2 import Dot2
from Flower import Flower
from Grass import Grass
from Joystick import Joystick

def main():
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height)) #도화지!
    my_draw = ImageDraw.Draw(my_image) 
    joystick.disp.image(my_image)

    # 잔상이 남지 않는 코드 & 대각선 이동 가능
    my_character = Character(joystick.width, joystick.height)

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

        my_character.move(command)


        #그리는 순서가 중요합니다. 배경을 먼저 깔고 위에 그림을 그리고 싶었는데 그림을 그려놓고 배경으로 덮는 결과로 될 수 있습니다.
        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (155, 219, 71))

        Dot1(10, 220).draw(my_draw)
        Dot1(11, 95).draw(my_draw)
        Dot1(12, 11).draw(my_draw)
        Dot1(19, 50).draw(my_draw)
        Dot1(41, 87).draw(my_draw)
        Dot1(48, 52).draw(my_draw)
        Dot1(49, 104).draw(my_draw)
        Dot1(56, 152).draw(my_draw)
        Dot1(60, 41).draw(my_draw)
        Dot1(67, 14).draw(my_draw)
        Dot1(70, 80).draw(my_draw)
        Dot1(93, 205).draw(my_draw)
        Dot1(96, 101).draw(my_draw)
        Dot1(159, 183).draw(my_draw)
        Dot1(163, 160).draw(my_draw)
        Dot1(171, 36).draw(my_draw)
        Dot1(180, 84).draw(my_draw)
        Dot1(184, 154).draw(my_draw)
        Dot1(218, 118).draw(my_draw)
        Dot1(223, 103).draw(my_draw)

        Dot2(1, 169).draw(my_draw)
        Dot2(6, 76).draw(my_draw)
        Dot2(29, 12).draw(my_draw)
        Dot2(35, 220).draw(my_draw)
        Dot2(60, 92).draw(my_draw)
        Dot2(61, 57).draw(my_draw)
        Dot2(62, 111).draw(my_draw)
        Dot2(97, 137).draw(my_draw)
        Dot2(120, 160).draw(my_draw)
        Dot2(140, 129).draw(my_draw)
        Dot2(149, 122).draw(my_draw)
        Dot2(150, 18).draw(my_draw)
        Dot2(171, 165).draw(my_draw)
        Dot2(181, 40).draw(my_draw)
        Dot2(184, 60).draw(my_draw)
        Dot2(185, 199).draw(my_draw)
        Dot2(195, 45).draw(my_draw)
        Dot2(200, 210).draw(my_draw)
        Dot2(201, 15).draw(my_draw)
        Dot2(227, 119).draw(my_draw)

        Flower(10, 100).draw(my_draw)
        Flower(30, 180).draw(my_draw)
        Flower(40, 40).draw(my_draw)
        Flower(40, 80).draw(my_draw)
        Flower(70, 110).draw(my_draw)
        Flower(150, 30).draw(my_draw)
        Flower(160, 190).draw(my_draw)
        Flower(180, 160).draw(my_draw)
        Flower(200, 70).draw(my_draw)
        Flower(210, 210).draw(my_draw)
        Flower(220, 140).draw(my_draw)
        Flower(220, 180).draw(my_draw)

        Grass(70, 30).draw(my_draw)
        Grass(110, 70).draw(my_draw)
        Grass(50, 180).draw(my_draw)
        Grass(100, 200).draw(my_draw)
        Grass(150, 120).draw(my_draw)
        Grass(25, 120).draw(my_draw)
        Grass(190, 10).draw(my_draw)

        
        my_character.draw(my_draw)
        #좌표는 동그라미의 왼쪽 위, 오른쪽 아래 점 (x1, y1, x2, y2)
        joystick.disp.image(my_image)
    

if __name__ == '__main__':
    main()