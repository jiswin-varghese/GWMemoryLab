from src.gwmemory.binary import BinarySystem
from src.gwmemory.pn import Inspiral

binary = BinarySystem(30,30)

solver = Inspiral(binary)

t, f = solver.evolve(0.2)

print("Initial frequency:", f[0])
print("Final frequency:", f[-1])

import matplotlib.pyplot as plt

plt.plot(t, f)

plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.title("Leading-order PN Inspiral")

plt.grid()

plt.savefig("pn_inspiral.png", dpi=300)
print("Figure saved as pn_inspiral.png ")