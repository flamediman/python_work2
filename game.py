import random
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
player_choice2 = ''
comp_choice = ''
result1 = ''
frame = simplegui.create_frame('home', 400, 300, 100)

def text_input(string):
    rpsls(string)

frame.add_input('ваш ход', text_input, 100)


def draw(canvas):
    canvas.draw_text(player_choice2, [75, 50], 40, "Red")
    canvas.draw_text(comp_choice, [75, 100], 40, "Red")
    canvas.draw_text(result1, [75, 150], 40, "Red")



def name_to_number(name):
    if name == "камень":
        return 0
    elif name == "спок":
        return 1
    elif name == "бумага":
        return 2
    elif name == "ящерица":
        return 3
    elif name == "ножницы":
        return 4
    else:
        return "ошибка"


def number_to_name(number):
    if number == 0:
        return "камень"
    elif number == 1:
        return "спок"
    elif number == 2:
        return "бумага"
    elif number == 3:
        return "ящерица"
    elif number == 4:
        return "ножницы"
    else:
        return "ошибка"


def win_lose(result):
    if result == 1:
        return 'вы победили '
    elif result == 0:
        return 'ничья'
    else:
        return 'вы проиграли'

def rpsls(player_choice):
    global result1
    global comp_choice
    global player_choice2
    player_choice2 = player_choice
    print(player_choice)
    player_number = name_to_number(player_choice)
    if player_number == "ошибка":
        player_choice2 = 'неверно введено'
    else:
        comp_number = random.randrange(5)
        comp_choice = number_to_name(comp_number)
        print(comp_choice)
        x = (comp_number - player_number) % 5
        if x >= 3:
            result = 1
        elif x == 0:
            result = 0
        else:
            result = -1
        result1 = win_lose(result)

frame.set_draw_handler(draw)
frame.start()
