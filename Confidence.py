import scipy.stats as stats
import math
import numpy

def CI(smean, sd, confidence, Samples):
    alpha = 1 - confidence
    zstar = abs( stats.norm.ppf(alpha/2) )
    MarginOfError = zstar * (sd / math.sqrt(Samples))
    LowerBound = smean - MarginOfError
    UpperBound = smean + MarginOfError
    return str(LowerBound) + " " + str(UpperBound)

def CIlist(obs, sd, confidence):
    smean = numpy.mean(obs)
    CI(smean, sd, confidence, len(obs))