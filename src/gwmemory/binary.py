"""
binary.py

Binary black-hole system.
"""

from dataclasses import dataclass

from .constants import G, C, PI, M_SUN


@dataclass
class BinarySystem:

    # User inputs (solar masses)
    m1: float
    m2: float

    @property
    def total_mass(self):
        return self.m1 + self.m2

    @property
    def chirp_mass(self):
        return ((self.m1 * self.m2) ** (3/5)) / ((self.m1 + self.m2) ** (1/5))

    @property
    def eta(self):
        return (self.m1 * self.m2) / (self.total_mass ** 2)

    @property
    def m1_si(self):
        return self.m1 * M_SUN

    @property
    def m2_si(self):
        return self.m2 * M_SUN

    @property
    def total_mass_si(self):
        return self.total_mass * M_SUN

    @property
    def chirp_mass_si(self):
        return self.chirp_mass * M_SUN

    @property
    def reduced_mass_si(self):
        return (self.m1_si * self.m2_si) / self.total_mass_si

    @property
    def isco_frequency(self):
        return (
            C**3 /
            (PI * (6**1.5) * G * self.total_mass_si)
        )