# %% [markdown]
# # TUGAS ICT FISMAT 1
# ## NOMOR 2 A
# ### Nama: Chaidar Aria Bayu Pratama
# ### NIM: 21030224052
# ### Kelas: Fisika 2021 E

# %% [markdown]
# 2. $$\sum_{n=1}^{\infty}\frac{n}{3^n}$$

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
smp.Sum(n / (3**n), (n, 1, smp.oo)).doit()

# %%
smp.Sum(n / (3**n), (n, 1, smp.oo)).n()

# %%
smp.Sum(n / (3**n), (n, 1, smp.oo)).is_convergent()
