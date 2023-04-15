from tkinter import Tk, Button, Frame, Entry, ttk, PhotoImage, LEFT, Label
import tkinter.font as font

import customtkinter as ctk


ctk.set_appearance_mode("Dark")


class calculatorApp:
    def __init__(self, master):  

        self.master = master 

        # set the title of the window 
        self.master.title("Calculator")

        # set window size
        self.master.geometry("320x500")

        # set the background color of the window
        self.master.configure(bg="black")

        self.hist_button()
        self.display()
        self.all_buttons()
    
        


        # infinite loop
        self.master.mainloop() 


    '''
    First row of the calculator
    '''
    def hist_button(self):

        self.history_button = ctk.CTkButton(self.master,text="history", corner_radius = 8,height=2, width=8)

        self.history_button.place(x=0,y=0)

    '''
    Set the display
    '''
    def display(self):
        self.label = ctk.CTkEntry(self.master, height=120, width=315, text_color='green', bg_color='white')

        self.label.place(x=0,y=40)
        

    # def update_label(self, my_text):

    #     self.label.configure(text=my_text)

    '''
    The 24 buttons
    '''
    def all_buttons(self):
        row1 = 2
        row2 = 2
        row3 = 2
        row4 = 2
        row5 = 2
        row6 = 2
        y = 165
        buttons = ["%", "CE", "C", "X", '1/x',"1/x", "x^2", "x^1/2", "/", "7",'8','9','*','4','5','6','-','1','2','3','+','00','0','.','last']

        # define font
        myFont = font.Font(size=11, weight="bold", family='Courier')
        for i in range(25):
            text = buttons[i]
            if i <= 4:
                self.btn = ctk.CTkButton(self.master, text=text,height=50, fg_color='#3D3B32', width=75)

                self.btn.place(x=row1,y=y)
                row1+= 80
                self.btn['font'] = myFont

            elif i > 4 and i <= 8:
                self.btn = ctk.CTkButton(self.master, text=text,height=50, fg_color='#3D3B32', width=75)

                self.btn.place(x=row2,y=221)
                row2+= 80

                self.btn['font'] = myFont

            elif i > 8 and i <= 12:
                self.btn = ctk.CTkButton(self.master, text=text,height=50, fg_color='#3D3B32', width=75)

                self.btn.place(x=row3,y=277)
                row3+= 80

                self.btn['font'] = myFont

            elif i > 12 and i <= 16:
                self.btn = ctk.CTkButton(self.master, text=text,height=50, fg_color='#3D3B32', width=75)

                self.btn.place(x=row4,y=333)
                row4+= 80

                self.btn['font'] = myFont

            elif i > 16 and i <= 20:
                self.btn = ctk.CTkButton(self.master, text=text,height=50, fg_color='#3D3B32', width=75)

                self.btn.place(x=row5,y=389)
                row5+= 80

                self.btn['font'] = myFont

            else:
                self.btn = ctk.CTkButton(self.master, text=text,height=50, fg_color='#3D3B32', width=75)

                self.btn.place(x=row6,y=445)
                row6+= 80

                self.btn['font'] = myFont


if __name__ == "__main__":
    root = Tk()
    app = calculatorApp(root)
