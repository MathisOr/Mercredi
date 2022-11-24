print('maths')

import numpy
from matplotlib import pyplot

pyplot.figure()
x = numpy.linspace(-numpy.pi, numpy.pi, 100)
y = numpy.sin(x)
pyplot.plot(x, y)
pyplot.show()