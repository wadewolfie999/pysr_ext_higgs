# Version v5.3.0
import numpy

FEATURES = ('mchi1', 'mchipm1')

def predict(X):
    mchi1 = numpy.asarray(X['mchi1'], dtype=float)
    mchipm1 = numpy.asarray(X['mchipm1'], dtype=float)
    return numpy.broadcast_to(numpy.asarray(0.9831143619017236 - numpy.exp(4*(-9473.746885051392*mchi1*(mchi1 + mchipm1)/mchipm1**2 - mchipm1**2/(mchi1 + 3.3277173633206085))/(3048.383200273093*mchipm1/((-0.03905646364146095*mchi1*(-381.32667087515931*mchi1**12/(-mchi1 + (1.4868466271092322 + (3.333641668254851 - 7015.862366316909/mchipm1)*(55.211646150405386*mchi1 - 55.257719520092348)*(mchipm1 - 18.787663910564365)/mchi1)**2)**3 + mchi1 - 2.3159940700174513*mchipm1 + numpy.cos(mchi1)**3 + 0.03905646364146095) + 5.7700305017944293e-8*mchipm1**2*(mchipm1 + 18.787663910564365)**2/(3.333641668254851 - 7015.862366316909/mchipm1)**2)*numpy.cos(3.8571244396442319*numpy.exp(6*mchi1 - 6*mchipm1))) + 7.2515758500794005)**2), dtype=float), (len(X),)).copy()
