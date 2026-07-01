from src.gwmemory.binary import BinarySystem
from src.gwmemory.pn import Inspiral
from src.gwmemory.energy import EnergyFlux

binary = BinarySystem(30, 30)

solver = Inspiral(binary)

t, f = solver.evolve_to_merger()

energy = EnergyFlux(binary, f)

E = energy.radiated_energy(t)

print("Initial energy :", E[0])
print("Final energy   :", E[-1])

assert E[-1] > E[0]

print("✓ Radiated energy increases.")

import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))

plt.plot(t, E)

plt.xlabel("Time (s)")
plt.ylabel("Radiated Energy (J)")

plt.title("Cumulative Radiated Energy")

plt.grid()

plt.savefig("docs/figures/radiated_energy.png", dpi=300)

print("graph saved as radiated_energy.png")

plt.show()