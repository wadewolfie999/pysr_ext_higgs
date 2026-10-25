# Version v5.3.0
import numpy

FEATURES = ('mchi1', 'mchipm1')

def predict(X):
    mchi1 = numpy.asarray(X['mchi1'], dtype=float)
    mchipm1 = numpy.asarray(X['mchipm1'], dtype=float)
    return numpy.broadcast_to(numpy.asarray(0.0024014686028372913*mchi1 - 5.5619591698021137e-5*mchipm1*numpy.cos(1.9818570139556385e-6*mchipm1**2) - 3.0001136419956882e-7*(-mchi1 + mchipm1)**2 + 0.61074652692370113*(mchi1/mchipm1 - 0.3640153559561071)*(-2.3481549045374917e-6*mchipm1**2 + numpy.cos(-0.002950812503982865*mchipm1 + 0.16114244372418238 + (-mchi1 + mchipm1 - 0.44883882821779203)/(-mchi1 + mchipm1)) - 0.7586481852215448), dtype=float), (len(X),)).copy()
