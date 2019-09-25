import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc, ConnectionPatch
class Pitch:

    def __init__(self, x,y, col="white"):
        self.X = x
        self.Y = y
        self.pitch_col = col
    def add_passes(self, passes, col = ''):
        self.passes = passes
        self.pass_col = col
    def add_shots(self, shots, col= '', size = -1):
        self.shots = shots
        self.shots_col = col
        self.shots_size = size


    def show_pitch(self, ax):
        # size of the pitch is 120, 80
        # Create figure

        # Pitch Outline & Centre Line
        plt.plot([self.X[0], self.X[0]], [self.Y[0], self.Y[1]], color="black")
        plt.plot([self.X[0], self.X[1]], [self.Y[1], self.Y[1]], color="black")
        plt.plot([self.X[1], self.X[1]], [self.Y[1], self.Y[0]], color="black")
        plt.plot([self.X[1], self.X[0]], [self.Y[0], self.Y[0]], color="black")
        plt.plot([(self.X[1] + self.X[0])/2, (self.X[1] + self.X[0])/2], [self.Y[0], self.Y[1]], color="black")

        # Left Penalty Area
        plt.plot([self.X[0] + (self.X[1] - self.X[0]) * 0.12, self.X[0] + (self.X[1] - self.X[0]) * 0.12], [self.Y[0] + (self.Y[1] - self.Y[0]) * 0.72,self.Y[0] + (self.Y[1] - self.Y[0]) * 0.27  ], color="black")
        plt.plot([self.X[0], self.X[0] + (self.X[1] - self.X[0]) * 0.12], [self.Y[0] + (self.Y[1] - self.Y[0]) * 0.72 , self.Y[0] + (self.Y[1] - self.Y[0]) * 0.72], color="black")
        plt.plot([self.X[0], self.X[0] + (self.X[1] - self.X[0]) * 0.12], [self.Y[0] + (self.Y[1] - self.Y[0]) * 0.27, self.Y[0] + (self.Y[1] - self.Y[0]) * 0.27], color="black")

        # Right Penalty Area
        plt.plot([self.X[1], self.X[1] - (self.X[1] - self.X[0])* 0.12], [self.Y[0] + (self.Y[1] - self.Y[0]) * 0.72,self.Y[0] + (self.Y[1] - self.Y[0]) * 0.72], color="black")
        plt.plot([self.X[1] - (self.X[1] - self.X[0])* 0.12, self.X[1] - (self.X[1] - self.X[0]) * 0.12], [self.Y[0] + (self.Y[1] - self.Y[0]) * 0.72, self.Y[0] + (self.Y[1] - self.Y[0]) * 0.27], color="black")
        plt.plot([self.X[1], self.X[1] - (self.X[1] - self.X[0])* 0.12], [self.Y[0] + (self.Y[1] - self.Y[0]) * 0.27, self.Y[0] + (self.Y[1] - self.Y[0]) * 0.27], color="black")

        # Left 6-yard Box
        plt.plot([self.X[0], self.X[0] + (self.X[1] - self.X[0]) * 0.04], [self.Y[0] + (self.Y[1] - self.Y[0]) * .6, self.Y[0] + (self.Y[1] - self.Y[0]) * .6], color="black")
        plt.plot([self.X[0] + (self.X[1] - self.X[0]) * 0.04, self.X[0] + (self.X[1] - self.X[0]) * 0.04], [self.Y[0] + (self.Y[1] - self.Y[0]) * .6, self.Y[0] + (self.Y[1] - self.Y[0]) * .4], color="black")
        plt.plot([self.X[0], self.X[0] + (self.X[1] - self.X[0]) * 0.04], [self.Y[0] + (self.Y[1] - self.Y[0]) * .4, self.Y[0] + (self.Y[1] - self.Y[0]) * .4], color="black")

        # Right 6-yard Box
        plt.plot([self.X[1], self.X[0] + (self.X[1] - self.X[0]) * 0.96], [self.Y[0] + (self.Y[1] - self.Y[0]) * .6, self.Y[0] + (self.Y[1] - self.Y[0]) * .6], color="black")
        plt.plot([self.X[0] + (self.X[1] - self.X[0]) * 0.96, self.X[0] + (self.X[1] - self.X[0]) * 0.96], [self.Y[0] + (self.Y[1] - self.Y[0]) * .6, self.Y[0] + (self.Y[1] - self.Y[0]) * .4], color="black")
        plt.plot([self.X[1], self.X[0] + (self.X[1] - self.X[0]) * 0.96], [self.Y[0] + (self.Y[1] - self.Y[0]) * .4, self.Y[0] + (self.Y[1] - self.Y[0]) * .4], color="black")

        # Prepare Circles
        centreCircle = plt.Circle(((self.X[0] + self.X[1]) / 2, (self.Y[0] + self.Y[1]) / 2), (self.Y[1] - self.Y[0]) * .101, color="black", fill=False)
        centreSpot = plt.Circle(((self.X[0] + self.X[1]) / 2, (self.Y[0] + self.Y[1]) / 2), (self.Y[1] - self.Y[0]) * 0.0089, color="black")
        leftPenSpot = plt.Circle((self.X[0] + (self.X[1] - self.X[0]) * 0.0808, (self.Y[0] + self.Y[1]) / 2),  (self.Y[1] - self.Y[0]) * 0.0089, color="black")
        rightPenSpot = plt.Circle((self.X[1] - (self.X[1] - self.X[0]) * 0.0808, (self.Y[0] + self.Y[1]) / 2),  (self.Y[1] - self.Y[0]) * 0.0089, color="black")

        # Draw Circles
        ax.add_patch(centreCircle)
        ax.add_patch(centreSpot)
        ax.add_patch(leftPenSpot)
        ax.add_patch(rightPenSpot)

        # Prepare Arcs
        # arguments for arc
        # x, y coordinate of centerpoint of arc
        # width, height as arc might not be circle, but oval
        # angle: degree of rotation of the shape, anti-clockwise
        # theta1, theta2, start and end location of arc in degree
        leftArc = Arc((self.X[0] + (self.X[1] - self.X[0]) * 0.0808, (self.Y[0] + self.Y[1]) / 2), height=(self.X[1] - self.X[0]) * 0.135, width=(self.X[1] - self.X[0]) * 0.135, angle=0, theta1=310, theta2=50, color="black")
        rightArc = Arc((self.X[1] - (self.X[1] - self.X[0]) * 0.0808, (self.Y[0] + self.Y[1]) / 2), height=(self.X[1] - self.X[0]) * 0.135, width=(self.X[1] - self.X[0]) * 0.135, angle=0, theta1=130, theta2=230, color="black")

        # Draw Arcs
        ax.add_patch(leftArc)
        ax.add_patch(rightArc)

        if self.pass_size == -1:
            if self.pass_col == '':
                for i in range(len(self.passes)):
                    plt.scatter(self.passes[i][0], self.passes[i][1], alpha = 1)
            else:
                for i in range(len(self.passes)):
                    plt.scatter(self.passes[i][0], self.passes[i][1], c= self.pass_col, alpha=1)
        else:
            if self.pass_col == '':
                for i in range(len(self.passes)):
                    plt.scatter(self.passes[i][0], self.passes[i][1], s = self.pass_size[i], alpha = 1)
            else:
                for i in range(len(self.passes)):
                    plt.scatter(self.passes[i][0], self.passes[i][1], c= self.pass_col, s = self.pass_size[i], alpha = 1)

        ax.set_facecolor(self.pitch_col)
        plt.show()

    def create_pitch(self, ax):
        # size of the pitch is 120, 80
        # Create figure

        # Pitch Outline & Centre Line
        plt.plot([self.X[0], self.X[0]], [self.Y[0], self.Y[1]], color="black")
        plt.plot([self.X[0], self.X[1]], [self.Y[1], self.Y[1]], color="black")
        plt.plot([self.X[1], self.X[1]], [self.Y[1], self.Y[0]], color="black")
        plt.plot([self.X[1], self.X[0]], [self.Y[0], self.Y[0]], color="black")
        plt.plot([(self.X[1] + self.X[0])/2, (self.X[1] + self.X[0])/2], [self.Y[0], self.Y[1]], color="black")

        # Left Penalty Area
        plt.plot([self.X[0] + (self.X[1] - self.X[0]) * 0.12, self.X[0] + (self.X[1] - self.X[0]) * 0.12], [self.Y[0] + (self.Y[1] - self.Y[0]) * 0.72,self.Y[0] + (self.Y[1] - self.Y[0]) * 0.27  ], color="black")
        plt.plot([self.X[0], self.X[0] + (self.X[1] - self.X[0]) * 0.12], [self.Y[0] + (self.Y[1] - self.Y[0]) * 0.72 , self.Y[0] + (self.Y[1] - self.Y[0]) * 0.72], color="black")
        plt.plot([self.X[0], self.X[0] + (self.X[1] - self.X[0]) * 0.12], [self.Y[0] + (self.Y[1] - self.Y[0]) * 0.27, self.Y[0] + (self.Y[1] - self.Y[0]) * 0.27], color="black")

        # Right Penalty Area
        plt.plot([self.X[1], self.X[1] - (self.X[1] - self.X[0])* 0.12], [self.Y[0] + (self.Y[1] - self.Y[0]) * 0.72,self.Y[0] + (self.Y[1] - self.Y[0]) * 0.72], color="black")
        plt.plot([self.X[1] - (self.X[1] - self.X[0])* 0.12, self.X[1] - (self.X[1] - self.X[0]) * 0.12], [self.Y[0] + (self.Y[1] - self.Y[0]) * 0.72, self.Y[0] + (self.Y[1] - self.Y[0]) * 0.27], color="black")
        plt.plot([self.X[1], self.X[1] - (self.X[1] - self.X[0])* 0.12], [self.Y[0] + (self.Y[1] - self.Y[0]) * 0.27, self.Y[0] + (self.Y[1] - self.Y[0]) * 0.27], color="black")

        # Left 6-yard Box
        plt.plot([self.X[0], self.X[0] + (self.X[1] - self.X[0]) * 0.04], [self.Y[0] + (self.Y[1] - self.Y[0]) * .6, self.Y[0] + (self.Y[1] - self.Y[0]) * .6], color="black")
        plt.plot([self.X[0] + (self.X[1] - self.X[0]) * 0.04, self.X[0] + (self.X[1] - self.X[0]) * 0.04], [self.Y[0] + (self.Y[1] - self.Y[0]) * .6, self.Y[0] + (self.Y[1] - self.Y[0]) * .4], color="black")
        plt.plot([self.X[0], self.X[0] + (self.X[1] - self.X[0]) * 0.04], [self.Y[0] + (self.Y[1] - self.Y[0]) * .4, self.Y[0] + (self.Y[1] - self.Y[0]) * .4], color="black")

        # Right 6-yard Box
        plt.plot([self.X[1], self.X[0] + (self.X[1] - self.X[0]) * 0.96], [self.Y[0] + (self.Y[1] - self.Y[0]) * .6, self.Y[0] + (self.Y[1] - self.Y[0]) * .6], color="black")
        plt.plot([self.X[0] + (self.X[1] - self.X[0]) * 0.96, self.X[0] + (self.X[1] - self.X[0]) * 0.96], [self.Y[0] + (self.Y[1] - self.Y[0]) * .6, self.Y[0] + (self.Y[1] - self.Y[0]) * .4], color="black")
        plt.plot([self.X[1], self.X[0] + (self.X[1] - self.X[0]) * 0.96], [self.Y[0] + (self.Y[1] - self.Y[0]) * .4, self.Y[0] + (self.Y[1] - self.Y[0]) * .4], color="black")

        # Prepare Circles
        centreCircle = plt.Circle(((self.X[0] + self.X[1]) / 2, (self.Y[0] + self.Y[1]) / 2), (self.Y[1] - self.Y[0]) * .101, color="black", fill=False)
        centreSpot = plt.Circle(((self.X[0] + self.X[1]) / 2, (self.Y[0] + self.Y[1]) / 2), (self.Y[1] - self.Y[0]) * 0.0089, color="black")
        leftPenSpot = plt.Circle((self.X[0] + (self.X[1] - self.X[0]) * 0.0808, (self.Y[0] + self.Y[1]) / 2),  (self.Y[1] - self.Y[0]) * 0.0089, color="black")
        rightPenSpot = plt.Circle((self.X[1] - (self.X[1] - self.X[0]) * 0.0808, (self.Y[0] + self.Y[1]) / 2),  (self.Y[1] - self.Y[0]) * 0.0089, color="black")

        # Draw Circles
        ax.add_patch(centreCircle)
        ax.add_patch(centreSpot)
        ax.add_patch(leftPenSpot)
        ax.add_patch(rightPenSpot)

        # Prepare Arcs
        # arguments for arc
        # x, y coordinate of centerpoint of arc
        # width, height as arc might not be circle, but oval
        # angle: degree of rotation of the shape, anti-clockwise
        # theta1, theta2, start and end location of arc in degree
        leftArc = Arc((self.X[0] + (self.X[1] - self.X[0]) * 0.0808, (self.Y[0] + self.Y[1]) / 2), height=(self.X[1] - self.X[0]) * 0.135, width=(self.X[1] - self.X[0]) * 0.135, angle=0, theta1=310, theta2=50, color="black")
        rightArc = Arc((self.X[1] - (self.X[1] - self.X[0]) * 0.0808, (self.Y[0] + self.Y[1]) / 2), height=(self.X[1] - self.X[0]) * 0.135, width=(self.X[1] - self.X[0]) * 0.135, angle=0, theta1=130, theta2=230, color="black")

        # Draw Arcs
        ax.add_patch(leftArc)
        ax.add_patch(rightArc)
        try:
            if self.shots_size == -1:
                if self.shots_col == '':
                    for i in range(len(self.shots)):
                        plt.scatter(self.shots[i][0], self.shots[i][1], alpha = 1)
                else:
                    for i in range(len(self.shots)):
                        plt.scatter(self.shots[i][0], self.shots[i][1], c= self.shots_col, alpha=1)
            else:
                if self.shots_col == '':
                    for i in range(len(self.shots)):
                        plt.scatter(self.shots[i][0], self.shots[i][1], s = self.shots_size[i], alpha = 1)
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

fig=plt.figure() #set up the figures
fig.set_size_inches(7, 5)
ax=fig.add_subplot(1,1,1)
pc = Pitch((-120,120),(-80,80),col='green')
pc.add_shots([[108,30]], col="blue")
pc.add_passes([[20,20,108,30],[0,0,20,20]], col = "blue")
pc.create_pitch(ax)
plt.show()