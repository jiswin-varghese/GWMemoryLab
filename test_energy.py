from src.gwmemory.binary import BinarySystem
from src.gwmemory.pn import Inspiral
from src.gwmemory.energy import EnergyFlux

binary = BinarySystem(30, 30)

solver = Inspiral(binary)

t, f = solver.evolve_to_merger()

energy = EnergyFlux(binary, f)

flux = energy.flux()

print("Initial flux :", flux[0])
print("Final flux   :", flux[-1])
assert flux[-1] > flux[0]

print("✓ Energy flux increases.")