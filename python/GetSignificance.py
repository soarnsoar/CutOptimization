import ROOT
import sys
sys.path.insert(0,'python')
#MakeHistograms.py  ValueToMaximize.py
from MakeHistograms import MakeCombinedHisto
#def MakeCombinedHisto(inputpath,proclist,CutName,VariableName):
from ValueToMaximize import GetStoSqrtB
#def GetStoSqrtB(histo_s, histo_b,x1,x2):

def GetSignificance(mass,inputpath,VariableName,CutName,BKGLIST,x1,x2,isVBFSIG=True):
    mass=str(mass)
    if isVBFSIG:
        SIG="qqH_hww"+mass+"_RelW002"
    else:
        SIG="ggH_hww"+mass+"_RelW002"

    hbkg=MakeCombinedHisto(inputpath, BKGLIST,CutName,VariableName)
    hbkg.SetName("bkg")
    hsig=MakeCombinedHisto(inputpath, [SIG],CutName,VariableName)
    
    sgnfc=GetStoSqrtB(hsig,hbkg,x1,x2)
    return sgnfc
    #print sgnfc
    
    #N=hsig.GetNbinsX()
    #XMAX=hsig.GetBinLowEdge(N)+hsig.GetBinWidth(N)
    #print XMAX

def GetSignificanceList(mass,inputpath,VariableName,CutName,BKGLIST,DoLowercut=True,isVBFSIG=True):
    mass=str(mass)
    if isVBFSIG:
        SIG="qqH_hww"+mass+"_RelW002"
    else:
        SIG="ggH_hww"+mass+"_RelW002"

    hbkg=MakeCombinedHisto(inputpath, BKGLIST,CutName,VariableName)
    hbkg.SetName("bkg")
    hsig=MakeCombinedHisto(inputpath, [SIG],CutName,VariableName)
    N=hsig.GetNbinsX()
    XMIN=hsig.GetBinLowEdge(0)+hsig.GetBinWidth(0)
    XMAX=hsig.GetBinLowEdge(N)+hsig.GetBinWidth(N)
    #print XMIN
    #print XMAX
    x_list=[]
    s_list=[]
    b_list=[]
    sgnfc_list=[]
    if DoLowercut:
        for i in range(N+1):
            x1=hsig.GetBinLowEdge(i)+hsig.GetBinWidth(i)
            x2=XMAX
            sgnfc,s,b=GetStoSqrtB(hsig,hbkg,x1,x2)
            if not sgnfc : sgnfc=0
            x_list.append(x1)
            s_list.append(s)
            b_list.append(b)
            sgnfc_list.append(sgnfc)
    else:
        for i in range(N+1):
            x1=XMIN
            x2=hsig.GetBinLowEdge(i)+hsig.GetBinWidth(i)
            sgnfc,s,b=GetStoSqrtB(hsig,hbkg,x1,x2)
            if not sgnfc : sgnfc=0
            x_list.append(x2)
            s_list.append(s)
            b_list.append(b)
            sgnfc_list.append(sgnfc)
    

    return x_list,sgnfc_list,s_list,b_list


if __name__ == '__main__':
    inputpath="../rootFile_2016__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Boosted_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root"
    VariableName="DNN_isVBF_OTF"
    CutName="__BoostedALL_SR_NoMEKDCut"
    BKGLIST=[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww']
    
    #sgnfc=GetSignificance(1000,inputpath,VariableName,CutName,BKGLIST,0.95,1.0)
    xlist,sgnfclist,slist,blist=GetSignificanceList(1000,inputpath,VariableName,CutName,BKGLIST)
    print xlist,sgnfclist
    print len(xlist)
