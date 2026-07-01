"""
memory.py

Leading-order gravitational-wave memory.
"""

import numpy as np

from .constants import G, C

# 1 Megaparsec in metres
MPC = 3.085677581e22


class Memory:

    def __init__(self, energy, distance=400):
        """
        Parameters
        ----------
        energy : ndarray
            Cumulative radiated energy (J)

        distance : float
            Source distance in Mpc
        """

        self.energy = energy
        self.distance = distance * MPC

    def strain(self):
        """
        Leading-order gravitational-wave memory strain.
        """

        return (
            4 * G * self.energy
            / (C**4 * self.distance)
        )