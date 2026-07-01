from src.gwmemory.binary import BinarySystem
from src.gwmemory.pn import Inspiral
from src.gwmemory.waveform import Waveform

import matplotlib.pyplot as plt

binary = BinarySystem(30,30)

solver = Inspiral(binary)

#t,f = solver.evolve_rk4(0.2)
t, f = solver.evolve_to_merger()

wave = Waveform(t,f)

h = wave.strain()

plt.plot(t, h)

plt.ylabel("Normalized Strain")
plt.title("Leading-Order Gravitational-Wave Chirp")
plt.title("Gravitational-Wave Phase")

plt.grid()

plt.savefig("docs/figures/chirp_waveform.png", dpi=300)