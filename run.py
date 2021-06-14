import ROOT
import sys
sys.path.insert(0,'python')
#MakeHistograms.py  ValueToMaximize.py
from MakeHistograms import MakeCombinedHisto
#def MakeCombinedHisto(inputpath,proclist,CutName,VariableName):
from ValueToMaximize import GetStoSqrtB
#def GetStoSqrtB(histo_s, histo_b,x1,x2):
from GetSignificance import GetSignificanceList
#def GetSignificanceList(mass,inputpath,VariableName,CutName,BKGLIST,DoLowercut=True,isVBFSIG=True):

if __name__ == '__main__':
    #inputpath="../rootFile_2016__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Boosted_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root"
    #VariableName="DNN_isVBF_OTF"
    #CutName="__BoostedALL_SR_NoMEKDCut"
    #BKGLIST=[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww']
    
    #sgnfc=GetSignificance(1000,inputpath,VariableName,CutName,BKGLIST,0.95,1.0)
    ##--Load Config
    exec(open("config/config_v1.py","r")) ## create myconfig
    ##---Resolved2016
    cutname=myconfig["Resolved2016"]['cutname']
    variablename=myconfig["Resolved2016"]['variablename']
    bkglist=myconfig["Resolved2016"]["bkglist"]
    inputpath=myconfig["Resolved2016"]["inputpath"]
    xlist,sgnfclist,slist,blist=GetSignificanceList(1000,inputpath,variablename,cutname,bkglist)
    print xlist
    print sgnfclist
    print slist
    print blist
    #print len(xlist)
