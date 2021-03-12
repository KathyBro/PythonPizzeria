from tkinter import *
import tkinter.font as tkFont
import random as rng
import CalculationLib as mathy
import array as arr
import re

question_and_answer_area = ''
reset = False
homework_questions = []
day = 1
score = 0
minimum_q = 1
maximum_q = 10
submit_button = ''

def grade(parent_widget):
    global homework_questions
    global score
    global submit_button
    # submit_button["state"] = "disabled"
    children_widgets = parent_widget.winfo_children()
    question_num = 0
    if not score > 0:
        for child_widget in children_widgets:
            if child_widget.winfo_class() == 'Entry':
                try:
                    given_answer = float(child_widget.get())
                    actual_answer = homework_questions[question_num][1]

                    if given_answer == actual_answer:
                        score += 1
                    question_num += 1
                except:
                    pass


def add_calculation_text(button_type):
    global question_and_answer_area
    global reset
    switch = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "+",
        11: "-",
        12: "*",
        13: "/",
        14: "."
    }

    #Figure out what needs to be added
    add_on = switch.get(button_type, "Error")
    #Figure out what is already there
    text_so_far = question_and_answer_area.cget("text")
    if reset:
        text_so_far = ''
        reset = False
    
    #To allow 0's
    match = re.search('[^0]', text_so_far)
    not_index = match.start() if match else -1
    #Put it together
    text_so_far = text_so_far[not_index:]
    result_text = text_so_far + add_on
    #Formatted
    # text = f"{result_text:>16}"
    text = result_text.zfill(16)

    #Set it with a format
    question_and_answer_area.config(text=text)

def delete_from_question(args=''):
    global question_and_answer_area
    text_as_stands = question_and_answer_area.cget("text")

    text_as_stands = text_as_stands[0:len(text_as_stands)-1]
    question_and_answer_area.config(text="0"+text_as_stands)

def solve_question_in_calculator(args = ''):
    global question_and_answer_area
    global reset
    reset = True

    question = question_and_answer_area.cget("text")
    #Gets the numbers and type
    match = re.search("(\d+(.\d+)?)([+*\/-])(\d+(.\d+)?)", question)

    try:
        first_num = float(match.group(1))
        second_num = float(match.group(4))
    
        answer = 0

        if '+' in match.group(3): # A + - / or *
            answer = round(first_num + second_num, 3)
        elif '-' in match.group(3):
            answer = round(first_num - second_num, 3)
        elif '*' in match.group(3):
            answer = round(first_num * second_num, 3)
        elif '/' in match.group(3):
            if second_num != 0:
                answer = round(first_num / second_num, 3)
            else:
                answer = 'ERROR'
        else:
            answer = 'ERROR'
        
        text = str(answer).zfill(16)
        question_and_answer_area.config(text=text)
    except Exception:
        text = 'ERROR'.zfill(16)
        question_and_answer_area.config(text=text)


def create_calculator_canvas(frame):
    global question_and_answer_area
    calculator_font = tkFont.Font(family='', size=20)

    #Canvas
    calculator = Canvas(frame, bg='#b9c3ba')
    
    question_and_answer_area = Label(
        calculator, 
        height=1, 
        font=calculator_font, 
        bg="#30444d"
        )
    question_and_answer_area.grid(padx=10, pady=15, columnspan=5, row=0)

    #Button creation
    button_color = "#feffff"
    row_position = 3
    column_position = 0

    for i in range(1, 10):
        digit = Button(
            calculator, 
            bg=button_color, 
            relief=RAISED, 
            text=str(i), 
            command=lambda j=i: add_calculation_text(j)
            )
        digit.grid(padx=10, pady=10, column=column_position, row=row_position)

        column_position += 1
        if column_position == 3:
            row_position -= 1
            column_position = 0

    zero = Button(
            calculator, 
            bg=button_color, 
            relief=RAISED, 
            text=str(0), 
            command=lambda: add_calculation_text(0)
            )
    zero.grid(padx=10, pady=10, column=1, row=4)
    
    point = Button(
            calculator, 
            bg=button_color, 
            relief=RAISED, 
            text='.', 
            command=lambda: add_calculation_text(14)
            )
    point.grid(padx=10, pady=10, column=2, row=4)

    delete = Button(
            calculator, 
            bg=button_color, 
            relief=RAISED, 
            text='DEL', 
            command=lambda: delete_from_question()
            )
    delete.grid(padx=10, pady=10, column=0, row=4)

    add = Button(
            calculator, 
            bg=button_color, 
            relief=RAISED, 
            text='+', 
            command=lambda: add_calculation_text(10)
            )
    add.grid(padx=10, pady=10, column=4, row=1)

    subtract = Button(
            calculator, 
            bg=button_color, 
            relief=RAISED, 
            text='-', 
            command=lambda: add_calculation_text(11)
            )
    subtract.grid(padx=10, pady=10, column=4, row=2)

    multiply = Button(
            calculator, 
            bg=button_color, 
            relief=RAISED, 
            text='*', 
            command=lambda: add_calculation_text(12)
            )
    multiply.grid(padx=10, pady=10, column=4, row=3)

    divide = Button(
            calculator, 
            bg=button_color, 
            relief=RAISED, 
            text='/', 
            command=lambda: add_calculation_text(13)
            )
    divide.grid(padx=10, pady=10, column=4, row=4)

    equals = Button(
            calculator, 
            bg=button_color, 
            relief=RAISED, 
            text='=', 
            command=lambda: solve_question_in_calculator()
            )
    equals.grid(padx=10, pady=10, column=1, row=5)

    return calculator

