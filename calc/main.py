from tkinter import Tk, Button, Frame, Entry, ttk, PhotoImage, LEFT, Label
import tkinter.font as font





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

        self.history_button = Button(self.master, background='black', text="History",fg='white' ,height=2, width=8)

        self.history_button.place(x=0,y=0)

    '''
    Set the display
    '''
    def display(self):
        self.label = Label(text="",fg='green', bg='gray', height=5, width=23, font=("Helvetica", 18))
        self.label.place(x=0,y=40)
        self.update_label()

    def update_label(self):
        pass

    '''
    The 24 buttons
    '''
    def all_buttons(self):
        row1 = 0
        row2 = 0
        row3 = 0
        row4 = 0
        row5 = 0
        row6 = 0
        y = 165
        buttons = ["%", "CE", "C", "X", '1/x',"1/x", "x^2", "x^1/2", "/", "7",'8','9','*','4','5','6','-','1','2','3','+','00','0','.','=']

        # define font
        myFont = font.Font(size=11, weight="bold", family='Courier')
        for i in range(25):
            text = buttons[i]
            if i <= 4:
                self.btn = Button(self.master, background='#3D3B32', text=text,fg='white' ,height=3, width=11)
                self.btn.place(x=row1,y=y)
                row1+= 80

                self.btn['font'] = myFont

            elif i > 4 and i <= 8:
                self.btn = Button(self.master, background='#3D3B32', text=text,fg='white' ,height=3, width=11)
                self.btn.place(x=row2,y=221)
                row2+= 80

                self.btn['font'] = myFont

            elif i > 8 and i <= 12:
                self.btn = Button(self.master, background='#3D3B32', text=text,fg='white' ,height=3, width=11)
                self.btn.place(x=row3,y=277)
                row3+= 80

                self.btn['font'] = myFont

            elif i > 12 and i <= 16:
                self.btn = Button(self.master, background='#3D3B32', text=text,fg='white' ,height=3, width=11)
                self.btn.place(x=row4,y=333)
                row4+= 80

                self.btn['font'] = myFont

            elif i > 16 and i <= 20:
                self.btn = Button(self.master, background='#3D3B32', text=text,fg='white' ,height=3, width=11)
                self.btn.place(x=row5,y=389)
                row5+= 80

                self.btn['font'] = myFont

            else:
                self.btn = Button(self.master, background='#3D3B32', text=text,fg='white' ,height=3, width=11)
                self.btn.place(x=row6,y=445)
                row6+= 80

                self.btn['font'] = myFont


if __name__ == "__main__":
    root = Tk()
    app = calculatorApp(root)
