# Actual solution

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint 

ya=lambda x:(2*np.exp)-x-1

y0=1.0
xs=np.arange(0,0.12,0.02)
us=odeint(ya,y0,xs)
ys=us[:,0]
print(us)
plt.plot(xs,ys,'ro',label="numeric solution")
plt.plot(xs,ya(xs),label="actual solution")
plt.xlabel('x values')
plt.ylabel('y values')
plt.legend(loc='lower right', prop={'size':10})
plt.show()
