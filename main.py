from Tkinter import *
import time
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

from random import random, randint
from math import pow, sqrt
from time import sleep

mean_s = 0.0

def print_matrix(m):                                                            #TODO: remove this method
    for i in m:
        print i

def calculate_cumulative_prob(n, p):
    """
    generate_matrix method

    Parameters:
        n (int): dimension of the array
        p (array:float): array of probabilities
    Returns:
        p (array:float): cumulative version of the array inputed
    """
    for i in range(1, n):
        p[i] += p[i - 1]

    return p

def generate_matrix(n):
    """
    generate_matrix method

    Parameters:
        n (int): dimension of the neighborhood
    Returns:
        m (array:array:int): n by n matrix populated with 0's
    """
    return [[0 for i in range(n)] for k in range(n)]

def populate_matrix(m, n, p, e):
    """
    populate_matrix method

    Parameters:
        m (array:array:int): matrix representing the neighborhood
        n (int): number of ethnicities
        p (array:float): array of probabilitie for each ethnicity
        e (int): number of empty spots
    Returns:
        m (array:array:int): populated neighborhood with the individuals of each ethnicity and also e empty spots
    """

    n_m = len(m)
    p = calculate_cumulative_prob(n, p)

    for l in range(n_m):
        for c in range(n_m):
            r = random()
            for et_i, et_p in enumerate(p):
                if r <= et_p:
                    m[l][c] = et_i
                    break

    for i in range(e):
        l = randint(0, len(m) - 1)
        c = randint(0, len(m) - 1)
        if m[l][c] == -1:
            i -= 1
        else:
            m[l][c] = -1

    return m

def is_not_empty_spot(n):
    if n == -1:
        return 0
    else:
        return 1

def is_same_kind(k, n):
    if n == k:
        return 1
    else:
        return 0

def calculate_poss_individual_satisfation(m, l, c, v):
    n_m = len(m)
    count = 0
    sm = 0
    if l - 1 >= 0:
        count += is_not_empty_spot(m[l - 1][c])
        sm += is_same_kind(m[l - 1][c], v)

        if c - 1 >= 0:
            count += is_not_empty_spot(m[l - 1][c - 1])
            sm += is_same_kind(m[l - 1][c - 1], v)
        if c + 1 < n_m:
            count += is_not_empty_spot(m[l - 1][c + 1])
            sm += is_same_kind(m[l - 1][c + 1], v)
    if l + 1 < n_m:
        count += is_not_empty_spot(m[l + 1][c])
        sm += is_same_kind(m[l + 1][c], v)

        if c - 1 >= 0:
            count += is_not_empty_spot(m[l + 1][c - 1])
            sm += is_same_kind(m[l + 1][c - 1], v)
        if c + 1 < n_m:
            count += is_not_empty_spot(m[l + 1][c + 1])
            sm += is_same_kind(m[l + 1][c + 1], v)
    if c - 1 >= 0:
        count += is_not_empty_spot(m[l][c - 1])
        sm += is_same_kind(m[l][c - 1], v)
    if c + 1 < n_m:
        count += is_not_empty_spot(m[l][c + 1])
        sm += is_same_kind(m[l][c + 1], v)

    if count == 0:
        return 1
    else:
        return float(sm)/count

def calculate_individual_satisfation(m, l, c):
    n_m = len(m)
    count = 0
    sm = 0
    if l - 1 >= 0:
        count += is_not_empty_spot(m[l - 1][c])
        sm += is_same_kind(m[l - 1][c], m[l][c])

        if c - 1 >= 0:
            count += is_not_empty_spot(m[l - 1][c - 1])
            sm += is_same_kind(m[l - 1][c - 1], m[l][c])
        if c + 1 < n_m:
            count += is_not_empty_spot(m[l - 1][c + 1])
            sm += is_same_kind(m[l - 1][c + 1], m[l][c])
    if l + 1 < n_m:
        count += is_not_empty_spot(m[l + 1][c])
        sm += is_same_kind(m[l + 1][c], m[l][c])

        if c - 1 >= 0:
            count += is_not_empty_spot(m[l + 1][c - 1])
            sm += is_same_kind(m[l + 1][c - 1], m[l][c])
        if c + 1 < n_m:
            count += is_not_empty_spot(m[l + 1][c + 1])
            sm += is_same_kind(m[l + 1][c + 1], m[l][c])
    if c - 1 >= 0:
        count += is_not_empty_spot(m[l][c - 1])
        sm += is_same_kind(m[l][c - 1], m[l][c])
    if c + 1 < n_m:
        count += is_not_empty_spot(m[l][c + 1])
        sm += is_same_kind(m[l][c + 1], m[l][c])

    if count == 0:
        return 1
    else:
        return float(sm)/count

