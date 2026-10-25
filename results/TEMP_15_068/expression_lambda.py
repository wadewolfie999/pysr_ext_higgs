# Version v5.3.0
import numpy

FEATURES = ('mchi1', 'mchipm1')

def predict(X):
    mchi1 = numpy.asarray(X['mchi1'], dtype=float)
    mchipm1 = numpy.asarray(X['mchipm1'], dtype=float)
    return numpy.broadcast_to(numpy.asarray(numpy.cos((numpy.cos(0.0040287826938821689*mchi1 - 0.00049729729813319252*mchi1/(-mchi1 + mchipm1)) + 0.5645274129759962)*numpy.cos(5.71690793620207e-7*mchipm1**2)*numpy.cos(-0.003611299686454646*mchi1 + 0.0005245936877285318*mchi1/(-mchi1 + mchipm1) + 8.6055580634205687e-10*mchipm1**2*(2*mchi1 + mchipm1))), dtype=float), (len(X),)).copy()
