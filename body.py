import numpy as np

G = 6.6743 * 10**(-11)
dt = .01

class Body:

    def __init__(self, m):
        self.mass = m
        self.r0 = np.zeros(3)
        self.v0 = np.zeros(3)
        self.a0 = np.zeros(3)

        self.r = self.r0
        self.v = self.v0
        self.a = self.a0

    def setInitPosition(self, x, y, z):
        self.r0 = np.array([x, y, z])

    def setInitVelocity(self, x, y, z):
        self.v0 = np.array([x, y, z])

    def reset(self):
        self.r = self.r0
        self.v = self.v0
        self.a = self.a0