def calculate_satisfation(m, l_s, m_s):
    n_m = len(m)
    s = []
    mea_s = 0
    for l in range(n_m):
        for c in range(n_m):
            if(m[l][c] != -1):
                sat = calculate_individual_satisfation(m, l, c)
                mea_s += sat
                if sat < l_s or sat > m_s:
                    s.append( (l, c) )
    global mean_s
    mean_s = float(mea_s) / (n_m * n_m)
    # print 'mean satisfaction: {}'.format(mean_s)
    # print 'satisfaction: {} {}'.format(len(s), 1 - float(len(s)) / (n_m * n_m))

    return s

def get_empty_spots_with_past(m):
    e = []
    n_m = len(m)

    for l in range(n_m):
        for c in range(n_m):
            if m[l][c] == -1:
                e.append( [l, c, -1, -1] )

    return e

def get_empty_spots(m):
    e = []
    n_m = len(m)

    for l in range(n_m):
        for c in range(n_m):
            if m[l][c] == -1:
                e.append( (l,c) )

    return e

def get_nearest_empty_with_past(e, n, l, c):
    d = n + 1
    for e_i, e_v in enumerate(e):
        if e_v[2] != l and e_v[3] != c:
            d_t = sqrt( pow(l - e_v[0], 2) + pow(c - e_v[1], 2) )
            if d_t < d:
                i = e_i
                d = d_t

    return i

def get_nearest_empty(e, n, l, c):
    d = n + 1
    for e_i, e_v in enumerate(e):
        d_t = sqrt( pow(l - e_v[0], 2) + pow(c - e_v[1], 2) )
        if d_t < d:
            i = e_i
            d = d_t

    return i

def get_best_satisfation(m, e, l, c):
    b = 0
    for e_i, e_v in enumerate(e):
        b_t = calculate_poss_individual_satisfation(m, e_v[0], e_v[1], m[l][c])
        if b_t > b:
            i = e_i
            b = b_t

    return i

def moving_to_best(m, s):
    e = get_empty_spots(m)

    for s_i in s:
        e_i = get_best_satisfation(m, e, s_i[0], s_i[1])
        m[ e[e_i][0] ][ e[e_i][1] ] = m[ s_i[0] ][ s_i[1] ]
        m[ s_i[0] ][ s_i[1] ] = -1
        e[e_i] = (s_i[0], s_i[1])

    return m

def moving_to_nearest(m, s):
    e = get_empty_spots_with_past(m)
    n_m = len(m)

    for s_i in s:
        e_i = get_nearest_empty_with_past(e, n_m, s_i[0], s_i[1])
        m[ e[e_i][0] ][ e[e_i][1] ] = m[ s_i[0] ][ s_i[1] ]
        m[ s_i[0] ][ s_i[1] ] = -1
        e[e_i] = [s_i[0], s_i[1], e[e_i][0], e[e_i][1]]

    return m

def moving_to_random(m, s):
    e = get_empty_spots(m)

    for s_i in s:
        r = randint(0, len(e) - 1)
        m[ e[r][0] ][ e[r][1] ] = m[ s_i[0] ][ s_i[1] ]
        m[ s_i[0] ][ s_i[1] ] = -1
        e[r] = (s_i[0], s_i[1])

    return m

def plot():

    mx = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    my = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    mz = [[0 for x in range(10)] for y in range(10)]

    for x in range(len(mx)):
        for y in range(len(mx)):
			global mean_s
			mean_s = 0.0
			if y > x:
				m = generate_matrix(50)
				m = populate_matrix(m, 3, [0.33,0.33,0.34], 75)
				it = 0
				s = calculate_satisfation(m, mx[x], my[y])
				while len(s) > 0:
					m = moving_to_random(m, s)
					s = calculate_satisfation(m, mx[x], my[y])
					it += 1
					if it > 1000:
						break
				mz[x][y] = float(mean_s)
				print mean_s
			else:
				mz[x][y] = float(mean_s)
				print '({},{})\t{}'.format(mx[x], my[y], mz[x][y])

	print mz
	# mz = [
 #        [0.0, 0.4508647619047619, 0.4496752380952378, 0.3560033333333331, 0.3014742857142886, 0.3337709523809551, 0.3711800000000024, 0.41911666666666697, 0.44966190476190443, 0.4754123809523805],
 #        [0.0, 0.0, 0.450681904761904, 0.433738571428572, 0.3460419047619064, 0.33059857142857246, 0.3805328571428591, 0.42845380952380974, 0.49392761904761956, 0.509778095238096],
 #        [0.0, 0.0, 0.0, 0.44562476190476136, 0.4388652380952384, 0.44037285714285773, 0.4526504761904761, 0.5025661904761891, 0.5621900000000012, 0.6882757142857162],
 #        [0.0, 0.0, 0.0, 0.0, 0.4565504761904761, 0.45610761904761865, 0.4767585714285714, 0.5154728571428577, 0.6016885714285748, 0.7458323809523839],
 #        [0.0, 0.0, 0.0, 0.0, 0.0, 0.4572161904761909, 0.4691385714285705, 0.5160771428571425, 0.5944390476190496, 0.8015219047619059],
 #        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4582071428571421, 0.5062747619047607, 0.5961104761904776, 0.8844371428571418],
 #        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.46510666666666695, 0.49884714285714316, 0.9001599999999996],
 #        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.44835904761904793, 0.47232476190476225],
 #        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.45494714285714327],
 #        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
 #        ]

    data = [
    go.Contour(
        z = mz,
        x = mx,
        y = mx
    )]

    py.plot(data)

