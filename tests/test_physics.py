import numpy as np

from src.gwmemory.binary import BinarySystem
from src.gwmemory.pn import Inspiral

binary = BinarySystem(30, 30)

solver = Inspiral(binary)

t, f = solver.evolve_rk4(0.2)

# Test 1
assert np.all(np.diff(f) > 0), \
    "Frequency is not monotonically increasing."

print("✓ Test 1 passed: Frequency increases monotonically.")


# Test 2

assert f[-1] > f[0], \
    "Final frequency must exceed initial frequency."

print("✓ Test 2 passed: Final frequency is larger.")

f_exact = solver.analytical_frequency(t)

error = np.max(np.abs(f - f_exact))

assert error < 1e-8, \
    "Analytical validation failed."

print("✓ Test 3 passed: Analytical agreement.")


