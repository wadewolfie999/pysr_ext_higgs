# Version v5.3.0
import numpy

FEATURES = ('mchi1', 'mchipm1')

def predict(X):
    mchi1 = numpy.asarray(X['mchi1'], dtype=float)
    mchipm1 = numpy.asarray(X['mchipm1'], dtype=float)
    return numpy.broadcast_to(numpy.asarray(0.0001563314903542978*mchi1 + numpy.cos(0.00042971526622973184*mchi1 + 0.10901053160131852*numpy.cos(0.010220335652266464*mchi1) + numpy.cos(0.00084221563880952839*mchi1 + 0.00064448579685492447*mchi1/(mchi1 - mchipm1) + 0.0012134516010386314*mchipm1 - 47.381992390600867 + (mchi1**2/(mchipm1 - 2.4824165868394656) + mchi1)/(mchipm1 + 187.9373802434672)) - 0.6799123723908508), dtype=float), (len(X),)).copy()
