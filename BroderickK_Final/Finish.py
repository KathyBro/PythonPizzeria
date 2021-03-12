from tkinter import *
import tkinter.font as tkFont

def the_end_window(the_final_score):
    root = Tk()
    root.title("Congratulations!!!!")
    root.geometry("400x300")

    main_frame = Frame(root)
    title_font = tkFont.Font(family="Arial 16 Bold", size=25)
    title = Label(main_frame, text="CONGRATULATIONS!!!",font=title_font)
    body = Message(main_frame, text=f"Way to go! You finished your shift and took your math test you got {(the_final_score/50)*100}%.")
    title.pack()
    body.pack()
    main_frame.pack()

    root.mainloop()

if __name__ == '__main__':
    the_end_window(49)