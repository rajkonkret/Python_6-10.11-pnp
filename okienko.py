import tkinter


# tkinter - biblioteka do aplikacji okienkowych

class MyGui:  # deklaracja klasy
    def __init__(self):  # inicjalizator
        self.main_window = tkinter.Tk()

        self.label1 = tkinter.Label(self.main_window, text='Witaj świecie')
        self.label2 = tkinter.Label(self.main_window, text='Python')
        self.label3 = tkinter.Label(self.main_window, text='Góra')
        self.label4 = tkinter.Label(self.main_window, text='Dół')
        # dodac trzy labelki, umieszczone right, top, bottom
        self.label1.pack(side='left')
        self.label2.pack(side='right')
        self.label3.pack(side='top')
        self.label4.pack(side=tkinter.BOTTOM)  # Enum
        tkinter.mainloop()


my_gui = MyGui()
