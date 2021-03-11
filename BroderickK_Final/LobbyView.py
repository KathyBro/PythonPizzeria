from tkinter import *
from Customer import customer
import PizzaAPIConnection as pizza
import random as rng
from tkinter.ttk import *

lobby_canvas = ''
player_character = []
customers= []
order_num = 4
base_root = ''

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

def loop():
    global base_root
    for i, cust in enumerate(customers):
        cust.time_left -= 1
        if cust.time_left == 0:
            cust.is_hungry = True
            draw_order_ready(i)
            cust.time_left = cust.eat_time
    
    base_root.after(1, loop)


def draw_order_ready(customer_num):
    global lobby_canvas
    global customers

    if customers[customer_num].is_hungry:
        x=0
        y=350

        if customer_num == 0:
            x=85
        elif customer_num == 1:
            x=560
        elif customer_num == 2:
            x=815

        tag = f"exclamation{customer_num}"
        line = lobby_canvas.create_rectangle(x,y,x+25, y+200, fill="red", tag=tag)

        customers[customer_num].is_hungry = True

        y += 220
        circle = lobby_canvas.create_oval(x, y, x+25, y+25, fill="red", tag=tag)

def take_order(customer_num):
    global customers
    global lobby_canvas
    global order_num
    print(customers[customer_num].is_hungry)

    if customers[customer_num].is_hungry:
        cust = customers[customer_num]
        # Remove exclamation point
        lobby_canvas.delete(f'exclamation{customer_num}')
        # Send order to API
        pizza.create_pizza_order(cust.order["Crust"], cust.order["Flavor"], order_num, cust.order["Size"], cust.order["Table_No"])
        # Customer isn't hungry
        customers[customer_num].is_hungry = False

        order_num += 1


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

def draw_customers(canvas_background):
    height = 700
    y = height//2
    x = 45
    
    mr_blueberry = canvas_background.create_oval(x, y-50, x+100, y+300, fill="blue")

    x = 525
    miss_strawberry = canvas_background.create_oval(x, y-50, x+100, y+300, fill="pink")

    x = 775
    lady_lemon = canvas_background.create_oval(x, y-50, x+100, y+300, fill="yellow")

def draw_character(canvas_background):
    global player_character
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

def create_frame(root):
    global lobby_canvas
    global base_root
    
    base_root = root
    
    f = Frame(root)

    width = 1100
    height = 700
    x = width//3
    y = height//2

    # Create the background
    canvas_background = Canvas(f, width=width, height=height)
    canvas_background.grid(column = 0, row = 1, columnspan=10)
    lobby_canvas = canvas_background

    image_background = PhotoImage(file=".\Pizzeria_Lobby.PNG")

    canvas_background.background = image_background
    bg = canvas_background.create_image(0, 0, anchor=NW, image=image_background)

    # Customers
    draw_customers(canvas_background)

    # Character    
    draw_character(canvas_background)


    base_root.bind("<Key>", pressing)
    base_root.bind("<Left>", left)
    base_root.bind("<Right>", right)
    # base_root.bind("<Up>", up)
    # base_root.bind("<Down>", down)
    base_root.bind("<space>", location_tracker)

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
        cust = customer()
        cust.name = customer_names[i]
        cust.order["Flavor"] = flavor[rng.randint(0,1)]
        cust.order["Size"] = size[rng.randint(0,2)]
        cust.order["Order_ID"] = order_num
        cust.order["Crust"] = crust[rng.randint(0,2)]
        cust.order["Table_No"] = i+1
        min = 10000 #30000
        max = 20000 #70000
        cust.order_patience = rng.randint(min, max)
        min = 10000 #12000
        max = 15000 #18000
        cust.eat_time = rng.randint(min, max)
        cust.time_left = cust.eat_time

        customers.append(cust)


if __name__ == "__main__":
    root = Tk()
    root.title("Python Pizzeria")
    root.geometry("1100x800")
    base_root = root
    create_customers()
    lobby = create_frame(root)
    root.after(0, loop)
    # draw_order_ready(2)
    lobby.pack(fill='both', expand=True)

    root.mainloop()