def main():
    plot()
    # root = Tk()
    # root.wm_title("Schelling Model Segregation")
    # app = Application(master=root)
    # root.mainloop()

class Application(Frame):
    def start_simulation(self):
        self.widgets_state_change("disabled")
        self.stopB['state'] = 'normal'
        print "Starting Simulation"

        self.s = calculate_satisfation(self.m, self.minS.get(), self.maxS.get())
        self.satisf = 1 - float(len(self.s)) / (len(self.m) * len(self.m))
        self.segreg = float(mean_s)
        while len(self.s) > 0 and self.stopped==0:
            self.choose_method()
            self.it += 1
            self.s = calculate_satisfation(self.m, self.minS.get(), self.maxS.get())
            print 'it: {}'.format(self.it)
            self.satisf = 1 - float(len(self.s)) / (len(self.m) * len(self.m))
            self.segreg = float(mean_s)
            self.draw_board(self.m)
            time.sleep(self.stepS.get())

        self.widgets_state_change("normal")
        self.startB['state'] = 'disabled'
        self.stopB['state'] = 'disabled'

    def widgets_state_change(self, state):
        self.startB['state'] = state
        self.resetB['state'] = state
        self.emptyS['state'] = state
        self.maxS['state'] = state
        self.minS['state'] = state
        self.proportionS['state'] = state
        self.stepS['state'] = state
        self.heuristics['state'] = state
        self.races['state'] = state
        self.sizeBoardS['state'] = state


    def choose_method(self):
        method = self.choice.get()
        if(method=="Random"):
            self.m = moving_to_random(self.m, self.s)
        elif(method=="Best"):
            self.m = moving_to_best(self.m, self.s)
        elif(method=="Closest"):
            self.m = moving_to_nearest(self.m, self.s)

    def reset_simulation(self):
        self.it = 0
        self.satisf = 0.0
        self.segreg = 0.0
        self.stopped=0

        self.startB['state'] = "normal"
        self.stopB['state'] = 'disabled'
        print "Reseting Simulation"

        numEmptySpaces = int(self.sizeBoardS.get()*self.sizeBoardS.get()*self.emptyS.get())
        self.m = generate_matrix(self.sizeBoardS.get())

        if(self.numRaces.get()=="2"):
            self.m = populate_matrix(self.m, 2, [self.proportionS.get(), 1-self.proportionS.get()], numEmptySpaces)
        else:
            self.m = populate_matrix(self.m, 3, [0.33,0.33,0.33], numEmptySpaces)

        self.draw_board(self.m)

    def stop_simulation(self):
        self.stopped=1
        self.stopB['state'] = ['disabled']
        self.widgets_state_change("normal")
        self.startB['state'] = ['disabled']

    def createWidgets(self):
        leftFrame = Frame(self)
        leftFrame.pack(side=LEFT)

        actionsFrame = Frame(leftFrame, bd=15)
        actionsFrame.pack(side=TOP)
        self.startB = Button(actionsFrame, text='Start', font="bold", command=self.start_simulation, state="disabled")
        self.resetB = Button(actionsFrame, text='Reset', font="bold", command=self.reset_simulation)
        self.stopB = Button(actionsFrame, text='Stop', font="bold", command=self.stop_simulation)

        self.startB.pack(side=LEFT)
        self.resetB.pack(side=LEFT)
        self.stopB.pack(side=LEFT)

        optionsFrame = Frame(leftFrame)
        optionsFrame.pack(side=BOTTOM)

        heuristicFrame = Frame(optionsFrame)
        heuristicFrame.pack(side=TOP)
        self.choice = StringVar(self)
        self.choice.set('Random')
        self.heuristics = OptionMenu(heuristicFrame, self.choice, *('Random','Best', 'Closest'))
        self.heurMessage = Message(heuristicFrame, text="Heuristic:", width=100)


        racesFrame = Frame(optionsFrame)
        racesFrame.pack(side=TOP)
        self.numRaces = StringVar(self)
        self.numRaces.set('2')
        self.races = OptionMenu(racesFrame, self.numRaces, *('2', '3'))
        self.racesMessage = Message(racesFrame, text="Number of Races:", width=200)

        self.racesMessage.pack(side=LEFT)
        self.races.pack(side=LEFT)

        emptyFrame = Frame(optionsFrame)
        emptyFrame.pack(side=TOP)
        self.emptyS = Scale(emptyFrame, orient=HORIZONTAL, from_=0, to=1, resolution=0.005)
        self.emptyS.set(0.1)
        self.emptyM = Message(emptyFrame, text="Empty:", width=50)
        self.emptyM.pack(side=LEFT)
        self.emptyS.pack(side=LEFT)

        minFrame = Frame(optionsFrame)
        minFrame.pack(side=TOP)
        self.minS = Scale(minFrame, orient=HORIZONTAL, from_=0, to=1, resolution=0.05)
        self.minM = Message(minFrame, text="Low limit:", width = 100)
        self.minM.pack(side=LEFT)
        self.minS.pack(side=LEFT)

        maxFrame = Frame(optionsFrame)
        maxFrame.pack(side=TOP)
        self.maxS = Scale(maxFrame, orient=HORIZONTAL, from_=0, to=1, resolution=0.05)
        self.maxM = Message(maxFrame, text="High limit:", width = 100)
        self.maxM.pack(side=LEFT)
        self.maxS.pack(side=LEFT)

        propFrame = Frame(optionsFrame)
        propFrame.pack(side=TOP)
        self.proportionS = Scale(propFrame, orient=HORIZONTAL, from_=0, to=1, resolution=0.05)
        self.propM = Message(propFrame, text="Proportion:", width = 100)
        self.propM.pack(side=LEFT)
        self.proportionS.pack(side=LEFT)

        delayFrame = Frame(optionsFrame)
        delayFrame.pack(side=TOP)
        self.stepS = Scale(delayFrame, orient=HORIZONTAL, from_=0, to=2, resolution=0.1)
        self.stepM = Message(delayFrame, text="Delay:", width=50)
        self.stepM.pack(side=LEFT)
        self.stepS.pack(side=LEFT)

        sizeFrame = Frame(optionsFrame)
        sizeFrame.pack(side=TOP)
        self.sizeBoardS = Scale(sizeFrame, orient=HORIZONTAL)
        self.sizeM = Message(sizeFrame, text="Board Size:", width = 100)
        self.sizeM.pack(side=LEFT)
        self.sizeBoardS.pack(side=LEFT)


        #initialize values to default:
        self.minS.set(0.75)
        self.maxS.set(1)
        self.proportionS.set(0.5)
        self.sizeBoardS.set(50)

        #self.heuristics.pack()
        self.heurMessage.pack(side=LEFT)
        self.heuristics.pack(side=LEFT)

        self.stepS.pack(side=TOP)


        self.proportionS.pack(side=TOP)
        self.sizeBoardS.pack(side=TOP)

        self.it = 0.0
        self.satisf = 0.0
        self.segreg = 0.0
        self.itM = Message(self.rightFrame, text="Iteration: "+str(self.it), width=100)
        self.satisfM = Message(self.rightFrame, text="Satisfaction: "+str(self.satisf), width=150)
        self.segregM = Message(self.rightFrame, text="Segregation: " +str(self.segreg), width=150)
        self.segregM.pack(side=BOTTOM)
        self.satisfM.pack(side=BOTTOM)
        self.itM.pack(side=BOTTOM)

    def draw_board(self, m):
        print "Drawing board"
        self.w.delete(ALL)
        length = float(self.w.winfo_reqwidth()-2)/len(self.m)
        for i in range(len(self.m)):
            for j in range(len(self.m)):
                if(m[i][j]==0):
                    color="green"
                elif(m[i][j]==1):
                    color="orange"
                elif(m[i][j]==2):
                    color="blue"
                elif(m[i][j]==-1):
                    color="white"
                else:
                    print "error"
                self.w.create_rectangle(j*length, i*length, (j+1)*length,(i+1)*length, fill=color)

        self.w.create_rectangle(1,1,350,350, width=3)

        self.itM.config(text=("Iteration: "+str(self.it)))
        self.satisfM.config(text="Satisfaction: {:6.6f}".format(self.satisf))
        self.segregM.config(text="Segregation: {:6.6f}".format(self.segreg))
        self.w.update()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.stopped = 0
        self.pack()
        self.rightFrame = Frame(self)
        self.rightFrame.pack(side=RIGHT)
        self.w = Canvas(self.rightFrame, width = 350, height=350)
        self.w.create_rectangle(1,1,350,350)
        self.createWidgets()
        self.w.pack(side=TOP)
        self.mainloop();

if __name__ == '__main__':
    plotly.tools.set_credentials_file(username='bcasaleiro', api_key='VRnrNNTYpWjkbCFgxZ9w')
    main()
