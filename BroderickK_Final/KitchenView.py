from tkinter import *
import tkinter.font as tkFont
import PizzaAPIConnection as connection
from PIL import Image, ImageTk

pizza_canvas = ''
order = ''

def fill_new_order():
    global order
    # Delete old order

    # Get the new order
    orders = connection.get_pizza_orders()
    order.config(text='')
    print('Filled new order')

def add_crust():
    global pizza_canvas

    pizza_base = Image.open('.\PizzaBread.png')
    pizza_base.resize((400, 400))
    pizza_image = ImageTk.PhotoImage(pizza_base)
    # pizza_image = image_background

    pizza_canvas.background = pizza_image
    pizza_canvas.create_image(0, 0, anchor=NW, image=pizza_image)

def add_sauce():
    global pizza_canvas

    pizza_dough = Image.open('.\PizzaBread.png')
    pizza_dough.resize((400, 400))

    pizza_sauce = Image.open('.\Sauce.png')
    pizza_sauce.resize((400,400))
    pizza_dough.paste(pizza_sauce, (0, 0), pizza_sauce)

    pizza_image = ImageTk.PhotoImage(pizza_dough)

    pizza_canvas.background = pizza_image
    pizza_canvas.create_image(0, 0, anchor=NW, image=pizza_image)

def add_cheese():
    global pizza_canvas

    pizza_dough = Image.open('.\PizzaBread.png')
    pizza_dough.resize((400, 400))

    pizza_sauce = Image.open('.\Sauce.png')
    pizza_sauce.resize((400,400))
    pizza_dough.paste(pizza_sauce, (0, 0), pizza_sauce)

    pizza_cheese = Image.open('.\Cheese.png')
    pizza_cheese.resize((400, 400))
    pizza_dough.paste(pizza_cheese, (0, 0), pizza_cheese)

    pizza_image = ImageTk.PhotoImage(pizza_dough)

    pizza_canvas.background = pizza_image
    pizza_canvas.create_image(0, 0, anchor=NW, image=pizza_image)

def add_pepperoni():
    global pizza_canvas

    pizza_dough = Image.open('.\PizzaBread.png')
    pizza_dough.resize((400, 400))

    pizza_sauce = Image.open('.\Sauce.png')
    pizza_sauce.resize((400,400))
    pizza_dough.paste(pizza_sauce, (0, 0), pizza_sauce)

    pizza_cheese = Image.open('.\Cheese.png')
    pizza_cheese.resize((400, 400))
    pizza_dough.paste(pizza_cheese, (0, 0), pizza_cheese)

    pizza_pepperoni = Image.open('.\Pepperoni.png')
    pizza_pepperoni.resize((400, 400))
    pizza_dough.paste(pizza_pepperoni, (0,0), pizza_pepperoni)

    pizza_image = ImageTk.PhotoImage(pizza_dough)

    pizza_canvas.background = pizza_image
    pizza_canvas.create_image(0, 0, anchor=NW, image=pizza_image)

def create_frame(base_root):
    f = Frame(base_root)

    # Order on top
    order_canvas = Canvas(f, height = 150)
    order_canvas.pack(side='top', fill=X)


    # Crust on left
    crust_canvas = Canvas(f, width=250)
    crust_canvas.pack(side='left', fill=Y)

    # Pizza in middle and send
    global pizza_canvas
    pizza = Frame(f, width=550, height=800)
    canvas = Canvas(pizza, width=500, height=500)
    canvas.pack(pady=10)
    pizza_canvas = canvas


    # Toppings on right
    toppings_canvas = Canvas(f, width=250)
    toppings_canvas.pack(side='right', fill=Y)

    pizza.pack()

    

    toppings_canvas.configure(background = 'red')
    pizza.configure(background='green')
    crust_canvas.configure(background='pink')
    order_canvas.configure(background='blue')

    # Order
    submit_button = Button(order_canvas, text='Submit', command= lambda: fill_new_order(), width=10, height=5)
    submit_button.grid(column=0, row=0, padx=10, pady=10)
    order_label = Label(order_canvas, text='Crust: Thin\tTopping:Pepperoni')
    order_label.grid(column=1, row=0, columnspan=3, padx=10)
    global order
    order = order_label

    # Thin, stuffed, pan
    crust_font = tkFont.Font(family='Arial 16 bold', size=12)
    crust_label = Label(crust_canvas, text='Crust', font=crust_font)
    crust_label.pack(padx=10, pady=(30, 20))
    thin_button = Button(crust_canvas, text='Thin', width=20, command= lambda: add_crust())
    thin_button.pack(padx=10, pady=10)
    stuffed_button = Button(crust_canvas, text='Stuffed', width=20, command= lambda: add_crust())
    stuffed_button.pack(padx=10, pady=10)
    pan_button = Button(crust_canvas, text='Pan',width=20, command= lambda: add_crust())
    pan_button.pack(padx=10, pady=10)

    # Toppings
    toppings_label = Label(toppings_canvas, text='Toppings', font=crust_font)
    toppings_label.pack(padx=10, pady=(30, 20))
    sauce_button = Button(toppings_canvas, text='Sauce', width=20, command= lambda: add_sauce())
    sauce_button.pack(padx=10, pady=10)
    cheese_button = Button(toppings_canvas, text='Cheese', width=20, command= lambda: add_cheese())
    cheese_button.pack(padx=10, pady=10)
    pepperoni_button = Button(toppings_canvas, text='Pepperoni', width=20, command= lambda: add_pepperoni())
    pepperoni_button.pack(padx=10, pady=10)

    return f

if __name__ == '__main__':
    root = Tk()
    root.geometry("1100x800")
    kitchen = create_frame(root)

    kitchen.pack(fill='both', expand=True)

    root.mainloop()