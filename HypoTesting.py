import NormalDist  as Norm 
import scipy.stats as stats
import math        as math


def Print(pH0, pH1):
    print("H0: P = ", pH0)
    print("H1: P = ", pH1)

def NormalTest(Smean, mean, sd, samples):
    pH0 = 2 * Norm.PCLTLess(Smean, mean, sd, samples)
    pH1 = 1 - pH0
    Print(pH0, pH1)

def DiffMeans2distMore(mean1, sd1, S1, mean2, sd2, S2, confidence):
    alpha = 1 - confidence
    z = stats.norm.ppf(alpha)
    var1 = sd1**2
    var2 = sd2**2
    sd = math.sqrt(var1/S1 + var2/S2)
    NullMeanDiff = z * sd
    MeanDiff = mean1 - mean2
    print("Null Mean Difference: " + str(NullMeanDiff))
    print("Actual Mean Difference: " + str(MeanDiff))
    if NullMeanDiff >= MeanDiff:
        print("Accept H0, Reject H1")
    else:
        print("Reject H0, Accept H1")

def DiffMeans2distLess(mean1, sd1, S1, mean2, sd2, S2, confidence):
    alpha = 1 - confidence
    z = stats.norm.ppf(alpha)
    var1 = sd1**2
    var2 = sd2**2
    sd = math.sqrt(var1/S1 + var2/S2)
    NullMeanDiff = z * sd
    MeanDiff = mean1 - mean2
    print("Null Mean Difference: " + str(NullMeanDiff))
    print("Actual Mean Difference: " + str(MeanDiff))
    if NullMeanDiff <= MeanDiff:
        print("Accept H0, Reject H1")
    else:
        print("Reject H0, Accept H1")


def DiffMeansMore(smean, mean, sd, n, significance):
    t  = abs( stats.t.ppf(significance, n-1) )
    ts = Norm.getZ(smean, mean, (sd/math.sqrt(n)))
    if ts > t:
        print("Evidence for H1")
    else:
        print("No Evidence for H1")

def DiffMeansLess(smean, mean, sd, n, significance):
    t  = abs( stats.t.ppf(significance, n-1) )
    ts = Norm.getZ(smean, mean, (sd/math.sqrt(n)))
    if ts < t:
        print("Evidence for H1")
    else:
        print("No Evidence for H1")