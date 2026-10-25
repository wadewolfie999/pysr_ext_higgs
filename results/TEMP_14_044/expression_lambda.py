# Version v5.3.0
import numpy

FEATURES = ('mchi1', 'mchipm1')

def predict(X):
    mchi1 = numpy.asarray(X['mchi1'], dtype=float)
    mchipm1 = numpy.asarray(X['mchipm1'], dtype=float)
    return numpy.broadcast_to(numpy.asarray(numpy.cos((numpy.cos(0.0011179575743389659*mchipm1) + numpy.cos(0.0036365157066324105*mchi1 - 0.5430077792785011))*numpy.cos(0.0007418339523333352*mchi1 + numpy.cos(0.0017245059292014982*mchi1 + 2*numpy.exp(mchi1 - mchipm1) - 0.995728453980836))), dtype=float), (len(X),)).copy()
