import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

frame = simplegui.create_frame("game", 300, 200)
color = 'write'

def text_input(string):
    global color
    color = string
    frame.set_canvas_background(color)

def draw(canvas):
    canvas.draw_text(color, [0, 112], 50, "Red")

frame.add_input("Введите цвет", text_input, 100)
frame.set_draw_handler(draw)


frame.start()
