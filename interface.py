from Tkinter import *

class Application(Frame):
    def start_simulation(self):
        self.startB['state'] = 'disabled'
        print "Starting Simulation"
        self.startB['state'] = 'normal'

    def reset_simulation(self):
        print "Reseting Simulation"

    def createWidgets(self):
        self.startB = Button(self, text='Start', command=self.start_simulation)
        self.resetB = Button(self, text='Reset', command=self.reset_simulation)


        self.redblueScroll = Scale(self, orient=HORIZONTAL, label="Red/Blue Prob")
        self.redblueScroll.set(50)

        self.redblueScroll.pack(anchor=CENTER)
        self.startB.pack({"side": "left"})
        self.resetB.pack({"side": "left"})


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
