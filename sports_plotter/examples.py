from sports_plotter.soccer import Pitch
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sports_plotter.hockey import Rink
import pandas as pd

#Create a plot of a full hockey rink with two red hexagons at (50,0) and (-50,10) representing shots
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
rnk = Rink()
rnk.add_shots([[50, 0],[-50, 10]], shape='H', color=['yellow','red'], size=[50,100])
rnk.plot_rink(ax)
plt.show()
'''



#Create a plot of a soccer pitch and plot a couple passes and makes them blue
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
#create the pitch object and say it will come with a grid that is 20x20
pitch = Pitch(grid=[20,20])


#create array of pass co-ordinates for pass network in format [x1, y1, x2,y2]
#where 1 signifies where the pass was made from and 2 is where the pass ended up
pass_network = [[20,20,100,70],
                [60,20, 50 ,80],
                [20,20,20,60],
                [40, 60, 20, 20]]
#array of the id for the passer on each pass in pass_network array
passer_ids =  [2,1,2,4]
#array of reciever ids for each reciever in pass_network array
reciever_ids = [3,3,4,2]
#send data to pass_network function
pitch.pass_network(pass_network,passer_ids,reciever_ids)
pitch.show_pitch(ax)
plt.show()



#create a plot of a soccer pitch and plot a contour graph over
fig = plt.Figure()
ax = fig.add_subplot(1,1,1)
pitch = Pitch([-120,120],[-80,80], col='green')
pitch.show_pitch(ax)
mean, cov = [60, 40], [(80, 0), (0, 80)]
x, y = np.random.multivariate_normal(mean, cov, size=50).T
sns.kdeplot(x,y, zorder=1000, shade_lowest=False)
plt.show()

'''