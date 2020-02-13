# sports_plotter
sports_plotter is a package for making plotting in hockey and soccer easier.

# Usage
import
```
from sports_plotter.hockey import Rink
from sports_plotter.soccer import Pitch
```

initialize a Rink object and then show it. Every rink uses NHL API co-ordinates as default so (0,0) is center ice and the nets are at (-89,0) and (89,0).
```
fig, ax = plt.subplots(1,1)
rink = Rink()
rink.plot_rink(ax)
```


initialize a Pitch object and then show it. Every Pitch uses statsbomb dimensions as the default which make (0,0) the bottom left corner and (120,80) the top right corner.
```
fig, ax = plt.subplots(1,1)
pitch = Pitch()
pitch.show_pitch()
```

both a Rink or Pitch can be put as vertical and/or just half. In cases where it is half the right/top half is shown.
```
rink = Rink(vert=True)
rink = Rink(half=True)
rink = Rink(half=True, vert=True)
```

initialize a Rink object using custom dimensions. pass x as an iterable of two elements using the left boundary followed by the right boundary only and y as an iterable using two elements of the bottom boundary followed by the top boundary.
```
rink = Rink(x=[0,200], y=[0,80])
```

initialize a Pitch using custom dimensions. x and y are the same as a Rink object.
```
pitch = Pitch(custom_dim = {'x':[-80,80],
                            'y':[-40,40],
                            'pen_width':18,
                            'pen_length':44,
                            'six_yard_width':6,
                            'six_yard_length':20,
                            'pen_spot_distance':12}
```


create a Rink object, plot two shots on the ice at (50,0) and (-50,10) coloured red and shaped as a hexagon.
```
fig, ax = plt.subplots(1,1)
rnk = Rink()
rnk.add_shots([[50,0],[-50,10]], shape='H', color='red')
rnk.plot_rink(ax)
plt.show()
```

create a soccer field object (Pitch) and plot passes on it. The first pass will be from (6,40) to (20,5) and the arrow will be blue.
```
fig, ax = plt.subplots(1,1)
pitch = Pitch()
pitch.add_passes([[6,40,20,5],[-110,-20,-50,60],[-80,-50,80,-40]],col='blue')
pitch.show_pitch(ax)
plt.show()

```


create a Pitch object call the plot function then after make a contour plot and the contour plot will appear over the soccer field.
```
fig, ax = plt.subplots(1,1)
pitch = Pitch( col='green')
pitch.show_pitch(ax)
mean, cov = [60, 40], [(80, 0), (0, 80)]
x, y = np.random.multivariate_normal(mean, cov, size=50).T
sns.kdeplot(x,y, zorder=1000, shade_lowest=False)
plt.show()
```
create a blank pitch with a 20x10 grid overlay
```
fig, ax = plt.subplots(1,1)
pitch = Pitch(grid = [20,10])
pitch.show_pitch(ax)
plt.show()
```
plot a passing network over a soccer pitch
```
fig, ax = plt.subplots(1,1)
pitch = Pitch()
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
```

