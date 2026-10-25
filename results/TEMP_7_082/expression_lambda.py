# Version v5.3.0
import numpy

FEATURES = ('mchi1', 'mchipm1')

def predict(X):
    mchi1 = numpy.asarray(X['mchi1'], dtype=float)
    mchipm1 = numpy.asarray(X['mchipm1'], dtype=float)
    return numpy.broadcast_to(numpy.asarray(1.239945070371659*numpy.cos(285.0163090640031/(1.09530417787674*mchi1 + 162.4535037117941))**2*numpy.cos(1.586908423231659*numpy.cos(1.904573633324856*numpy.cos(numpy.cos(1.889080952963016*numpy.cos(numpy.cos(1.83184626582135*numpy.cos(142.50826222441612/mchipm1)**4*numpy.cos(numpy.cos(1.0822340599408649/(2*mchi1 - 2*mchipm1 + 0.6500800138018834))))/(mchi1 - mchipm1 - 0.39662441926791125)))/(mchi1 - mchipm1 - 0.43293892967454467)))), dtype=float), (len(X),)).copy()
