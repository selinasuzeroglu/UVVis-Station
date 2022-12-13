import matplotlib.pyplot as plt
import numpy as np
from SQL import *
import pandas as pd

value = InProcessData('UVVis', 'Absorptance', values).get_specific_data(8)
wavelength = InProcessData('UVVis', 'Absorptance', wavelengths).get_specific_data(8)


plt.plot(wavelength, value)
plt.axis('tight')
plt.show()

