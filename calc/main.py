from tkinter import Tk, Button, Frame, Entry

class calculatorApp:
    def __init__(self, master):  

        self.master = master 

        # set the title of the window 
        self.master.title("Calculator")

        # set window size
        self.master.geometry("320x500")

        self.master.configure(bg="black")


        # infinite loop
        self.master.mainloop() 


if __name__ == "__main__":
    root = Tk()
    app = calculatorApp(root)
