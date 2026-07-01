from src.gwmemory.binary import BinarySystem
from src.gwmemory.pn import Inspiral

binary = BinarySystem(30, 30)

solver = Inspiral(binary)

t, f = solver.evolve_to_merger()

print("Initial frequency :", f[0])
print("Final frequency   :", f[-1])
print("ISCO frequency    :", binary.isco_frequency)
print("Number of steps   :", len(t))
print("Duration          :", t[-1], "seconds")