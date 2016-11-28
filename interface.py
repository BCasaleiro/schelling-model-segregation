from Tkinter import *
import time

from random import random, randint
from math import pow, sqrt
from time import sleep

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
    mean_s = 0
    for l in range(n_m):
        for c in range(n_m):
            if(m[l][c] != -1):
                sat = calculate_individual_satisfation(m, l, c)
                mean_s += sat
                if sat < l_s or sat > m_s:
                    s.append( (l, c) )
    print 'mean satisfaction: {}'.format(float(mean_s) / (n_m * n_m))
    print 'satisfaction: {} {}'.format(len(s), 1 - float(len(s)) / (n_m * n_m))
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

def main():
    root = Tk()
    app = Application(master=root)
    root.mainloop()


class Application(Frame):
    def start_simulation(self):
        self.startB['state'] = 'disabled'
        print "Starting Simulation"

        self.s = calculate_satisfation(self.m, 0.75, 1)
        self.satisf = 1 - float(len(self.s)) / (len(self.m) * len(self.m))
        while len(self.s) > 0:
            self.m = moving_to_random(self.m, self.s)
            self.it += 1
            self.s = calculate_satisfation(self.m, 0.75, 1)
            print 'it: {}'.format(self.it)
            self.satisf = 1 - float(len(self.s)) / (len(self.m) * len(self.m))
            self.draw_board(self.m)
            time.sleep(self.stepS.get())

        self.startB['state'] = 'normal'

    def reset_simulation(self):
        self.it = 0
        self.satisf = 0.0
        self.startB['state'] = "normal"
        print "Reseting Simulation"

        self.m = generate_matrix(50)
        self.m = populate_matrix(self.m, 2, [0.5, 0.5], 250)
        print self.m

        self.itM = Message(self.rightFrame, text="Iteration: "+str(self.it), width=100)
        self.satisfM = Message(self.rightFrame, text="Satisfaction: "+str(self.satisf), width=150)
        self.satisfM.pack(side=BOTTOM)
        self.itM.pack(side=BOTTOM)
        self.draw_board(self.m)


    def createWidgets(self):
        controls = Frame(self)
        controls.pack(side=LEFT)

        self.startB = Button(controls, text='Start', command=self.start_simulation, state="disabled")
        self.resetB = Button(controls, text='Reset', command=self.reset_simulation)

        self.stepS = Scale(controls, orient=HORIZONTAL, label="Delay", from_=0, to=2, resolution=0.1)
        self.emptyS = Scale(controls, orient=HORIZONTAL, label="Empty(%)")

        self.heuristics = Listbox(controls)
        for item in ["random", "closest", "best"]:
            self.heuristics.insert(END, item)
        self.heuristics['state']='normal'

        var = StringVar()
        self.heuristics2 = OptionMenu(controls, var, *('train','plane'))
        self.startB.pack(side=TOP)
        self.resetB.pack(side=TOP)
        self.stepS.pack(side=LEFT)
        self.emptyS.pack(side=LEFT)

        #self.heuristics.pack()
        self.heuristics2.pack(side=BOTTOM)


    def draw_board(self, m):
        print "Drawing board"
        self.w.delete(ALL)
    	length = (self.w.winfo_reqwidth()-2)/len(self.m)
    	for i in range(len(self.m)):
    		for j in range(len(self.m)):
				if(m[i][j]==0):
					self.w.create_rectangle(j*length, i*length, (j+1)*length,(i+1)*length, fill="blue")
				elif(m[i][j]==1):
					self.w.create_rectangle(j*length, i*length, (j+1)*length,(i+1)*length, fill="red")
				elif(m[i][j]==-1):
					self.w.create_rectangle(j*length, i*length, (j+1)*length,(i+1)*length, fill="white")
				else:
					print "error"

        self.itM.config(text=("Iteration: "+str(self.it)))
        self.satisfM.config(text=("Satisfaction: "+str(self.satisf)))

        self.w.update()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.rightFrame = Frame(self)
        self.rightFrame.pack(side=RIGHT)
        self.w = Canvas(self.rightFrame, width = 350, height=350)
        self.createWidgets()
        self.w.pack(side=TOP)

        self.mainloop();

if __name__ == '__main__':
    main()
