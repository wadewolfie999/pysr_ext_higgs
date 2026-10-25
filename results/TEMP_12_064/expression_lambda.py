# Version v5.3.0
import numpy

FEATURES = ('mchi1', 'mchipm1')

def predict(X):
    mchi1 = numpy.asarray(X['mchi1'], dtype=float)
    mchipm1 = numpy.asarray(X['mchipm1'], dtype=float)
    return numpy.broadcast_to(numpy.asarray(numpy.cos((-mchi1 + mchipm1)*numpy.exp(mchi1 - mchipm1) + (numpy.cos(2.9071847628409433*(0.8698961291302949 - numpy.exp(mchi1 - mchipm1))/(mchi1 - mchipm1)) + numpy.cos((0.0023500341036272214*mchi1 + 0.8698961291302949)*numpy.cos(numpy.exp(mchi1 - mchipm1))))*numpy.cos(1.1842469812652451e-9*mchipm1**2/(mchi1 - mchipm1) - 0.0008099082877929833*mchipm1)), dtype=float), (len(X),)).copy()
