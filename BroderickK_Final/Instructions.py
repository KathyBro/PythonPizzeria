from tkinter import *
import tkinter.font as tkFont

def instructions_window():
    root = Tk()
    root.title("Instructions")
    root.geometry("400x300")

    inst_frame = Frame(root)
    title_font = tkFont.Font(family="Arial 16 Bold", size=25)
    title = Label(inst_frame, text="INSTRUCTIONS", font=title_font)
    body = Message(inst_frame, text="LOBBY-Use arrow keys or WASD to move. Hit space to take orders which are represented by the exclamation points. These will go to the PizzaOrdersAPI.\n\nKITCHEN-Create the pizza that is on the top. The pizza will be sent automatically to the guest.\n\nBACKROOM-And don't FORGET TO DO YOUR HOMEWORK!!!Your math final is in 5 days. Submit your assignment before you end the day.")
    title.pack()
    body.pack()
    inst_frame.pack()

    root.mainloop()

if __name__ == '__main__':
    instructions_window()