import ROOT
import sys
sys.path.insert(0,'python')
import os


#MakeHistograms.py  ValueToMaximize.py
from MakeHistograms import MakeCombinedHisto
#def MakeCombinedHisto(inputpath,proclist,CutName,VariableName):
from ValueToMaximize import GetStoSqrtB
#def GetStoSqrtB(histo_s, histo_b,x1,x2):
from GetSignificance import GetSignificanceList
#def GetSignificanceList(mass,inputpath,VariableName,CutName,BKGLIST,DoLowercut=True,isVBFSIG=True):
from array import array
def GetSgnfcList(mass,confpath,confname):
    exec(open(confpath,"r")) ## create myconfig
    ##---
    cutname=myconfig[confname]['cutname']
    variablename=myconfig[confname]['variablename']
    bkglist=myconfig[confname]["bkglist"]
    inputpath=myconfig[confname]["inputpath"]
    xlist,sgnfclist,slist,blist=GetSignificanceList(mass,inputpath,variablename,cutname,bkglist)
    #print xlist
    #print sgnfclist
    #print slist
    #print blist
    return xlist,sgnfclist,slist,blist
def GetSgnfcListBkg(mass,confpath,confname):
    exec(open(confpath,"r")) ## create myconfig
    crcutnames=myconfig[confname]['crcutnames']
    variablename=myconfig[confname]['variablename']
    bkglist=myconfig[confname]["bkglist"]
    inputpath=myconfig[confname]["inputpath"]
    #bkg
    dict_crb={}
    for cr in crcutnames:
        cutname=crcutnames[cr]
        xlist,sgnfclist,slist,blist=GetSignificanceList(mass,inputpath,variablename,cutname,bkglist)
        dict_crb[cr]=blist
    return dict_crb


def temp():
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
def GetMod(mylist):
    dict_number={}
    MaxNumber=-1
    for element in list(set(mylist)):
        nelement=0
        for a in mylist:
            if a==element: nelement+=1
        if nelement>=MaxNumber:
            MaxNumber=nelement

        dict_number[element]=nelement
    
    elementlist_WithMaxNumber=[]
    for element in dict_number:
        if dict_number[element]==MaxNumber:
            elementlist_WithMaxNumber.append(element)

    return sum(elementlist_WithMaxNumber)/len(elementlist_WithMaxNumber)

