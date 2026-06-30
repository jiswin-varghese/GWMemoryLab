from src.gwmemory.binary import BinarySystem
from src.gwmemory.pn import Inspiral
import matplotlib.pyplot as plt
import numpy as np

binary = BinarySystem(30, 30)

solver = Inspiral(binary, dt=0.01)


t1, f1 = solver.evolve(0.2)
t2, f2 = solver.evolve_rk4(0.2)
f_exact = solver.analytical_frequency(t2)
f_exact = solver.analytical_frequency(t2)

plt.figure(figsize=(8,5))

plt.plot(t1, f1, '--', label="Euler")
plt.plot(t2, f2, linewidth=2, label="RK4")
plt.plot(t2, f_exact, ':', linewidth=2, label="Analytical")

plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.title("Validation of the PN Inspiral Solver")

plt.legend()
plt.grid()

plt.savefig("docs/figures/pn_validation_.png", dpi=300)

print("Validation figure saved.")

error = np.abs(f2 - f_exact)

print(f"Maximum error : {np.max(error):.6e} Hz")
print(f"Mean error    : {np.mean(error):.6e} Hz")