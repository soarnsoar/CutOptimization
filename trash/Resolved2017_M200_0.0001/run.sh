#!/bin/bash
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
export SCRAM_ARCH=slc7_amd64_gcc700
source $VO_CMS_SW_DIR/cmsset_default.sh
cd /cms/ldap_home/jhchoi/HWW_Analysis/slc7/ForShape/CMSSW_10_2_19
eval `scramv1 ru -sh`
cd /cms_scratch/jhchoi/AN_PLOT_v3_VBFDNN_Opt/CutOptimization/WORKDIR/Resolved2017_M200_0.0001
(cd /cms_scratch/jhchoi/AN_PLOT_v3_VBFDNN_Opt/CutOptimization;python run_MEKD.py config/config_MEKD_v4.py Resolved2017_M200_0.0001)
myerr=$?
ntry=1
echo "myerr=$myerr"
while [ $myerr -ne 0 ]
do
ntry=`expr $ntry + 1`
(cd /cms_scratch/jhchoi/AN_PLOT_v3_VBFDNN_Opt/CutOptimization;python run_MEKD.py config/config_MEKD_v4.py Resolved2017_M200_0.0001)
myerr=$?
echo ntry="$ntry"
echo "myerr=$myerr"
if [ $ntry -gt 3 ]
then
break
fi
done
echo "[ntry=$ntry]"
if [ $myerr -eq 0 ]
then
mv /cms_scratch/jhchoi/AN_PLOT_v3_VBFDNN_Opt/CutOptimization/WORKDIR/Resolved2017_M200_0.0001/run.jid /cms_scratch/jhchoi/AN_PLOT_v3_VBFDNN_Opt/CutOptimization/WORKDIR/Resolved2017_M200_0.0001/run.done
fi
