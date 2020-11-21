from vispy.plot import Fig
fig = Fig()

#And then PlotWidget instances are automatically created by accessing the fig instance:
ax_left = fig[0, 0]
ax_right = fig[0, 1]

#Then plots are accomplished via methods of the PlotWidget instances:

import numpy as np
data = np.random.randn(1, 3)
ax_left.plot(data)
ax_right.histogram(data[0])
