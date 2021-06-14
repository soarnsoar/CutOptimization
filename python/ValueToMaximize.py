###------Value to Maximize
import ROOT
import math
def GetStoSqrtB(histo_s, histo_b,x1,x2):
    
    binx1_s=histo_s.FindBin(x1)
    binx2_s=histo_s.FindBin(x2)

    binx1_b=histo_b.FindBin(x1)
    binx2_b=histo_b.FindBin(x2)

    if not (binx1_s==binx1_b and binx2_s==binx2_b): 
        print "bin is not equivalent"
        return False
    binx1=binx1_s
    binx2=binx2_s
    S=histo_s.Integral(binx1,binx2)
    B=histo_b.Integral(binx1,binx2)
    
    if B<=0: 
        print "B is zero or negative"
        return False
    if S<0:
        print "S is negative"
        return False
    ret=S/math.sqrt(B)
    return ret