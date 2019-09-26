import hockey
from hockey import Rink
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
rnk = Rink()
rnk.add_shots([[50,0],[-50,10]], shape=['H','H'], size=[50,75], color=['red','blue'])
rnk.plot_rink(ax)
plt.show()