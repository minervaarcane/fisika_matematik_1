# %% [markdown]
# # TUGAS ICT FISMAT 1
# ## NOMOR 2 B
# ### Nama: Chaidar Aria Bayu Pratama
# ### NIM: 21030224052
# ### Kelas: Fisika 2021 E

# %% [markdown]
# 2
# $$x\sqrt{1+x}$$

# %%
import numpy as np
import matplotlib.pyplot as plt
import sympy as smp
import scipy as scp
from numpy import *
from matplotlib import *
from sympy import *
from mpmath import *
from scipy import *
plt.style.use('classic')

n, x = smp.symbols('n x')


# %%
x = np.linspace(-np.pi, np.pi, 200)
y = np.zeros(len(x))
labels = ['S1', 'S2', 'S3', 'S4']
plt.figure()
for n, label in zip(range(4), labels):
    y += x*np.sqrt(1+x)
    plt.plot(x, y, label=label)
plt.plot(x, np.sqrt(1+x), 'k', label='Analytic')
plt.grid()
plt.title('Grafik deret maclaurin')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right', prop={'size': 10})
plt.show()


# %%
