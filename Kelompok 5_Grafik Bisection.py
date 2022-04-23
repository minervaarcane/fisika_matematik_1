import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-0.5,0,0.005)
y = lambda x:4*(x**3)+7*x+3
plt.plot(x,y(x))
plt.grid()
plt.show()
