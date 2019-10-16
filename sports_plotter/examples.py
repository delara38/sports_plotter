from sports_plotter.soccer import Pitch
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

pitch = Pitch()
pitch.create_pitch(ax)

plt.ylim(pitch.ylim)
plt.xlim(pitch.xlim)
plt.show()