def create_question(day):
    global minimum_q
    global maximum_q
    # Addition (1)
    # Subtraction
    # Multiplication
    # Division
    # Mix
    if day >= 5: # Mix encounter
        question_type = rng.randint(0,3)
    else:
        question_type = day - 1

    first = rng.randint(minimum_q, maximum_q)
    second = rng.randint(minimum_q, maximum_q)
    answer = 0
    question = str(first) + ' '
    if question_type == 0:
        #Addition
        question += '+ '
        answer = first + second
    elif question_type == 1:
        question += '- '
        answer = first - second
    elif question_type == 2:
        question += '* '
        answer = first * second
    elif question_type == 3:
        question += '/ '
        answer = round(first / second, 2)
    
    question += str(second)

    return [question, answer]

def create_homework_canvas(frame):
    global day
    global homework_questions
    global submit_button
    # Difficulty
    # 10 times
    # Label => (Num). 
    #Canvas
    homework = Canvas(frame, bg='white')

    for i in range(1, 11):
        question = create_question(day)
        homework_questions.append(question)

        label_question = Label(homework, anchor='w', bg='white', text=f"{i}. {question[0]}")
        label_question.grid(row=i, column=0)

        entry_answer = Entry(homework)
        entry_answer.grid(row = i, column=1)

    submit_assignment = Button(homework, text="Submit Assignment", command=lambda w=homework: grade(w))
    submit_assignment.grid(row=20, column=0, columnspan=4)
    submit_button = submit_assignment

    return homework

def create_frame(base_root):
    f = Frame(base_root)

    # Font
    calculator_font = tkFont.Font(family='', size=40)

    # Canvas for the Calculator
    calculator = create_calculator_canvas(f)

    # Canvas for the homework
    homework = create_homework_canvas(f)
    homework.pack(side='left', fill='both', expand=True)
    calculator.pack(side='right', fill='both', expand=True)

    for i in range(10):
        base_root.bind(str(i), lambda j=i: add_calculation_text(int(j.char)))
    base_root.bind("+", lambda event: add_calculation_text(10))
    base_root.bind("-", lambda event: add_calculation_text(11))
    base_root.bind("*", lambda event: add_calculation_text(12))
    base_root.bind("/", lambda event: add_calculation_text(13))
    base_root.bind('<Return>', solve_question_in_calculator)
    base_root.bind("<BackSpace>", delete_from_question)

    return f

def set_day(passed_in_day):
    global day
    global score
    global homework_questions
    homework_questions = []
    score = 0
    day = passed_in_day

def next_day():
    global day
    global score
    global homework_questions
    homework_questions = []
    score = 0
    day += 1

def get_day():
    global day
    return day

def get_grade():
    global score
    return score

if __name__ == "__main__":
    root = Tk()
    root.geometry("1100x800")
    back_room = create_frame(root)
    back_room.pack(fill='both', expand=True)

    root.mainloop()