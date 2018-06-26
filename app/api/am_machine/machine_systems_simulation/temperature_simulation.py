import numpy as np
from numpy.random import ranf
from .base import BasicSystem


class ExtruderTemperature(BasicSystem):

    def __init__(self, data_handler, inputs, outputs, **kwargs):
        BasicSystem.__init__(self, data_handler, inputs, outputs)
        self.ambient_temp = 20.

        options = dict()
        if 'options' in kwargs:
            options = kwargs['options']

        self.n_extruders = 1
        if 'n_extruders' in options:
            self.n_extruders = options['n_extruders']

        self.n_sensors = 1
        if 'n_sensors' in options:
            self.n_sensors = options['n_sensors']

        self.x1 = np.zeros(self.n_extruders)
        self.x2 = np.zeros(self.n_extruders)
        self.x3 = np.zeros(self.n_extruders)

        self.alpha = 0.1
        self.beta = 0.1

        self.active = [False for ext in range(self.n_extruders)]

    def process(self):
        u = self.data_handler.get_node(self.inputs).get_value()
        for i, val in enumerate(u):
            if val > 0:
                self.active[i] = True
            u[i] = 0 if self.active[i] else val

        out = np.zeros([self.n_extruders, self.n_sensors])

        for e in range(self.n_extruders):
            for s in range(self.n_sensors):
                out[e, s] = self.x1[e] + self.ambient_temp + (ranf() - 0.5) * 0.5

            self.x3[e] = (self.alpha * (u[e] - self.ambient_temp - self.x1[e]) - self.beta * self.x2[e]) * self.dt
            self.x2[e] += self.x3[e]
            self.x1[e] += self.x2[e] + (ranf() - 0.5)

        self.data_handler.get_node(self.outputs).set_value(out.tolist())
