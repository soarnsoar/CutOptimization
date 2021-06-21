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

def GetMassList(confname,confpath):
    exec(open(confpath,"r")) ## create myconfig
    return myconfig[confname]['masslist']

def GetSgnfcList(mass,confpath,confname):
    exec(open(confpath,"r")) ## create myconfig
    ##---
    cutname=myconfig[confname]['cutname']
    variablename=myconfig[confname]['variablename']
    bkglist=myconfig[confname]["bkglist"]
    inputpath=myconfig[confname]["inputpath"]
    #GetSignificanceList(mass,inputpath,VariableName,CutName,BKGLIST,DoLowercut=True,isVBFSIG=True)
    xlist,sgnfclist,slist,blist=GetSignificanceList(mass,inputpath,variablename,cutname,bkglist,True,False)
    #print xlist
    #print sgnfclist
    #print slist
    #print blist
    return xlist,sgnfclist,slist,blist
def temp():
    ##--Load Config
    exec(open("config/config_v1.py","r")) ## create myconfig
    ##---Resolved2016
    cutname=myconfig["Resolved2016"]['cutname']
    variablename=myconfig["Resolved2016"]['variablename']
    bkglist=myconfig["Resolved2016"]["bkglist"]
    inputpath=myconfig["Resolved2016"]["inputpath"]
    xlist,sgnfclist,slist,blist=GetSignificanceList(1000,inputpath,variablename,cutname,bkglist,True,False)
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

def DrawMassMEKDscoreSgnfc(confname,confpath,rel=True,filtered=True,AddMaxLine=True): ## rel -> relative significance, filtered -> skip cut  98% of bkg
    suffix=""
    if rel: suffix+="_relsgnfc"
    if filtered: suffix+="_filter0p02"
    ##1) Define TH2D
    #TH2F (const char *name, const char *title, Int_t nbinsx, Double_t xlow, Double_t xup, Int_t nbinsy, Double_t ylow, Double_t yup)
    #confname="Resolved2016"
    #confpath="config/config_temp.py"
    #
    #masslist=[115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 900, 1000, 1500, 2000, 2500, 3000, 4000, 5000]
    masslist=GetMassList(confname,confpath)
    #masslist=[ 200, 210, 230, 250, 270, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 900, 1000, 1500, 2000, 2500, 3000, 4000, 5000]
    masslistbin=[]
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
    #masslistbin=array('d',masslist+[masslist[-1]+1000])
    #print masslistbin
    #h=ROOT.TH2D(confname,confname,len(masslist),masslistbin,21,-0.025,1.025) ##x : mass, y=MEKDscore, z=significance

    score_for_maxsgnfc_list=[]
    filtered_xlist=[]
    Ndiv_orig=0.
    for mass in masslist:
        xlist,sgnfclist,slist,blist=GetSgnfcList(mass,confpath,confname)
        Ndiv_orig=float(len(xlist))
        max_b=max(blist)
        max_s=max(slist)
        filtered_sgnfclist=[]
        for i in range(len(xlist)):
            #print "s eff.->",xlist[i],':',slist[i]/max_s
            #if blist[i]/max_b <0.02 and filtered:
            if (blist[i]/max_b <0.01 or slist[i]/max_s < 0.1) and filtered:
                print xlist[i],mass
                print '--> b decreasing to under 2%',blist[i]/max_b
                print '--> s decreasing to under 10%',slist[i]/max_s
                filtered_sgnfclist.append(0)
            else:
                filtered_sgnfclist.append(sgnfclist[i])
                filtered_xlist.append(xlist[i])
        max_filtered_sgnfc=max(filtered_sgnfclist)
        print "max_filtered_sgnfc=",max_filtered_sgnfc
        for i in range(len(xlist)):
            sgnfc=filtered_sgnfclist[i]
            if max_filtered_sgnfc == sgnfc:
                score_for_maxsgnfc_list.append(xlist[i])

    maxscore=max(filtered_xlist)
    
    #width=0.05
    #print "Ndiv_orig=",Ndiv_orig
    width=1/(Ndiv_orig-1)
    #print 'width=',width
    Ndiv=int(maxscore/width)
    
    h=ROOT.TH2D(confname,confname,len(masslist),masslistbin,  Ndiv+1,  -width/2,   maxscore+width/2  )
    for mass in masslist:
        xlist,sgnfclist,slist,blist=GetSgnfcList(mass,confpath,confname)
        max_s=max(slist)
        max_b=max(blist)
        filtered_sgnfclist=[]
        for i in range(len(xlist)):
            if  (blist[i]/max_b <0.01 or slist[i]/max_s < 0.1) and filtered:
                print xlist[i],mass
                print '--> b decreasing to under 2%',blist[i]/max_b
                print '--> s decreasing to under 10%',slist[i]/max_s
                filtered_sgnfclist.append(0)
            else:
                filtered_sgnfclist.append(sgnfclist[i])
        #print filtered_sgnfclist
        max_filtered_sgnfc=max(filtered_sgnfclist)
        #print max_filtered_sgnfc
        for i in range(len(xlist)):
            rel_sgnfc=filtered_sgnfclist[i]/max_filtered_sgnfc
            sgnfc=filtered_sgnfclist[i]
            if rel:
                h.Fill(mass,xlist[i],rel_sgnfc)
            else:
                h.Fill(mass,xlist[i],sgnfc)
    if AddMaxLine:
        MaxScore=GetMod(score_for_maxsgnfc_list)
        line_maxscore=ROOT.TLine(min(list(masslistbin)),MaxScore,max(list(masslistbin)),MaxScore)   ##TLine (Double_t x1, Double_t y1, Double_t x2, Double_t y2)
        line_maxscore.SetLineColor(2)
    c=ROOT.TCanvas()
    h.Draw("colz")
    line_maxscore.Draw()
    h.SetStats(0)
    #c.SetLogx()
    #c.SetLogz()
    c.SetLogy()
    os.system("mkdir -p plots_mekd/")
    c.SaveAs("plots_mekd/"+confname+suffix+".pdf")

