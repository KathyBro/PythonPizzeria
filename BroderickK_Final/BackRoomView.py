from tkinter import *
import tkinter.font as tkFont
import random as rng
import CalculationLib


def create_frame(base_root):
    f = Frame(base_root)

    # Font
    calculator_font = tkFont.Font(family='', size=40)

    # Canvas for the Calculator
    calculator = Canvas(f, bg='#b9c3ba')
    space_label = Label(calculator, bg='#b9c3ba')
    space_label.pack(side='top')
    question_and_answer_area = Label(calculator, height=1, font=calculator_font, bg="#30444d", text='   1+2')
    question_and_answer_area.pack(side='top')

    # Canvas for the homework
    homework = Canvas(f, bg='white')
    homework.pack(side='left', fill='both', expand=True)
    calculator.pack(side='right', fill='both', expand=True)

    return f


if __name__ == "__main__":
    root = Tk()
    root.geometry("1100x800")
    back_room = create_frame(root)
    back_room.pack(fill='both', expand=True)

    root.mainloop()