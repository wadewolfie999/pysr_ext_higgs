# Version v5.3.0
import numpy

FEATURES = ('mchi1', 'mchipm1')

def predict(X):
    mchi1 = numpy.asarray(X['mchi1'], dtype=float)
    mchipm1 = numpy.asarray(X['mchipm1'], dtype=float)
    return numpy.broadcast_to(numpy.asarray(numpy.cos(numpy.cos(0.0061297098632736863*mchi1**3*mchipm1*(numpy.cos(numpy.cos(numpy.cos(0.0067415218184474576*mchi1**4*(numpy.cos(numpy.cos(0.039411289288254768*mchipm1**2*numpy.cos(mchipm1 - 1.0993553408313173)*numpy.cos(numpy.cos(numpy.cos((numpy.cos(mchi1**2) - 1.180370972830416)*(numpy.cos(numpy.cos(1.0864409736134717/mchi1)) + numpy.cos(numpy.cos(4.4499460275467418e-6*mchi1*(numpy.exp(0.016448221487657004*mchi1/mchipm1**3) + 1.3952997099950084) + mchipm1 - 0.22967492753516194))))) - 1.0864409736134717)/mchi1**3)) - 0.2278992666066265)/(mchi1 - 0.6946425812491337)**3))) - 0.9950334412094952)/(mchi1 + 0.789102217619601)**3) + 0.4445403464765526) + 0.06227710785266158, dtype=float), (len(X),)).copy()
