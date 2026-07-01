from src.gwmemory.binary import BinarySystem
from src.gwmemory.pn import Inspiral
from src.gwmemory.waveform import Waveform

import matplotlib.pyplot as plt

binary = BinarySystem(30,30)

solver = Inspiral(binary)

t,f = solver.evolve_rk4(0.2)

wave = Waveform(t,f)

phi = wave.phase()

plt.plot(t,phi)

plt.xlabel("Time (s)")
plt.ylabel("Phase (rad)")
plt.title("Gravitational-Wave Phase")

plt.grid()

plt.savefig("docs/figures/phase.png")