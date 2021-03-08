from tkinter import *

lobby_canvas = ''
player_character = []

def left(event):
    global lobby_canvas
    global player_character
    x = -15 # Left / right
    y = 0 # Up / down
    for piece in player_character:
        lobby_canvas.move(piece, x, y)

def right(event):
    global lobby_canvas
    global player_character
    x = 15 # Left / right
    y = 0 # Up / down
    for piece in player_character:
        lobby_canvas.move(piece, x, y)

def up(event):
    global lobby_canvas
    global player_character
    x = 0 # Left / right
    y = -15 # Up / down
    for piece in player_character:
        lobby_canvas.move(piece, x, y)

def down(event):
    global lobby_canvas
    global player_character
    x = 0 # Left / right
    y = 15 # Up / down
    for piece in player_character:
        lobby_canvas.move(piece, x, y)

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
    pass

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

    x = 45
    # Customers
    mr_blueberry = canvas_background.create_oval(x, y-50, x+100, y+300, fill="blue")

    x = 525
    miss_strawberry = canvas_background.create_oval(x, y-50, x+100, y+300, fill="pink")

    x = 775
    miss_anxious = canvas_background.create_oval(x, y-50, x+100, y+300, fill="yellow")

    # Character
    # character_location = Frame(f, width=450, height=450)
    # character_canvas = Canvas(character_location, width=300, height=300)

    y = 150
    head = canvas_background.create_oval(100, y,150, y +100, fill='gray90')
    player_character.append(head)

    x = 125
    y += 175
    stick = canvas_background.create_line(x, y-75, x, y)
    player_character.append(stick)

    diff_x = 25
    stick_leg1 = canvas_background.create_line(x, y, x-diff_x, y+50)
    player_character.append(stick_leg1)
    stick_leg2 = canvas_background.create_line(x, y, x+diff_x, y+50)
    player_character.append(stick_leg2)

    y -= 30
    stick_arm1 = canvas_background.create_line(x, y, x-30, y-20)
    player_character.append(stick_arm1)
    stick_arm2 = canvas_background.create_line(x, y, x+30, y-10)
    player_character.append(stick_arm2)

    # character_canvas.pack()
    # character_location.pack()


    # create_rectangle

    base_root.bind("<Key>", pressing)

    base_root.bind("<Left>", left)
    base_root.bind("<Right>", right)
    base_root.bind("<Up>", up)
    base_root.bind("<Down>", down)
    base_root.bind("<space>", location_tracker)

    lobby_canvas = canvas_background

    return f

if __name__ == "__main__":
    root = Tk()
    root.geometry("1100x800")
    lobby = create_frame(root)
    lobby.pack(fill='both', expand=True)

    root.mainloop()