def DrawMassMaxSgnfc(confname,confpath,filtered=True):
    ##--Draw TH1D x : mass y : max significance
    suffix=""
    
    if filtered: suffix+="_filter0p02"

    #masslist=[ 200, 210, 230, 250, 270, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 900, 1000, 1500, 2000, 2500, 3000, 4000, 5000]
    masslist=GetMassList(confname,confpath)
    #h=ROOT.TH1D(confname,confname,len(masslist)-1,masslistbin)
    ##--Use tgraph

    max_filtered_sgnfclist=[]
    for mass in masslist:
        xlist,sgnfclist,slist,blist=GetSgnfcList(mass,confpath,confname)
        max_b=max(blist)
        #print blist
        filtered_sgnfclist=[]
        for i in range(len(xlist)):
            if blist[i]/max_b <0.02 and filtered:
                print xlist[i],'--> decreasing to under 2%',blist[i]/max_b
                filtered_sgnfclist.append(0)
            else:
                filtered_sgnfclist.append(sgnfclist[i])
        max_filtered_sgnfc=max(filtered_sgnfclist)
        max_filtered_sgnfclist.append(max_filtered_sgnfc)
        for i in range(len(xlist)):
            rel_sgnfc=filtered_sgnfclist[i]/max_filtered_sgnfc
            sgnfc=filtered_sgnfclist[i]
            #h.Fill(mass,sgnfc)
    gr=ROOT.TGraph(len(masslist),array('d',masslist),array('d',max_filtered_sgnfclist))
    c=ROOT.TCanvas()
    #h.Draw()
    #h.SetStats(0)
    gr.Draw()
    gr.SetTitle(confname+", S/#sqrt{B}")
    os.system("mkdir -p plots_mekd/")
    c.SaveAs("plots_mekd/sgnfc_"+confname+suffix+".pdf")


