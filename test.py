from Tkinter import *

class Application(Frame):
    def GenerateList(self):
        print "hi there, everyone!"

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "Quit"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.grid(row=0, column=1)

        self.hi_there = Button(self)
        self.hi_there["text"] = "Generate List",
        self.hi_there["command"] = self.GenerateList

        self.hi_there.grid(row=0, column=2)
        self.recipeEntryFields()

    def recipeEntryFields(self):
        self.recipeButtons = []

        for i in range(0,5):
            self.recipeButtons.append(Entry(self))
            self.label = Label(self, text="Test")
            self.label.grid(row=i + 1, column=1)
            self.recipeButtons[i].grid(row=i + 1, column=2)
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.master.title("Python Planner")
app.master.minsize(1000, 400)
app.mainloop()
root.destroy()
