import matplotlib.pyplot as plt
import numpy as np
from SQL import *
import pandas as pd


class Plot:
    def __init__(self, x_axis, y_axis):
        self.x_axis = x_axis
        self.y_axis = y_axis

    def spectrum(self, x_axis_name, y_axis_name, title):
        plt.plot(self.x_axis, self.y_axis)
        plt.axis('tight')
        plt.xlabel(x_axis_name)
        plt.xlabel(y_axis_name)
        plt.title(title)
        plt.show()


value = InProcessData('UVVis', 'Absorptance', values).get_specific_data(8)
wavelength = InProcessData('UVVis', 'Absorptance', wavelengths).get_specific_data(8)

spectrum = Plot(wavelength, value).spectrum('wavelength', 'Absorptance', 'UVVis')