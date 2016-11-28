from Tkinter import *
import time

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


        self.draw_board(30)

    def draw_board(self, size):
    	length = (self.w.winfo_reqwidth()-2)/size
    	for i in range(size):
    		for j in range(size):
    			if(j%2==0):
    				self.w.create_rectangle(i*length, j*length, (i+1)*length,(j+1)*length, fill="blue")
    			else:
    				self.w.create_rectangle(i*length, j*length, (i+1)*length,(j+1)*length, fill="red")
        time.sleep(0.1)

    def sayhi(self):
        print "hello"
        time.sleep(0.1)
        self.sayhi()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.w = Canvas(self, width = 250, height=250)
        self.createWidgets()
        self.w.pack()
        self.after(0, self.sayhi)

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
