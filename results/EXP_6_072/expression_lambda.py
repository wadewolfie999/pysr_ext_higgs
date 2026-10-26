# Version v5.3.1
import numpy

FEATURES = ('mchi1', 'mchipm1')

def predict(X):
    mchi1 = numpy.asarray(X['mchi1'], dtype=float)
    mchipm1 = numpy.asarray(X['mchipm1'], dtype=float)
    return numpy.broadcast_to(numpy.asarray(3.6476351559826954*((-0.2675904440173584/((mchi1 - 0.1709438368060553)*(mchipm1/((-0.6304848019479864)*((0.066146833040938411/(0.2977333128821026/(mchipm1 + mchipm1) + (mchi1 - mchipm1)/mchi1)**2))*(0.07260831044039938 + 8.951199122075424/((0.1709438368060553*mchi1)))**2) - 0.2675904440173584/mchipm1)) + 0.6955345839831512/((-35.45092321820688/((0.07250052755844655 + 8.951197831291678/((0.17101141999820696*mchi1)))*(mchi1 - 0.4793761720213704)))))**2 - 1.5895574426136225 - (-1)*8.673023774159901/(12261068026780.55/(mchi1 - mchipm1)**4)) - 0.6181144824152078, dtype=float), (len(X),)).copy()
