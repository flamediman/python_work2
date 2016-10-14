import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
message = "sfsdf"

frame = simplegui.create_frame("game", 300, 200)

def text_input(string):
    rpsls(string)

frame.add_input("Ваш ход ", text_input, 100)



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
    	print("сообщение об ошибке 1")


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
        return "сообщение об ошибке"


def rpsls(player_choice):
    print(' ')
    print(player_choice)
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(5)
    comp_choice = number_to_name(comp_number)
    print(comp_choice)
    result = (comp_number - player_number) % 5
    if result >= 3:
    	print('вы победили')
    elif result == 0:
    	print('ничья')
    else :
        print('вы проиграли')

def draw(canvas):
    canvas.draw_text(message, [0, 112], 50, "Yellow")
frame.set_draw_handler(draw)

frame.start()
