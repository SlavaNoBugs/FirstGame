from tkinter import *
window = Tk()
window.title("Начинаем Tkinter")
canvas = Canvas(window,width=1500,height=1000,bg="white",
          cursor="pencil")
canvas.create_rectangle(
    2, 2, 252, 402,
    outline="Black",
    fill="White")
canvas.create_rectangle(
    1250, 2, 1500, 402,
    outline="Black",
    fill="White")
canvas.create_line(0, 402, 1500, 402)
stat = Button(window, text="Статистика")
canvas_widget = canvas.create_window(290, 15, window=stat)
invent = Button(window, text="Инвентарь")
canvas_widget = canvas.create_window(360, 15, window=invent)

canvas.pack()
window.mainloop()