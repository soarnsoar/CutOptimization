import ROOT
from copy import deepcopy


def MakeCombinedHisto(inputpath,proclist,CutName,VariableName):
    tfile=ROOT.TFile.Open(inputpath)

    idx=0
    for proc in proclist:
        if idx==0:
            h=tfile.Get(CutName+"/"+VariableName+"/"+"histo_"+proc)

        else:
            #print 'CutName',CutName
            htemp=tfile.Get(CutName+"/"+VariableName+"/"+"histo_"+proc)
            h.Add(htemp)
            
        idx+=1
    


    h.SetDirectory(0)
    tfile.Close()
    return h

def MakeCombinedHisto_test(inputpath,proclist,CutName,VariableName):
    tfile=ROOT.TFile.Open(inputpath)

    idx=0
    for proc in proclist:
        print proc
        if idx==0:
            h=tfile.Get(CutName+"/"+VariableName+"/"+"histo_"+proc)
            print h.GetBinLowEdge(21)
            print h.GetBinContent(21)
        else:
            
            htemp=tfile.Get(CutName+"/"+VariableName+"/"+"histo_"+proc)
            print h.GetBinLowEdge(21)
            print htemp.GetBinContent(21)
            h.Add(htemp)
            
        idx+=1
    


    h.SetDirectory(0)
    tfile.Close()
    return h



if __name__ == '__main__':
    #inputpath="../2016/NoCB/rootFile_2016__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Boosted_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root"
    inputpath="../2016/NoCB/rootFile_2016__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root"
    mass="1000"

    VariableName="DNN_isVBF_OTF"
    #CutName="__BoostedALL_SR_NoMEKDCut"
    CutName="___ResolvedVBFDNN__SR_NoMEKDCut"
    BKGLIST=[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww']
    SIG="qqH_hww_"+mass+"_RelW002"
    
    h=MakeCombinedHisto_test(inputpath, BKGLIST,CutName,VariableName)
    #print h.GetBinContent(21)
    #print h.Integral(21,21)
