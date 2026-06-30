from src.gwmemory.binary import BinarySystem

binary = BinarySystem(36, 29)

print("="*40)
print("Binary Parameters")
print("="*40)

print(f"m1              = {binary.m1} Msun")
print(f"m2              = {binary.m2} Msun")
print(f"Total Mass      = {binary.total_mass:.2f} Msun")
print(f"Reduced Mass    = {binary.reduced_mass:.2f} Msun")
print(f"Eta             = {binary.eta:.4f}")
print(f"Chirp Mass      = {binary.chirp_mass:.2f} Msun")