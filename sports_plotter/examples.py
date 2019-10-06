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
rnk.plot_rink(ax)
rnk.add_shots([[50,0],[-50,10]], shape='H', color='red')
plt.show()

#Create a plot of a soccer pitch and plot a couple passes and makes them blue
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
pitch = Pitch([-120,120],[-80,80])
pitch.add_passes([[6,40,20,5],[-110,-20,-50,60],[-80,-50,80,-40]],col='blue')
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