def DrawMassDNNscoreSgnfc(confname,confpath,rel=True,filtered=True,AddMaxLine=True): ## rel -> relative significance, filtered -> skip cut  98% of bkg
    suffix=""
    if rel: suffix+="_relsgnfc"
    if filtered: suffix+="_filter0p02"
    ##1) Define TH2D
    #TH2F (const char *name, const char *title, Int_t nbinsx, Double_t xlow, Double_t xup, Int_t nbinsy, Double_t ylow, Double_t yup)
    #confname="Resolved2016"
    #confpath="config/config_temp.py"
    #
    #masslist=[115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 900, 1000, 1500, 2000, 2500, 3000, 4000, 5000]
    masslist=[ 200, 210, 230, 250, 270, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 900, 1000, 1500, 2000, 2500, 3000, 4000, 5000]
    masslistbin=[]
    max_filtered_sgnfclist=[]
    for i in range(len(masslist)):
        bincenter=masslist[i]
        if i!=0:
            lbinwidth=masslist[i]-masslist[i-1]
        else:
            lbinwidth=masslist[i+1]-masslist[i]
        masslistbin.append(bincenter-lbinwidth/2)
    masslistbin.append(masslist[-1]+(masslist[-1]-masslist[-2])/2)
    print masslistbin
    masslistbin=array('d',masslistbin)
    score_for_maxsgnfc_list=[]
    filtered_xlist=[]
    Ndiv_orig=0.
    ##---Dictionary for variables to draw
    dict_to_draw={}
    #h.Fill(mass,xlist[i],rel_sgnfc)
    #h.Fill(mass,xlist[i],sgnfc)
    #dict_to_draw[mass][xlist]
    #dict_to_draw[mass][rel_sgnfc_list]
    #dict_to_draw[mass][sgnfc_list]

    for mass in masslist:
        dict_to_draw[mass]={}
        dict_to_draw[mass]['xlist']=[]
        dict_to_draw[mass]['score_for_maxsgnfc_list']=[]
        dict_to_draw[mass]['sgnfc_list']=[]
        xlist,sgnfclist,slist,blist=GetSgnfcList(mass,confpath,confname)
        max_b=max(blist)
        max_s=max(slist)
        dict_to_draw[mass]['xlist']=xlist
        Ndiv_orig=float(len(xlist))
        ##--CR infos
        dict_crb=GetSgnfcListBkg(mass,confpath,confname)
        filtered_sgnfclist=[]
        for i in range(len(xlist)):
            #print "s eff.->",xlist[i],':',slist[i]/max_s
            #if blist[i]/max_b <0.02 and filtered:
            if filtered:
                isFINECR=True ## if there's no negative or zero CR yield
                ##--Check CRs
                for cr in dict_crb:
                    crbkg=dict_crb[cr][i]
                    if crbkg<=0: isFINECR=False


                if (blist[i]/max_b <0.02 or slist[i]/max_s < 0.1 or blist[i] <= 0 or isFINECR==False):
                    print xlist[i],mass
                    print '--> b decreasing to under 2%',blist[i]/max_b
                    print '--> s decreasing to under 10%',slist[i]/max_s
                    print '--> CR is fine?->',isFINECR
                    filtered_sgnfclist.append(0)
                else:
                    filtered_sgnfclist.append(sgnfclist[i])
                    filtered_xlist.append(xlist[i])
            else:
                filtered_sgnfclist.append(sgnfclist[i])
                filtered_xlist.append(xlist[i])
        dict_to_draw[mass]['sgnfc_list']=filtered_sgnfclist
        max_filtered_sgnfc=max(filtered_sgnfclist)
        max_filtered_sgnfclist.append(max_filtered_sgnfc)
        for i in range(len(xlist)):
            sgnfc=filtered_sgnfclist[i]
            if max_filtered_sgnfc == sgnfc:
                score_for_maxsgnfc_list.append(xlist[i])
        #dict_to_draw[mass]['score_for_maxsgnfc_list']=score_for_maxsgnfc_list
    maxscore=max(filtered_xlist)
    
    #width=0.05
    width=1/(Ndiv_orig-1)
    print "width=",width
    Ndiv=int(maxscore/width)

    h=ROOT.TH2D(confname,confname,len(masslist),masslistbin,  Ndiv+1,  -width/2,   maxscore+width/2  )
    for mass in masslist:
        xlist=dict_to_draw[mass]['xlist']
        filtered_sgnfclist=dict_to_draw[mass]['sgnfc_list']
        max_filtered_sgnfc=max(filtered_sgnfclist)
        for i in range(len(xlist)):
            rel_sgnfc=filtered_sgnfclist[i]/max_filtered_sgnfc
            sgnfc=filtered_sgnfclist[i]
            if rel:
                print mass,xlist[i],rel_sgnfc
                h.Fill(mass,xlist[i],rel_sgnfc)
            else:
                h.Fill(mass,xlist[i],sgnfc)
    if AddMaxLine:
        MaxScore=GetMod(score_for_maxsgnfc_list)
        line_maxscore=ROOT.TLine(min(list(masslistbin)),MaxScore,max(list(masslistbin)),MaxScore)   ##TLine (Double_t x1, Double_t y1, Double_t x2, Double_t y2)
        line_maxscore.SetLineColor(2)
        line_maxscore.Draw()
    c=ROOT.TCanvas()
    h.Draw("colz")
    h.SetStats(0)
    #c.SetLogx()
    #c.SetLogz()
    os.system("mkdir -p plots/")
    c.SaveAs("plots/"+confname+suffix+".pdf")
    
    ##DrawMassMaxSgnfc
    ##--Draw TH1D x : mass y : max significance
    gr=ROOT.TGraph(len(masslist),array('d',masslist),array('d',max_filtered_sgnfclist))
    c2=ROOT.TCanvas()
    gr.Draw()
    gr.SetTitle(confname+", S/#sqrt{B}")
    os.system("mkdir -p plots/")
    c2.SaveAs("plots/sgnfc_"+confname+suffix+".pdf")

    ##-DrawMassMaxScore
    ##--Draw TH1D x : mass y : max significance
    #score_for_maxsgnfc_list
    gr=ROOT.TGraph(len(masslist),array('d',masslist),array('d',score_for_maxsgnfc_list))
    c3=ROOT.TCanvas()
    gr.Draw()
    gr.SetTitle(confname+", DNN Score maximizing S/#sqrt(B)")
    os.system("mkdir -p plots/")
    c3.SaveAs("plots/maxdnnpoint_"+confname+suffix+".pdf")


if __name__ == '__main__':
    confpath="config/config_v2.py"
    conflist=['Boosted2016','Boosted2017','Boosted2018']+['Resolved2016','Resolved2017','Resolved2018']
    for conf in conflist:
        print conf
        DrawMassDNNscoreSgnfc(conf,confpath,True)
        DrawMassDNNscoreSgnfc(conf,confpath,False)
        DrawMassDNNscoreSgnfc(conf,confpath,True,False)
        DrawMassDNNscoreSgnfc(conf,confpath,False,False)
        #DrawMassMaxScore(conf,confpath)
