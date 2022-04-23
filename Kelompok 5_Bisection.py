import scipy.optimize as opt
y = lambda x:4*(x**3)+7*x+3
x = opt.bisect(y,-0.4,-0.3,xtol=0.005)
print(x)
