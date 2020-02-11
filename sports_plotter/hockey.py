import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc
import numpy as np

class Rink:

    def __init__(self, x = [-100,100], y = [-42.5,42.5], half=False, vert=False):
        self.X = x
        self.Y = y
        self.half = half
        self.vert = vert

    def add_shots(self, xy, color = 'black', shape = 'circle', size = 50):
        self.shots_xy = np.array(xy)
        self.shots_color1 = color
        self.shot_shape1 = shape
        self.shot_size1 = size


    def make_arena_full(self, ax):

        #plot rink boundaries
        ax.plot((-87,87),(-42.5,-42.5), c="black")
        ax.plot((-87,87),(42.5,42.5), c="black")
        ax.plot((-100,-100),(-20.5, 20.5), c='black')
        ax.plot((100,100), (-20.5,20.5), c='black')
        ax.add_patch(Arc((-87,-20.5),width=26, height=44, angle=0, theta1=180, theta2=270, linewidth=1.5))
        ax.add_patch(Arc((-87, 20.5), width=26, height=44, angle=0, theta1=90, theta2=180, linewidth=1.5))
        ax.add_patch(Arc((87, 20.5), width=26, height=44, angle=0, theta1=0, theta2=90 , linewidth=1.5))
        ax.add_patch(Arc((87, -20.5), width=26, height=44, angle=180, theta1=90, theta2=180, linewidth=1.5))

        #red lines and center lines
        ax.plot((89,89), (-42,42), c="red")
        ax.plot((-89, -89), (-42, 42), c="red")
        ax.plot((0, 0), (-42.5, 42.5), c="red")

        #blue lines
        plt.plot((-25,-25),(-42.5,42.5), c='blue')
        plt.plot((25, 25), (-42.5, 42.5), c='blue')

        #faceoff circles
        ax.add_patch(Circle((-69,22), radius=15, color='red', fill=False))
        ax.add_patch(Circle((69, 22), radius=15, color='red', fill=False))
        ax.add_patch(Circle((-69, -22), radius=15, color='red', fill=False))
        ax.add_patch(Circle((69, -22), radius=15, color='red', fill=False))

        #plot faceoff dots
        ax.scatter((-69,69,-69,69),(22,-22,-22,22), c='red', s=12)

        #plot hashmarks
        ax.plot((-67.5,-67.5),(36.9, 38.9), c='red')
        ax.plot((-70.5, -70.5), (36.9, 38.9), c='red')
        ax.plot((67.5,67.5),(36.9, 38.9), c='red')
        ax.plot((70.5, 70.5), (36.9, 38.9), c='red')
        ax.plot((-67.5,-67.5),(7, 5), c='red')
        ax.plot((-70.5, -70.5), (7, 5), c='red')
        ax.plot((67.5,67.5),(7, 5), c='red')
        ax.plot((70.5, 70.5), (7, 5), c='red')

        ax.plot((-67.5,-67.5),(-36.9, -38.9), c='red')
        ax.plot((-70.5, -70.5), (-36.9, -38.9), c='red')
        ax.plot((67.5,67.5),(-36.9, -38.9), c='red')
        ax.plot((70.5, 70.5), (-36.9, -38.9), c='red')
        ax.plot((-67.5,-67.5),(-7, -5), c='red')
        ax.plot((-70.5, -70.5), (-7, -5), c='red')
        ax.plot((67.5,67.5),(-7, -5), c='red')
        ax.plot((70.5, 70.5), (-7, -5), c='red')


        #centre ice circle and faceoff dot
        ax.scatter((0),(0), c='blue', zorder=100)
        ax.add_patch(Circle((0,0), radius=15, color='blue', fill=False))

        #offside dots
        ax.scatter((-20, 20, -20, 20), (22, -22, -22, 22), c='red', s=12)

        #draw creases
        ax.add_patch(Arc((-89,0),height=8, width=8, angle=180, theta1=90, theta2=270, color='red',zorder=3))
        ax.add_patch(Circle((-89, 0), radius=4, color='blue', fill=True, zorder=1))
        ax.add_patch(Rectangle([-94,-5], width=5, height=10, color='white'))


        ax.add_patch(Arc((89,0),height=8, width=8, theta1=90, theta2=270, color='red',zorder=3))
        ax.add_patch(Circle((89, 0), radius=4, color='blue', fill=True, zorder=1))
        ax.add_patch(Rectangle([89,-5], width=6, height=10, color='white'))

        #draw nets
        ax.add_patch(Rectangle((89,-3), height=6, width=4, color='grey'))
        ax.add_patch(Rectangle((-93, -3), height=6, width=4, color='grey'))


    def make_arena_half(self, ax):

        #plot rink boundaries
        ax.plot((0,87),(-42.5,-42.5), c="black")
        ax.plot((0,87),(42.5,42.5), c="black")
        ax.plot((100,100),(-20.5, 20.5), c='black')

        ax.add_patch(Arc((87, 20.5), width=26, height=44, angle=0, theta1=0, theta2=90 , linewidth=1.5))
        ax.add_patch(Arc((87, -20.5), width=26, height=44, angle=180, theta1=90, theta2=180, linewidth=1.5))

        #red lines and center lines
        ax.plot((89,89), (-42,42), c="red")
        ax.plot((0, 0), (-42.5, 42.5), c="red")

        #blue lines
        plt.plot((25, 25), (-42.5, 42.5), c='blue')

        #faceoff circles
        ax.add_patch(Circle((69, 22), radius=15, color='red', fill=False))
        ax.add_patch(Circle((69, -22), radius=15, color='red', fill=False))

        #plot faceoff dots
        ax.scatter((69,69),(22,-22), c='red', s=12)

        #plot hashmarks
        ax.plot((67.5,67.5),(36.9, 38.9), c='red')
        ax.plot((70.5, 70.5), (36.9, 38.9), c='red')
        ax.plot((67.5,67.5),(7, 5), c='red')
        ax.plot((70.5, 70.5), (7, 5), c='red')

        ax.plot((67.5,67.5),(-36.9, -38.9), c='red')
        ax.plot((70.5, 70.5), (-36.9, -38.9), c='red')
        ax.plot((67.5,67.5),(-7, -5), c='red')
        ax.plot((70.5, 70.5), (-7, -5), c='red')


        #centre ice circle and faceoff dot
        ax.scatter((0),(0), c='blue', zorder=100)
        ax.add_patch(Arc((0,0), height=30, width=30, angle=180, theta1=90, theta2=270, color='blue', fill=False))

        #offside dots
        ax.scatter((20, 20), (22, -22), c='red', s=12)

        #draw creases
        ax.add_patch(Arc((89,0),height=8, width=8, theta1=90, theta2=270, color='red',zorder=3))
        ax.add_patch(Circle((89, 0), radius=4, color='blue', fill=True, zorder=1))
        ax.add_patch(Rectangle([89,-5], width=6, height=10, color='white'))

        #draw nets
        ax.add_patch(Rectangle((89,-3), height=6, width=4, color='grey'))
        ax.set_xlim((-5,100))


    def make_arena_half_vert(self, ax):

        #plot rink boundaries
        ax.plot((-42.5,-42.5),(0,87), c="black")
        ax.plot((42.5,42.5),(0,87), c="black")
        ax.plot((-20.5, 20.5),(100,100), c='black')

        ax.add_patch(Arc((20.5, 87, 20.5), width=44, height=26, angle=0, theta1=0, theta2=90 , linewidth=1.5))
        ax.add_patch(Arc(( -20.5,87), width=44, height=26, angle=0, theta1=90, theta2=180, linewidth=1.5))

        #red lines and center lines
        ax.plot( (-42,42),(89,89), c="red")
        ax.plot((-42.5, 42.5),(0,0), c="red")

        #blue lines
        plt.plot((-42.5, 42.5),(25, 25), c='blue')

        #faceoff circles
        ax.add_patch(Circle(( 22,69), radius=15, color='red', fill=False))
        ax.add_patch(Circle((-22,69), radius=15, color='red', fill=False))

        #plot faceoff dots
        ax.scatter((22,-22),(69,69), c='red', s=12)

        #plot hashmarks
        ax.plot((36.9, 38.9),(67.5,67.5), c='red')
        ax.plot( (36.9, 38.9),(70.5, 70.5), c='red')
        ax.plot((7, 5), (67.5,67.5),c='red')
        ax.plot( (7, 5), (70.5, 70.5),c='red')

        ax.plot((-36.9, -38.9), (67.5,67.5),c='red')
        ax.plot( (-36.9, -38.9), (70.5, 70.5),c='red')
        ax.plot((-7, -5), (67.5,67.5),c='red')
        ax.plot( (-7, -5), (70.5, 70.5), c='red')


        #centre ice circle and faceoff dot
        ax.scatter((0),(0), c='blue', zorder=100)
        ax.add_patch(Arc((0,0), height=30, width=30, angle=180, theta1=180, theta2=360, color='blue', fill=False))

        #offside dots
        ax.scatter((22, -22), (20, 20), c='red', s=12)

        #draw creases
        ax.add_patch(Arc((0,89),height=8, width=8, theta1=180, theta2=360, color='red',zorder=3))
        ax.add_patch(Circle((0,89), radius=4, color='blue', fill=True, zorder=1))
        ax.add_patch(Rectangle([-5,89], width=10, height=6, color='white'))

        #draw nets
        ax.add_patch(Rectangle((-3,89), height=4, width=6, color='grey'))
        ax.set_ylim((-5,105))
    def plot_rink(self, ax):


        if self.half:
            if self.vert:
                self.make_arena_half_vert(ax)
            else:
                self.make_arena_half(ax)
        else:
            self.make_arena_full(ax)
        try:
            ax.scatter(self.shots_xy[:,0], self.shots_xy[:,1], c = self.shots_color1, marker = self.shot_shape1, s = self.shot_size1)

        except:
            pass