def DrawMassMaxScore(confname,confpath,filtered=True):
    ##--Draw TH1D x : mass y : max significance
    suffix=""
    
    if filtered: suffix+="_filter0p02"

    #masslist=[ 200, 210, 230, 250, 270, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 900, 1000, 1500, 2000, 2500, 3000, 4000, 5000]
    masslist=GetMassList(confname,confpath)
    #h=ROOT.TH1D(confname,confname,len(masslist)-1,masslistbin)
    ##--Use tgraph

    max_filtered_scorelist=[]
    for mass in masslist:
        xlist,sgnfclist,slist,blist=GetSgnfcList(mass,confpath,confname)
        max_b=max(blist)
        #print blist
        filtered_sgnfclist=[]
        for i in range(len(xlist)):
            if blist[i]/max_b <0.02 and filtered:
                filtered_sgnfclist.append(0)
            else:
                filtered_sgnfclist.append(sgnfclist[i])
        max_filtered_sgnfc=max(filtered_sgnfclist)
        
        for i in range(len(xlist)):
            rel_sgnfc=filtered_sgnfclist[i]/max_filtered_sgnfc
            sgnfc=filtered_sgnfclist[i]
            if max_filtered_sgnfc==sgnfc:max_filtered_scorelist.append(xlist[i])
            #h.Fill(mass,sgnfc)
    gr=ROOT.TGraph(len(masslist),array('d',masslist),array('d',max_filtered_scorelist))
    c=ROOT.TCanvas()
    #h.Draw()
    #h.SetStats(0)
    gr.Draw()
    gr.SetTitle(confname+", MEKD Score maximizing S/#sqrt(B)")
    os.system("mkdir -p plots_mekd/")
    c.SaveAs("plots_mekd/maxmekdpoint_"+confname+suffix+".pdf")
def temp():
    #confpath="config/config_MEKD_temp.py"
    #confpath="config/config_MEKD_v1.py"
    confpath="config/config_MEKD_v4.py"
    #conflist=['Boosted2016','Boosted2017','Boosted2018']+['Resolved2016','Resolved2017','Resolved2018']
    #conflist=['Boosted2016_M900', 'Boosted2016_M1500',
    #          'Boosted2017_M900', 'Boosted2017_M1500',
    #          'Boosted2018_M900', 'Boosted2018_M1500',
    #          'Resolved2016_M200', 'Resolved2016_M400',
    #          'Resolved2017_M200', 'Resolved2017_M400',
    #          'Resolved2018_M200', 'Resolved2018_M400',

    #          ]

    conflist=['Resolved2016_M400_0.00001','Resolved2016_M400_0.0001','Resolved2016_M400_0.001','Resolved2016_M400_0.01', 'Resolved2016_M400_0.1', 'Resolved2016_M400_1']\
        +['Resolved2016_M200_0.00001','Resolved2016_M200_0.0001','Resolved2016_M200_0.001','Resolved2016_M200_0.01', 'Resolved2016_M200_0.1', 'Resolved2016_M200_1']
    for conf in conflist:
        print conf
        DrawMassMEKDscoreSgnfc(conf,confpath,True)
        DrawMassMEKDscoreSgnfc(conf,confpath,False)
        DrawMassMEKDscoreSgnfc(conf,confpath,True,False)
        DrawMassMEKDscoreSgnfc(conf,confpath,False,False)
        DrawMassMaxScore(conf,confpath)

if __name__ == '__main__':
    confpath=sys.argv[1]
    conf=sys.argv[2]
    DrawMassMEKDscoreSgnfc(conf,confpath,True)
    DrawMassMEKDscoreSgnfc(conf,confpath,False)
    DrawMassMEKDscoreSgnfc(conf,confpath,True,False)
    DrawMassMEKDscoreSgnfc(conf,confpath,False,False)
    DrawMassMaxScore(conf,confpath)
    
    
