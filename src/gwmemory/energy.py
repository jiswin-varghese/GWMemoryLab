"""
energy.py

Gravitational-wave energy flux.
"""

import numpy as np

from .constants import G, C, PI


class EnergyFlux:

    def __init__(self, binary, frequency):

        self.binary = binary
        self.frequency = frequency

    def flux(self):
        """
        Leading-order GW energy flux.
        """

        eta = self.binary.eta
        M = self.binary.total_mass_si

        coefficient = (
            (32 / 5)
            * (C**5 / G)
            * eta**2
        )

        x = (
            PI * G * M * self.frequency / C**3
        )**(10/3)

        return coefficient * x
    def radiated_energy(self, time):
        """
        Cumulative radiated energy using the trapezoidal rule.
        """

        flux = self.flux()

        energy = np.zeros_like(time)

        for i in range(1, len(time)):

            dt = time[i] - time[i-1]

            energy[i] = (
                energy[i-1]
                + 0.5 * (flux[i] + flux[i-1]) * dt
            )

        return energy