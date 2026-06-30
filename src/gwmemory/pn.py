"""
pn.py

Leading-order Post-Newtonian inspiral evolution.
"""

import numpy as np

from .constants import G, C, M_SUN, PI
from .binary import BinarySystem


class Inspiral:

    def __init__(self, binary, f0=20.0, dt=1e-4):

        self.binary = binary
        self.f0 = f0
        self.dt = dt
    @property
    def chirp_mass(self):
        """
        Chirp mass in kilograms.
        """
        return self.binary.chirp_mass * M_SUN
        
    def dfdt(self, f):
        """
        Leading-order PN frequency evolution.
        """

        coefficient = (
            (96/5)
            * PI**(8/3)
            * (G * self.chirp_mass / C**3)**(5/3)
        )

        return coefficient * f**(11/3)
        
        
    def evolve(self, duration):

        nsteps = int(duration / self.dt)

        time = np.zeros(nsteps)
        frequency = np.zeros(nsteps)

        frequency[0] = self.f0

        for i in range(nsteps - 1):

            time[i + 1] = time[i] + self.dt

            frequency[i + 1] = (
                frequency[i]
                + self.dfdt(frequency[i]) * self.dt
            )

        return time, frequency
        
    def evolve_rk4(self, duration):

        nsteps = int(duration / self.dt)

        time = np.zeros(nsteps)
        frequency = np.zeros(nsteps)

        frequency[0] = self.f0

        for i in range(nsteps - 1):

          time[i + 1] = time[i] + self.dt

          f = frequency[i]

          k1 = self.dfdt(f)
          k2 = self.dfdt(f + 0.5 * self.dt * k1)
          k3 = self.dfdt(f + 0.5 * self.dt * k2)
          k4 = self.dfdt(f + self.dt * k3)

          frequency[i + 1] = (
            f
            + (self.dt / 6.0)
            * (k1 + 2*k2 + 2*k3 + k4)
          )

        return time, frequency
        
    def analytical_frequency(self, time):

       K = (
         (96/5)
         * PI**(8/3)
         * (G*self.chirp_mass/C**3)**(5/3)
       )

       return (
          self.f0**(-8/3)
          - (8/3)*K*time
       )**(-3/8)