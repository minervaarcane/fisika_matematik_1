# TUGAS FISIKA MATEMATIK 1 
# ICT TURUNAN PARSIAL

# Nama  : Riana Oktafianti
# NIM   : 21030224040
# Kelas : Fisika 2021 E

# Penyelesaian soal no 10 dengan python

import sympy as smp
from sympy import*

x,y = smp.symbols('x y')
f = ((x**4)+(y**3)-(x**2)*y)

# Differentiating partially w.r.t x
derivative_f = f.diff(x,y)
print(derivative_f)




