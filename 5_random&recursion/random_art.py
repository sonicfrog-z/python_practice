import tkinter
import random

width = 500
height = 500
window = tkinter.Tk()
window.title('Random Art')
canvas = tkinter.Canvas(window, width=width, height=height)
canvas.pack()


def draw_rectangle(canvas):
    top = random.randint(10, height-50)
    left = random.randint(10, width-50)
    bottom = random.randint(top+30, height-10)
    right = random.randint(left+30, width-10)
    color = random.choice(['red', 'blue', 'pink', 'yellow', 'green', "purple"])
    canvas.create_rectangle(left, top, right, bottom, outline=color)


for _ in range(1000):
    draw_rectangle(canvas)

window.mainloop()
