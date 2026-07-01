from src.gwmemory.binary import BinarySystem
from src.gwmemory.pn import Inspiral
from src.gwmemory.waveform import Waveform

import matplotlib.pyplot as plt

binary = BinarySystem(30,30)

solver = Inspiral(binary)

t,f = solver.evolve_rk4(0.2)

wave = Waveform(t,f)

h = wave.strain()

plt.figure(figsize=(10,4))

plt.plot(t,h)

plt.xlabel("Time (s)")
plt.ylabel("Normalized Strain")

plt.title("Gravitational-Wave Chirp")

plt.grid()

plt.savefig("docs/figures/chirp_waveform.png", dpi=300)