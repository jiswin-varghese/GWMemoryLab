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

from .constants import G, C, PI, M_SUN
@dataclass
class BinarySystem:
    """
    Binary black-hole system.
    """

    m1: float
    m2: float

    @property
    def total_mass(self):
        """
        Total mass in kilograms.
        """
        return (self.m1 + self.m2) * M_SUN

    @property
    def reduced_mass(self):
        return ((self.m1 * M_SUN) * (self.m2 * M_SUN)) / self.total_mass

    @property
    def eta(self):
       return ((self.m1 * M_SUN) * (self.m2 * M_SUN)) / (self.total_mass**2)

    @property
    def chirp_mass(self):
      m1 = self.m1 * M_SUN
      m2 = self.m2 * M_SUN
      M = m1 + m2

      return (m1 * m2)**(3/5) / M**(1/5)
      
    def isco_frequency(self):
        """
          Approximate gravitational-wave frequency at the ISCO.
        """

        return (
            C**3 /
            (PI * (6**1.5) * G * self.total_mass)
        )