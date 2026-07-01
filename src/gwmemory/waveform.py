"""
waveform.py

Gravitational-wave phase evolution.
"""

import numpy as np

from .constants import PI


class Waveform:

    def __init__(self, time, frequency):

        self.time = time
        self.frequency = frequency

    def phase(self):

        phi = np.zeros_like(self.time)

        dt = self.time[1] - self.time[0]

        for i in range(len(self.time)-1):

            phi[i+1] = (
                phi[i]
                + 2*PI*self.frequency[i]*dt
            )

        return phi
        
        
    def amplitude(self):

          amp = (self.frequency / self.frequency[0])**(2/3)

          return amp / np.max(amp)
          
          
    def strain(self):

          amp = self.amplitude()

          phi = self.phase()

          return amp * np.cos(phi)