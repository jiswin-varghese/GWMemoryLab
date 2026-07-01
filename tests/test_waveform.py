import numpy as np

from src.gwmemory.binary import BinarySystem
from src.gwmemory.pn import Inspiral
from src.gwmemory.waveform import Waveform

binary = BinarySystem(30,30)

solver = Inspiral(binary)

t,f = solver.evolve_rk4(0.2)

wave = Waveform(t,f)

phi = wave.phase()

assert np.all(np.diff(phi) > 0), \
    "Phase is not increasing."

print("✓ Phase increases monotonically.")