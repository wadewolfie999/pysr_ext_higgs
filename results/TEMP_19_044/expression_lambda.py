# Version v5.3.0
import numpy

FEATURES = ('mchi1', 'mchipm1')

def predict(X):
    mchi1 = numpy.asarray(X['mchi1'], dtype=float)
    mchipm1 = numpy.asarray(X['mchipm1'], dtype=float)
    return numpy.broadcast_to(numpy.asarray(1.0471682425656008*numpy.cos(-0.5399005817691068*numpy.cos(0.06243687511774902/(-mchi1 + mchipm1)**2)*numpy.cos(numpy.cos(0.0038649110353923895*mchipm1)) + numpy.cos(0.0006160326007406046*mchi1 + mchi1/mchipm1 + 0.001246679746186349*mchipm1) + 1.223996039565275), dtype=float), (len(X),)).copy()
