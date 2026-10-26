# Version v5.3.1
import numpy

FEATURES = ('mchi1', 'mchipm1')

def predict(X):
    mchi1 = numpy.asarray(X['mchi1'], dtype=float)
    mchipm1 = numpy.asarray(X['mchipm1'], dtype=float)
    return numpy.broadcast_to(numpy.asarray(0.0033950534040495324*mchipm1 + ((-0.753678714667031)*mchi1*mchi1/((mchipm1*(mchi1 + (mchi1 + 0.0005938908358292764*(mchi1 + mchipm1 + mchipm1 - (-1.3238102377649212))/((-(mchi1 - mchipm1) - 0.15810562309423207)*(-(mchi1 - mchipm1) - 0.15810562309423207)))/(-0.48181628950593397)))) - 1.289952325711101)**3 - 1.3238102377649212 + (mchi1 - 0.8979487806648314)/mchipm1, dtype=float), (len(X),)).copy()
