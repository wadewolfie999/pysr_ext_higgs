# Version v5.3.0
import numpy

FEATURES = ('mchi1', 'mchipm1')

def predict(X):
    mchi1 = numpy.asarray(X['mchi1'], dtype=float)
    mchipm1 = numpy.asarray(X['mchipm1'], dtype=float)
    return numpy.broadcast_to(numpy.asarray(numpy.cos((numpy.cos(0.006771653483997484*mchi1*numpy.cos(0.0010624337867578971*mchipm1)*numpy.cos(0.22086834599835395/(mchi1 - mchipm1))) + numpy.cos(0.0013335603759751385*mchi1 - numpy.cos(0.0010624337867578971*mchipm1)))*numpy.cos(0.0015533284844867915*mchi1)*numpy.cos(1.2526123639497352e-6*mchipm1**2*numpy.cos(0.0006219766309761784*mchipm1))), dtype=float), (len(X),)).copy()
