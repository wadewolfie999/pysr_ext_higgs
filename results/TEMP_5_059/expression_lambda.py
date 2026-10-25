# Version v5.3.0
import numpy

FEATURES = ('mchi1', 'mchipm1')

def predict(X):
    mchi1 = numpy.asarray(X['mchi1'], dtype=float)
    mchipm1 = numpy.asarray(X['mchipm1'], dtype=float)
    return numpy.broadcast_to(numpy.asarray(numpy.cos(2601701849.6049196/(4.6519505259157803*mchi1**2/(0.9668685139528674*mchipm1 + (mchi1 + 1/(((mchi1 - mchipm1)**2 - 0.02200355064329114)**2*numpy.cos(1124.9483020019968/(4.6519505259157803*mchi1**2/(mchipm1 + 0.9668685139528674 + 1891639.3970876367/mchipm1**2) + mchipm1 + 1124.9483020019968))))**2/mchipm1**2) + mchipm1 + 1124.9483020019968)**3)**18, dtype=float), (len(X),)).copy()
