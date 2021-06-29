##options in ExportShellCondorSetup.py

#   parser.add_option("-c","--command",   dest="command", help="command to run")
#   parser.add_option("-d","--workdir",   dest="workdir", help="workarea")
#   parser.add_option("-n","--jobname",   dest="jobname", help="jobname")
#   parser.add_option("-m","--ncpu",   dest="ncpu", help="number of multicores",default=1)
#   parser.add_option("-s","--submit",   dest="submit",action="store_true", help="submit",default=False)



CURDIR=`pwd`
#Resolved2016_M400_0.00001
CONFFILE=config/config_MEKD_v4.py
ARR_CONF=(

Boosted2016_M1500_0.01
Boosted2016_M900_0.01
Boosted2016_M400_0.01

Boosted2017_M1500_0.01
Boosted2017_M900_0.01
Boosted2017_M400_0.01

Boosted2018_M1500_0.01
Boosted2018_M900_0.01
Boosted2018_M400_0.01

Resolved2016_M400_0.00001
Resolved2016_M400_0.0001
Resolved2016_M400_0.001
Resolved2016_M400_0.01
Resolved2016_M400_0.1

Resolved2016_M200_0.00001
Resolved2016_M200_0.0001
Resolved2016_M200_0.001
Resolved2016_M200_0.01
Resolved2016_M200_0.1

#2017
Resolved2017_M400_0.00001
Resolved2017_M400_0.0001
Resolved2017_M400_0.001
Resolved2017_M400_0.01
Resolved2017_M400_0.1

Resolved2017_M200_0.00001
Resolved2017_M200_0.0001
Resolved2017_M200_0.001
Resolved2017_M200_0.01
Resolved2017_M200_0.1

##2018
Resolved2018_M400_0.00001
Resolved2018_M400_0.0001
Resolved2018_M400_0.001
Resolved2018_M400_0.01
Resolved2018_M400_0.1

Resolved2018_M200_0.00001
Resolved2018_M200_0.0001
Resolved2018_M200_0.001
Resolved2018_M200_0.01
Resolved2018_M200_0.1

)


for CONF in ${ARR_CONF[@]};do

    python python_tool/ExportShellCondorSetup.py -c "cd ${CURDIR};python run_MEKD.py ${CONFFILE} ${CONF}" -d WORKDIR/${CONF} -n WORKDIR/${CONF} -m 1 -s True

done
