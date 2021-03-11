from tkinter import *
import tkinter.font as tkFont
import BackRoomView
import KitchenView
import LobbyView
from Player import player
import json
from os import system
import os.path

my_player = ''
file_name = "PythonPizzera.txt"
back_room_frame = ''
root = ''

def save_game():
    global my_player
    global file_name
    global back_room_frame
    global root

    calculate_percentage_score()
    if back_room_frame != '':
        back_room_frame.grid_forget()
        back_room_frame = BackRoomView.create_frame(root)
        back_room_frame.grid(row=1, column=0, sticky='news', columnspan=4)
        root.update()

    with open(file_name, 'w') as file:
        name = my_player.name
        grade = my_player.math_grade
        current_day = my_player.current_day
        player_info = [{"name":name, "math_grade":grade, "day":current_day}]
        file.write(json.dumps(player_info, indent=4))

def raise_frame(frame):
    KitchenView.get_newest_order()
    frame.tkraise()

def find_player():
    global my_player
    global file_name
    if os.path.exists(file_name):
        my_player = player()
        with open(file_name, 'r') as file:
            player_info = json.loads(file.read())
            my_player.name = player_info[0]['name']
            my_player.math_grade = player_info[0]['math_grade']
            my_player.current_day = player_info[0]['day']
    else:
        if my_player == '':
            my_player = player()
        save_game()


def calculate_percentage_score():
    global my_player
    new_score = BackRoomView.get_grade()
    current_grade = my_player.math_grade

    # Need to figure out what it is and then divide again
    current_grade = current_grade * my_player.current_day

    current_grade += new_score
    current_grade /= my_player.current_day * 10

    BackRoomView.next_day()
    my_player.current_day += 1

if __name__ == '__main__':
    find_player()
    root = Tk()
    root.title('Python Pizzeria')
    root.geometry("1100x800")
    back_room_frame = BackRoomView.create_frame(root)
    kitchen_frame = KitchenView.create_frame(root)
    lobby_frame = LobbyView.create_frame(root)

    for frame in (back_room_frame, kitchen_frame, lobby_frame):
        frame.grid(row=1, column=0, sticky='news', columnspan=4)

    # To be able to switch frames
    back_room_button = Button(root, text='Back Room', command= lambda: raise_frame(back_room_frame))
    kitchen_button = Button(root, text='Kitchen', command= lambda: raise_frame(kitchen_frame))
    lobby_button = Button(root, text='Lobby', command= lambda: raise_frame(lobby_frame))

    back_room_button.grid(row=0, column=2)
    kitchen_button.grid(row=0, column=1)
    lobby_button.grid(row=0, column=0)

    # Save button
    save_button = Button(root, text='Save', command= lambda: save_game())

    save_button.grid(row=0, column=3)

    LobbyView.create_customers()
    root.after(0, LobbyView.loop())


    raise_frame(lobby_frame)

    root.mainloop()