import matplotlib.animation as animation
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np

# Time variables
t0 = 0  # [hrs]
t_end = 2  # [hrs]
dt = 0.005  # [hrs]

# Creating time array
# arange -> creates array with difference in each subsequent element equals to dt
# arange -> (starting point, ending point {value not included}, time difference)
# That is why t_end+dt

t = np.arange(t0, t_end + dt, dt)
print(t)

# Creating x variable
x = 800 * t
print(x)

# Creating y variable
# ones -> create a array with all values as 1 for the given length
# mathematical way to do this -> y = np.ones((init (tend/dt + 1) )

altitude = 2
y = np.ones(len(t)) * altitude
print(y)

# -----------------------------Animation---------------------------------

# Frame count must be equal to number of points or frame you are going to plot
frame_count = len(t)


# update function -> will draw the frames

def update_plot(num):
    plane_trajectory.set_data(x[0:num], y[0:num])
    return plane_trajectory,


# Setting grid Spcae and Creating the figure
# Divides canvas into 2 rows and 2 columns
gs = gridspec.GridSpec(2, 2)
fig = plt.figure(figsize=(16, 9), dpi=120, facecolor=(0.8, 0.8, 0.8))

# Subplot 1
ax0 = fig.add_subplot(gs[0:], facecolor=(0.9, 0.9, 0.9))
plane_trajectory, = ax0.plot([], [], 'g', linewidth=2)
plt.xlim(x[0], x[-1])
plt.ylim(0, y[0] + 1)


# function that performs animation in python
# takes -> fig : figure that animation will be drawn on
#          update_plot : function that tell what to draw and where
#          frames : frame count
#          interval : time interval between 2 frames, here 20 is 20 ms
#          repeat : tell animation to loop after completion
#          blit : optimization technique. Only draws part of frame that need to redrawn each frame
plane_ani = animation.FuncAnimation(fig, update_plot, frames=frame_count, interval=20, repeat=True, blit=True)
plt.show()
