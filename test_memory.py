from src.gwmemory.binary import BinarySystem
from src.gwmemory.pn import Inspiral
from src.gwmemory.energy import EnergyFlux
from src.gwmemory.memory import Memory

import matplotlib.pyplot as plt

binary = BinarySystem(30,30)

solver = Inspiral(binary)

t, f = solver.evolve_to_merger()

energy = EnergyFlux(binary, f)

E = energy.radiated_energy(t)

memory = Memory(E, distance=400)

h_mem = memory.strain()

print("Initial memory :", h_mem[0])
print("Final memory   :", h_mem[-1])

plt.figure(figsize=(8,5))

plt.plot(t, h_mem)

plt.xlabel("Time (s)")
plt.ylabel("Memory Strain")

plt.title("Leading-Order Gravitational-Wave Memory")

plt.grid()

plt.savefig("docs/figures/memory.png", dpi=300)
print("graph saved as memory.png")

plt.show()