import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Arc
import pandas as pd
import numpy as np
class Pitch:

    def __init__(self, col="white", custom_dim = None, vert= False, half=False, grid = False):
        self.vert= vert
        self.half = half
        if custom_dim is not None:
            self.X = custom_dim['x']
            self.Y = custom_dim['y']
            self.pen_width = custom_dim['pen_width']
            self.pen_length = custom_dim['pen_length']
            self.six_length = custom_dim['six_yard_length']
            self.six_width = custom_dim['six_yard_width']
            self.pen_dist = custom_dim['pen_spot_distance']
        else:
            self.X = (0,120)
            self.Y = (80,0)
            self.pen_width = 18
            self.pen_length = 44
            self.six_length = 20
            self.six_width = 6
            self.pen_dist = 12

        self.grid = grid


        self.pass_network_ = False
        self.pitch_col = col


    def add_passes(self, passes, col = ''):
        self.passes = passes
        self.pass_col = col
    def add_shots(self, xy, col= '', size = -1):
        self.shots = xy
        self.shots_col = col
        self.shots_size = size
    def pass_network(self, passes,passerId, recieverId):
        self.pn_passes = passes
        self.pn_passerids = passerId
        self.pn_recieverids = recieverId
        self.pass_network_ = True

    def plot_pn(self):
        df = pd.DataFrame(self.pn_passes, columns=['x1','y1','x2','y2'])
        df2 = pd.DataFrame(self.pn_passerids, columns=['passerId'])
        df3 = pd.DataFrame(self.pn_recieverids, columns=['recId'])
        df = pd.concat((df,df2,df3), axis=1)


        ids = df['passerId'].unique().tolist()
        ids2 = df['recId'].unique().tolist()
        ids = ids + ids2
        ids = set(ids)

        player_locs = []
        for id in ids:
            passing = df[df['passerId']==id]
            rec = df[df['recId'] == id]

            passing1 = passing[['x1','y1']].values
            rec1 = rec[['x2','y2']].values

            locs = np.concatenate((passing1,rec1))

            means = locs.mean(axis=0)
            x_loc = means[0]
            y_loc = means[1]

            loc = [x_loc, y_loc]
            player_locs.append(loc)
        ids = list(ids)

        num_pass = []
        for pl1_i in range(len(ids)):
            pl1 = ids[pl1_i]
            for pl2 in range(pl1_i + 1, len(ids)):
                pl2 = ids[pl2]
                df_con = df[((df['passerId'] == pl1) & (df['recId'] == pl2)) | ((df['passerId'] == pl2) & (df['recId'] == pl1))]
                num_pass.append(len(df_con))

        sum_pass = sum(num_pass)
        pass_connection = [x / sum_pass for x in num_pass]
        n = 0
        for pl1 in range(len(ids)):
            pl1_locs = player_locs[pl1]
            for pl2 in range(pl1 + 1, len(ids)):
                pl2_locs = player_locs[pl2]
                con = pass_connection[n]
                plt.scatter([pl1_locs[0],pl2_locs[0]], [pl1_locs[1],pl2_locs[1]], c='black')
                plt.plot([pl1_locs[0],pl2_locs[0]], [pl1_locs[1],pl2_locs[1]], alpha = con, c = 'black',linewidth = 4.0)
                n += 1


    def create_pitch(self, ax):

        #create pitch borders and centerline
        plt.plot((self.X[0],self.X[0]),(self.Y[0],self.Y[1]),c = 'black')
        plt.plot((self.X[0],self.X[1]),(self.Y[0],self.Y[0]), c='black')
        plt.plot((self.X[1],self.X[1]),(self.Y[0],self.Y[1]), c='black')
        plt.plot((self.X[0],self.X[1]),(self.Y[1],self.Y[1]), c='black')
        plt.plot(((self.X[1] + self.X[0])/2,(self.X[1] + self.X[0])/2),(self.Y[0],self.Y[1]), c='black')

        #add centre circle and dot
        plt.scatter((self.X[1] + self.X[0])/2,(self.Y[1] + self.Y[0])/2, c='black', s = 15)
        ax.add_artist(plt.Circle(((self.X[1] + self.X[0])/2,(self.Y[1] + self.Y[0])/2),(self.Y[1] - self.Y[0]) * 0.1,color='black', fill=False))

        #add penalty box
        plt.plot((self.X[0],self.X[0] + self.pen_width),(self.Y[0] + ((self.Y[1] - self.Y[0]) - self.pen_length)/2 ,self.Y[0] + ((self.Y[1] - self.Y[0]) - self.pen_length)/2), c='black')
        plt.plot((self.X[0],self.X[0] + self.pen_width),(self.Y[1] - ((self.Y[1] - self.Y[0]) - self.pen_length)/2,(self.Y[1] - ((self.Y[1] - self.Y[0]) - self.pen_length)/2)), c='black')
        plt.plot((self.X[0] + self.pen_width, self.X[0] + self.pen_width),(self.Y[0] + ((self.Y[1] - self.Y[0]) - self.pen_length)/2,(self.Y[1] - ((self.Y[1] - self.Y[0]) - self.pen_length)/2)), c='black')
        #left 6 yeard box
        plt.plot((self.X[0],self.X[0] + self.six_width),(self.Y[0] + ((self.Y[1] - self.Y[0]) - self.six_length)/2,self.Y[0] + ((self.Y[1] - self.Y[0]) - self.six_length)/2), c='black')
        plt.plot((self.X[0], self.X[0] + self.six_width),(self.Y[1] - ((self.Y[1] - self.Y[0]) - self.six_length)/2,self.Y[1] - ((self.Y[1] - self.Y[0]) - self.six_length)/2), c='black')
        plt.plot((self.X[0] + self.six_width, self.X[0] + self.six_width),(self.Y[0] + ((self.Y[1] - self.Y[0]) - self.six_length)/2, self.Y[1] - ((self.Y[1] - self.Y[0]) - self.six_length)/2), c='black')
        #left pen spot and arc
        ax.add_patch(Arc((self.X[0] + self.pen_dist,(self.Y[1] + self.Y[0] )/2), width = (self.Y[1] - self.Y[0]) * 0.23, height=(self.Y[1] - self.Y[0]) * 0.23, theta1=310, theta2=50, angle=180))
        plt.scatter(self.X[0] + self.pen_dist,(self.Y[1] + self.Y[0])/2, c='black', s =  15)

        #add penalty box
        plt.plot((self.X[1],self.X[1] -  self.pen_width),(self.Y[0] + ((self.Y[1] - self.Y[0]) - self.pen_length)/2 ,self.Y[0] + ((self.Y[1] - self.Y[0]) - self.pen_length)/2), c='black')
        plt.plot((self.X[1],self.X[1] - self.pen_width),(self.Y[1] - ((self.Y[1] - self.Y[0]) - self.pen_length)/2,(self.Y[1] - ((self.Y[1] - self.Y[0]) - self.pen_length)/2)), c='black')
        plt.plot((self.X[1] - self.pen_width, self.X[1] - self.pen_width),(self.Y[0] + ((self.Y[1] - self.Y[0]) - self.pen_length)/2,(self.Y[1] - ((self.Y[1] - self.Y[0]) - self.pen_length)/2)), c='black')
        #left 6 yeard box
        plt.plot((self.X[1],self.X[1] - self.six_width),(self.Y[0] + ((self.Y[1] - self.Y[0]) - self.six_length)/2,self.Y[0] + ((self.Y[1] - self.Y[0]) - self.six_length)/2), c='black')
        plt.plot((self.X[1], self.X[1] - self.six_width),(self.Y[1] - ((self.Y[1] - self.Y[0]) - self.six_length)/2,self.Y[1] - ((self.Y[1] - self.Y[0]) - self.six_length)/2), c='black')
        plt.plot((self.X[1] - self.six_width, self.X[1] - self.six_width),(self.Y[0] + ((self.Y[1] - self.Y[0]) - self.six_length)/2, self.Y[1] - ((self.Y[1] - self.Y[0]) - self.six_length)/2), c='black')
        #left pen spot and arc
        ax.add_patch(Arc((self.X[1] - self.pen_dist,(self.Y[1] + self.Y[0])/2), width = (self.Y[1] - self.Y[0]) * 0.23, height=(self.Y[1] - self.Y[0]) * 0.23, theta1=310, theta2=50, angle=0))
        plt.scatter(self.X[1] - self.pen_dist,(self.Y[1] + self.Y[0])/2, c='black', s =  15)



        plt.ylim(self.Y[0],self.Y[1])
        plt.xlim(self.X[0] - 0.1,self.X[1])

    def create_pitch_vert(self, ax):
        # create pitch borders and centerline
        plt.plot((self.Y[0],self.Y[0]), (self.X[0],self.X[1]), c='black')
        plt.plot((self.Y[0],self.Y[1]), (self.X[0], self.X[0]), c='black')
        plt.plot((self.Y[0],self.Y[1]), (self.X[1], self.X[1]), c='black')
        plt.plot((self.Y[1],self.Y[1]), (self.X[0], self.X[1]), c='black')
        plt.plot((self.Y[0] , self.Y[1]), ((self.X[0] + self.X[1]) / 2, (self.X[0] + self.X[1])/2), c='black')

        #create top pen box
        plt.plot((self.Y[0] + ((self.Y[1] - self.Y[0]) - self.pen_length )/2, self.Y[0] + ((self.Y[1] - self.Y[0]) - self.pen_length )/2),(self.X[1], self.X[1] - self.pen_width), c='black')
        plt.plot((self.Y[1] - ((self.Y[1] - self.Y[0]) - self.pen_length) /2, self.Y[1] - ((self.Y[1] - self.Y[0]) - self.pen_length) / 2), (self.X[1], self.X[1] - self.pen_width), c='black')
        plt.plot((self.Y[0] + ((self.Y[1] - self.Y[0]) - self.pen_length) /2, self.Y[1] - ((self.Y[1] - self.Y[0]) - self.pen_length) / 2), (self.X[1] - self.pen_width, self.X[1] - self.pen_width), c ='black')
        #Create top 6 yard box
        plt.plot((self.Y[0] + ((self.Y[1] - self.Y[0]) - self.six_length )/2, self.Y[0] + ((self.Y[1] - self.Y[0]) - self.six_length )/2),(self.X[1], self.X[1] - self.six_width), c='black')
        plt.plot((self.Y[1] - ((self.Y[1] - self.Y[0]) - self.six_length) /2, self.Y[1] - ((self.Y[1] - self.Y[0]) - self.six_length) / 2), (self.X[1], self.X[1] - self.six_width), c='black')
        plt.plot((self.Y[0] + ((self.Y[1] - self.Y[0]) - self.six_length) /2, self.Y[1] - ((self.Y[1] - self.Y[0]) - self.six_length) / 2), (self.X[1] - self.six_width, self.X[1] - self.six_width), c ='black')
        #Add pen spot and ard
        plt.scatter(((self.Y[1] + self.Y[0])/2),((self.X[1] - self.pen_dist)), c='black', s = 8)
        ax.add_artist(Arc(((self.Y[1] + self.Y[0])/2,(self.X[1] - self.pen_dist)),  height = (self.Y[1] - self.Y[0]) * 0.23, width=(self.Y[1] - self.Y[0]) * 0.23, theta1=310, theta2=50, angle=90 ))

        # create top pen box
        plt.plot((self.Y[0] + ((self.Y[1] - self.Y[0]) - self.pen_length) / 2, self.Y[0] + ((self.Y[1] - self.Y[0]) - self.pen_length) / 2), (self.X[0], self.X[0] + self.pen_width), c='black')
        plt.plot((self.Y[1] - ((self.Y[1] - self.Y[0]) - self.pen_length) / 2, self.Y[1] - ((self.Y[1] - self.Y[0]) - self.pen_length) / 2), (self.X[0], self.X[0] + self.pen_width), c='black')
        plt.plot((self.Y[0] + ((self.Y[1] - self.Y[0]) - self.pen_length) / 2, self.Y[1] - ((self.Y[1] - self.Y[0]) - self.pen_length) / 2),(self.X[0] + self.pen_width, self.X[0] + self.pen_width), c='black')
        # Create 6 yard box
        plt.plot((self.Y[0] + ((self.Y[1] - self.Y[0]) - self.six_length) / 2, self.Y[0] + ((self.Y[1] - self.Y[0]) - self.six_length) / 2), (self.X[0], self.X[0] + self.six_width), c='black')
        plt.plot((self.Y[1] - ((self.Y[1] - self.Y[0]) - self.six_length) / 2, self.Y[1] - ((self.Y[1] - self.Y[0]) - self.six_length) / 2), (self.X[0], self.X[0] + self.six_width), c='black')
        plt.plot((self.Y[0] + ((self.Y[1] - self.Y[0]) - self.six_length) / 2, self.Y[1] - ((self.Y[1] - self.Y[0]) - self.six_length) / 2), (self.X[0] + self.six_width, self.X[0] + self.six_width), c='black')
        #Add pen spot and arc
        plt.scatter(((self.Y[1] + self.Y[0])/2),((self.X[0] + self.pen_dist)), c='black', s = 8)
        ax.add_artist(Arc(((self.Y[1] + self.Y[0])/2,(self.X[0] + self.pen_dist)),  height = (self.Y[1] - self.Y[0]) * 0.23, width=(self.Y[1] - self.Y[0]) * 0.23, theta1=310, theta2=50, angle=270 ))


        #Add middle dot and circle
        plt.scatter(((self.Y[1] + self.Y[0] )/ 2), ((self.X[1] + self.X[0])/2), c='black', s=8)
        ax.add_artist(plt.Circle(((self.Y[1] + self.Y[0] )/ 2, (self.X[1] + self.X[0])/2), radius=(self.X[1] - self.X[0])*.1, color='black', fill=False))


        plt.xlim(self.Y[0],self.Y[1])
        plt.ylim(self.X[0] - 0.1,self.X[1])
    def show_pitch(self, ax):
        if self.vert:
            if self.half:
                self.create_pitch_vert(ax)
                plt.xlim((self.X[0] + self.X[1]) / 2 - 0.2, self.X[1])
            else:
                self.create_pitch_vert(ax)

        else:
            if self.half:
                self.create_pitch(ax)
                plt.xlim((self.X[0] + self.X[1]) / 2 -0.2, self.X[1])
            else:
                self.create_pitch(ax)


        if self.half:
            try:
                if self.shots_size == -1:
                    if self.shots_col == '':
                        for i in range(len(self.shots)):
                            plt.scatter(self.shots[i][1], self.shots[i][0], alpha=1, c='blue')
                    else:
                        for i in range(len(self.shots)):
                            plt.scatter(self.shots[i][1], self.shots[i][0], c=self.shots_col, alpha=1)
                else:
                    if self.shots_col == '':
                        for i in range(len(self.shots)):
                            plt.scatter(self.shots[i][1], self.shots[i][0], s=self.shots_size[i], alpha=1, c='blue')
                    else:
                        for i in range(len(self.shots)):
                            plt.scatter(self.shots[i][1], self.shots[i][0], c=self.shots_col, s=self.shots_size[i], alpha=1)
            except:
                pass

            try:

                if self.pass_col == '':
                   for i in range(len(self.passes)):
                        plt.arrow(self.passes[i][1], self.passes[i][0], self.passes[i][3] - self.passes[i][1],
                              self.passes[i][2] - self.passes[i][0], length_includes_head=True, head_width=3)
                else:
                    for i in range(len(self.passes)):
                        plt.arrow(self.passes[i][1], self.passes[i][0], self.passes[i][3] - self.passes[i][1],
                          self.passes[i][2] - self.passes[i][0], color=self.pass_col, length_includes_head=True,
                          head_width=3)

            except:
                pass

        else:

            try:
                if self.shots_size == -1:
                    if self.shots_col == '':
                        for i in range(len(self.shots)):
                            plt.scatter(self.shots[i][0], self.shots[i][1], alpha = 1, c='blue')
                    else:
                        for i in range(len(self.shots)):
                            plt.scatter(self.shots[i][0], self.shots[i][1], c= self.shots_col, alpha=1)
                else:
                    if self.shots_col == '':
                        for i in range(len(self.shots)):
                            plt.scatter(self.shots[i][0], self.shots[i][1], s = self.shots_size[i], alpha = 1, c='blue')
                    else:
                        for i in range(len(self.shots)):
                            plt.scatter(self.shots[i][0], self.shots[i][1], c= self.shots_col, s = self.shots_size[i], alpha = 1)
            except:
                pass
            try:

                if self.pass_col == '':
                    for i in range(len(self.passes)):
                        plt.arrow(self.passes[i][0], self.passes[i][1], self.passes[i][2] - self.passes[i][0],
                                  self.passes[i][3]- self.passes[i][1], length_includes_head=True, head_width=3)
                else:
                    for i in range(len(self.passes)):
                        plt.arrow(self.passes[i][0], self.passes[i][1], self.passes[i][2] - self.passes[i][0],
                                  self.passes[i][3] - self.passes[i][1], color = self.pass_col, length_includes_head=True, head_width=3)

            except:
                pass

        ax.set_facecolor(self.pitch_col)


        if self.pass_network_:
            self.plot_pn()

        if self.grid:
            dist = (self.X[1] - self.X[0]) / 10
            Xs = np.linspace(self.X[0], self.X[1], 10, endpoint=False)
            Ys = np.linspace(self.Y[0], self.Y[1], 10, endpoint=False)

            for x in Xs:
                plt.plot([x,x], [self.Y[0],self.Y[1]], c='black', alpha = 0.6)

            for y in Ys:
                plt.plot([self.X[0],self.X[1]],[y,y], c = 'black', alpha=0.6)



    def dim_(self):
        return self.X, self.Y

    def shots_(self):
        return self.shots

    def passes_(self):
        return self.passes


