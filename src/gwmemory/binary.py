"""
binary.py
==========

Binary black-hole parameters.

Inputs:
    m1, m2 : Solar masses

Outputs:
    Total mass
    Reduced mass
    Symmetric mass ratio
    Chirp mass
"""

from dataclasses import dataclass


@dataclass
class BinarySystem:
    """
    Binary black-hole system.
    """

    m1: float
    m2: float

    @property
    def total_mass(self):
        return self.m1 + self.m2

    @property
    def reduced_mass(self):
        return (self.m1 * self.m2) / self.total_mass

    @property
    def eta(self):
        return (self.m1 * self.m2) / (self.total_mass ** 2)

    @property
    def chirp_mass(self):
        return ((self.m1 * self.m2) ** (3/5)) / (self.total_mass ** (1/5))