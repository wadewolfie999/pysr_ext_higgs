# Version v5.3.0
import numpy

FEATURES = ('mchi1', 'mchipm1')

def predict(X):
    mchi1 = numpy.asarray(X['mchi1'], dtype=float)
    mchipm1 = numpy.asarray(X['mchipm1'], dtype=float)
    return numpy.broadcast_to(numpy.asarray(numpy.cos((-0.0016464956341800338*mchi1*(numpy.exp(mchi1 - mchipm1) - 0.8712027804933787) - 0.8749126159685751)*(numpy.cos((numpy.exp(mchi1 - mchipm1) - 0.8594876517622306)*(0.061305330738716246*mchi1 + 0.0013968196536284425*mchipm1*(mchi1 - mchipm1) - numpy.cos(numpy.cos(mchipm1)))*numpy.exp(mchi1 - mchipm1)) + numpy.cos(2.7715166273604876e-6*mchipm1*(mchi1 - mchipm1) + 0.001984162107227708*mchipm1))*numpy.cos(numpy.cos(0.0017199045572864197*mchipm1) - 0.6698894944561484)), dtype=float), (len(X),)).copy()
