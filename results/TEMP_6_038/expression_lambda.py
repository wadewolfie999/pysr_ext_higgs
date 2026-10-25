# Version v5.3.0-ATTEMPT2
import numpy

FEATURES = ('mchi1', 'mchipm1')

def predict(X):
    mchi1 = numpy.asarray(X['mchi1'], dtype=float)
    mchipm1 = numpy.asarray(X['mchipm1'], dtype=float)
    return numpy.broadcast_to(numpy.asarray(0.5329653825951353*mchi1*(numpy.sin((-mchi1 + mchipm1)**4)**2)**(1/16)*numpy.sin(numpy.sinh(1.2624352887127586/mchipm1)) + 0.3618155531824624*mchipm1**(1/4) - 1.505232312261181, dtype=float), (len(X),)).copy()
