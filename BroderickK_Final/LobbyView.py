from tkinter import *

lobby_canvas = ''
player_character = ''

def left(event):
    global lobby_canvas
    global player_character
    x = -15 # Left / right
    y = 0 # Up / down
    lobby_canvas.move(player_character, x, y)

def right(event):
    global lobby_canvas
    global player_character
    x = 15 # Left / right
    y = 0 # Up / down
    lobby_canvas.move(player_character, x, y)

def up(event):
    global lobby_canvas
    global player_character
    x = 0 # Left / right
    y = -15 # Up / down
    lobby_canvas.move(player_character, x, y)

def down(event):
    global lobby_canvas
    global player_character
    x = 0 # Left / right
    y = 15 # Up / down
    lobby_canvas.move(player_character, x, y)

def pressing(event):
    if event.char == "a":
        left('')
    elif event.char == "d":
        right('')
    elif event.char == "s":
        down('')
    elif event.char == "w":
        up('')

def location_tracker(event):
    

def create_frame(base_root):
    global lobby_canvas
    global player_character
    
    f = Frame(base_root)

    width = 1100
    height = 700
    x = width//3
    y = height//2


    # Create the background
    canvas_background = Canvas(f, width=width, height=height)
    canvas_background.pack()

    image_background = PhotoImage(file=".\Pizzeria_Lobby.PNG")

    canvas_background.background = image_background
    bg = canvas_background.create_image(0, 0, anchor=NW, image=image_background)

    # Character
    # character_location = Frame(f, width=450, height=450)
    # character_canvas = Canvas(character_location, width=300, height=300)

    # character_canvas.create_oval(100,50,150,100, fill='gray90')

    # x = 125
    # y = 175
    # stick = character_canvas.create_line(x, y-75, x, y)

    # diff_x = 25
    # stick_leg1 = character_canvas.create_line(x, y, x-diff_x, y+50)
    # stick_leg2 = character_canvas.create_line(x, y, x+diff_x, y+50)

    # y=145
    # stick_arm1 = character_canvas.create_line(x, y, x-30, y-20)
    # stick_leg2 = character_canvas.create_line(x, y, x+30, y-10)

    # character_canvas.pack()
    # character_location.pack()


    my_circle = canvas_background.create_oval(x, y-50, x+75, y+350, fill="blue")
    # create_rectangle

    base_root.bind("<Key>", pressing)

    base_root.bind("<Left>", left)
    base_root.bind("<Right>", right)
    base_root.bind("<Up>", up)
    base_root.bind("<Down>", down)
    base_root.bind("<Space>", location_tracking)

    lobby_canvas = canvas_background
    player_character = my_circle

    return f

if __name__ == "__main__":
    root = Tk()
    root.geometry("1100x800")
    lobby = create_frame(root)
    lobby.pack(fill='both', expand=True)

    root.mainloop()