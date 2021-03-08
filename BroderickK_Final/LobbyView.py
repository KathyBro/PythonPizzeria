from tkinter import *
import Customer
import random as rng

lobby_canvas = ''
player_character = []
customers= []
order_num = 4

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

# def up(event):
#     global lobby_canvas
#     global player_character
#     x = 0 # Left / right
#     y = -15 # Up / down
#     for piece in player_character:
#         lobby_canvas.move(piece, x, y)

# def down(event):
#     global lobby_canvas
#     global player_character
#     x = 0 # Left / right
#     y = 15 # Up / down
#     for piece in player_character:
#         lobby_canvas.move(piece, x, y)

def pressing(event):
    if event.char == "a":
        left('')
    elif event.char == "d":
        right('')
    # elif event.char == "s":
    #     down('')
    # elif event.char == "w":
    #     up('')

def take_order(customer_num):
    pass

def location_tracker(event):
    global lobby_canvas
    global player_character
    coords = lobby_canvas.coords(player_character[0])
    x1 = coords[0]

    if x1 >= 0 and x1 <=90:
        print("Customer 1")
        take_order(0)
    elif x1 >= 405 and x1 <= 570:
        print("Customer 2")
        take_order(1)
    elif x1 >= 660 and x1 <=840:
        print("Customer 3")
        take_order(2)
    else:
        print(x1)

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

    # image_background = PhotoImage(file=".\Pizzeria_Lobby.PNG")

    # canvas_background.background = image_background
    # bg = canvas_background.create_image(0, 0, anchor=NW, image=image_background)

    x = 45
    # Customers
    mr_blueberry = canvas_background.create_oval(x, y-50, x+100, y+300, fill="blue")

    x = 525
    miss_strawberry = canvas_background.create_oval(x, y-50, x+100, y+300, fill="pink")

    x = 775
    lady_lemon = canvas_background.create_oval(x, y-50, x+100, y+300, fill="yellow")

    # Character
    # character_location = Frame(f, width=450, height=450)
    # character_canvas = Canvas(character_location, width=300, height=300)
    
    x = 300
    y = 345
    head = canvas_background.create_oval(x, y, x+150, y +150, fill='gray90', width=4)
    player_character.append(head)

    x += 75
    y += 225
    stick = canvas_background.create_line(x, y-75, x, y+75, width=4)
    player_character.append(stick)

    diff_x = 50
    stick_leg1 = canvas_background.create_line(x, y+75, x-diff_x, y+135, width=4)
    player_character.append(stick_leg1)
    stick_leg2 = canvas_background.create_line(x, y+75, x+diff_x, y+135, width=4)
    player_character.append(stick_leg2)

    y -= 30
    stick_arm1 = canvas_background.create_line(x, y, x-30, y-20, width=4)
    player_character.append(stick_arm1)
    stick_arm2 = canvas_background.create_line(x, y, x+30, y-10, width=4)
    player_character.append(stick_arm2)

    # create_rectangle

    base_root.bind("<Key>", pressing)

    base_root.bind("<Left>", left)
    base_root.bind("<Right>", right)
    # base_root.bind("<Up>", up)
    # base_root.bind("<Down>", down)
    base_root.bind("<space>", location_tracker)

    lobby_canvas = canvas_background

    return f

def create_customers():
    global customers
    global order_num
    flavor = ["CHEESE", "PEPPERONI"]
    size = ["S", "M", "L"]
    crust = ["THIN", "PAN", "STUFFED"]
    customer_names = ["Mr. Blueberry", "Miss Strawberry", "Lady Lemon"]

    # mr blueberry, miss strawberry, and lady lemon
    for i in range(0, 3):
        cust = Customer()
        cust.name = customer_names[i]
        cust.order["Flavor"] = flavor[rng.randint(0,1)]
        cust.order["Size"] = size[rng.randint(0,2)]
        cust.order["Order_ID"] = order_num
        order_num += 1
        cust.order["Table_No"] = i

if __name__ == "__main__":
    root = Tk()
    root.title("Python Pizzeria")
    root.geometry("1100x800")
    lobby = create_frame(root)
    lobby.pack(fill='both', expand=True)

    root.mainloop()