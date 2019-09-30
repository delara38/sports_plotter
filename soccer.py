import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Arc
class Pitch:

    def __init__(self, x,y, col="white", custom_dim = None):
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

        self.pitch_col = col
    def add_passes(self, passes, col = ''):
        self.passes = passes
        self.pass_col = col
    def add_shots(self, shots, col= '', size = -1):
        self.shots = shots
        self.shots_col = col
        self.shots_size = size



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

    def show_pitch(self, ax):
        self.create_pitch(ax)
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

fig, ax = plt.subplots()
pc = Pitch((0,120),(0,80), col='green')
pc.show_pitch(ax)
plt.show()

