from tkinter import Tk, Button, Frame, Entry, ttk, PhotoImage, LEFT
import math
from PIL import Image, ImageTk




class calculatorApp:
    def __init__(self, master):  

        self.master = master 

        # set the title of the window 
        self.master.title("Calculator")

        # set window size
        self.master.geometry("320x500")

        # set the background color of the window
        self.master.configure(bg="black")


        # calling the first row on display
        self.first_frame()
    
        


        # infinite loop
        self.master.mainloop() 


    '''
    First row of the calculator
    '''
    def first_frame(self):
        # photoimage for history icon on a button
        history = Image.open('./calc/history.png')

        # resize the image
        history = history.resize((20,20))

        # convert the image to a tkinter image
        history = ImageTk.PhotoImage(history)

        history_button = Button(self.master, image=history,height=20, width=20)

        history_button.place(x=0,y=10)




if __name__ == "__main__":
    root = Tk()
    app = calculatorApp(root)
