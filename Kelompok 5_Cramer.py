# Fisika Komputasi
# Sistem Persamaan Linier

# Kelompok 5
# Soal no 6

import numpy as np
M=np.array([(2,3,-1),(3,-2,1),(2,4,-1)])
y=np.array([6,2,9])

x=np.linalg.solve(M,y)
print(x)
