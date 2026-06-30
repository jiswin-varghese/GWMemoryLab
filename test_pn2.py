from src.gwmemory.binary import BinarySystem
from src.gwmemory.pn import Inspiral
import matplotlib.pyplot as plt
import numpy as np

binary = BinarySystem(30, 30)

solver = Inspiral(binary, dt=0.01)


t1, f1 = solver.evolve(0.2)
t2, f2 = solver.evolve_rk4(0.2)
f_exact = solver.analytical_frequency(t2)
plt.figure(figsize=(8,5))

plt.plot(t1, f1, "--", label="Euler")
plt.plot(t2, f2, label="RK4")
plt.plot(t2, f_exact, ":", linewidth=2,
         label="Analytical")

plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.title("PN Inspiral Validation")

plt.legend()
plt.grid()

plt.savefig("pn_validation.png", dpi=300)

print("Figure saved as pn_validation.png")
error = np.abs(f2 - f_exact)

print("Maximum error:", np.max(error))
print("Mean error:", np.mean(error))