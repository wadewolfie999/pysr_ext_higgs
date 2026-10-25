# Version v5.3.0
import numpy

FEATURES = ('mchi1', 'mchipm1')

def predict(X):
    mchi1 = numpy.asarray(X['mchi1'], dtype=float)
    mchipm1 = numpy.asarray(X['mchipm1'], dtype=float)
    return numpy.broadcast_to(numpy.asarray(1.230457690662212*numpy.exp(-numpy.exp(3*numpy.exp(3*(6.923296036632556*numpy.exp(3*numpy.exp(-12550.28898243733*(-mchi1 + mchipm1)**6*numpy.exp(51.248126907349775*numpy.exp(-1807.7661046528661*(-mchi1 + mchipm1)**3)))) - 0.99999890201231244)/mchipm1))/(mchi1*numpy.cos(numpy.cos(1.3048615280737272e-7*(-mchi1 + mchipm1)**3*numpy.exp(-6*numpy.exp(-3.6824283549543966/mchi1)))**3)**3)), dtype=float), (len(X),)).copy()
