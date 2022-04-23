# Second Order Differential

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(x,y):
    return(y[1],-5*y[1]+6*y[0])

#Actual solution
ya=lambda x: np.exp(2*x)

y0=[1]
xs=np.arange(0,3.32,0.2)
us=odeint(f,y0,xs)
ys=us[:,0]
print (us)
plt.plot(xs,ys,'ro',label="numeric solution")
plt.plot(xs,ya(xs),label="actual solution")
plt.xlabel('x values')
plt.ylabel('y values')
plt.legend(loc='lower right', prop={'size':10})
plt.show()
