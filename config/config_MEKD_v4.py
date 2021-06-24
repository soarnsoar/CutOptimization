#[ 200, 210, 230, 250, 270, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 900, 1000, 1500, 2000, 2500, 3000, 4000, 5000]
myconfig={
    ##---2016 Boosted
    "Boosted2016_M1500_0.01":{
        "cutname":"__BoostedALL_SR_NoMEKDCut",
        "variablename":"MEKD_Bst_C_0.01_M1500",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2016//rootFile_2016__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Boosted_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        #'masslist':[800,900,1000, 1500, 2000, 2500, 3000, 4000, 5000]
        'masslist':[ 1500, 2000, 2500, 3000, 4000, 5000]
    },

    "Boosted2016_M900_0.01":{
        "cutname":"__BoostedALL_SR_NoMEKDCut",
        "variablename":"MEKD_Bst_C_0.01_M900",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2016//rootFile_2016__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Boosted_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 800,900,1000,1500, 2000, 2500, 3000, 4000, 5000]
    },

    "Boosted2016_M400_0.01":{
        "cutname":"__BoostedALL_SR_NoMEKDCut",
        "variablename":"MEKD_Bst_C_0.01_M400",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2016//rootFile_2016__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Boosted_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 800,900,1000,1500, 2000, 2500, 3000, 4000, 5000]
    },
    
    #115 120 124 125 126 130 140 145 150 155 160 165 170 180 190
    #0.00001, 0.0001, 0.001

    "Resolved2016_M400_0.00001":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.00001_M400",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2016//rootFile_2016__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },

    "Resolved2016_M200_0.00001":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.00001_M200",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2016//rootFile_2016__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },


    "Resolved2016_M400_0.0001":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.0001_M400",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2016//rootFile_2016__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },

    "Resolved2016_M200_0.0001":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.0001_M200",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2016//rootFile_2016__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },


    "Resolved2016_M400_0.001":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.001_M400",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2016//rootFile_2016__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },

    "Resolved2016_M200_0.001":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.001_M200",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2016//rootFile_2016__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },

    
    "Resolved2016_M400_0.01":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.01_M400",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2016//rootFile_2016__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },

    "Resolved2016_M200_0.01":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.01_M200",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2016//rootFile_2016__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },




    "Resolved2016_M400_0.1":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.1_M400",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2016//rootFile_2016__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },

    "Resolved2016_M200_0.1":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.1_M200",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2016//rootFile_2016__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },

    "Resolved2016_M400_1":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_1_M400",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2016//rootFile_2016__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },

    "Resolved2016_M200_1":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_1_M200",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2016//rootFile_2016__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },


    ##---2017 Boosted                                                                                                                                                                                       
    "Boosted2017_M1500_0.01":{
        "cutname":"__BoostedALL_SR_NoMEKDCut",
        "variablename":"MEKD_Bst_C_0.01_M1500",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2017//rootFile_2017__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Boosted_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 1500, 2000, 2500, 3000, 4000, 5000]
    },

    "Boosted2017_M900_0.01":{
        "cutname":"__BoostedALL_SR_NoMEKDCut",
        "variablename":"MEKD_Bst_C_0.01_M900",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2017//rootFile_2017__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Boosted_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 800,900,1000,1500, 2000, 2500, 3000, 4000, 5000]
    },

    "Boosted2017_M400_0.01":{
        "cutname":"__BoostedALL_SR_NoMEKDCut",
        "variablename":"MEKD_Bst_C_0.01_M400",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2017//rootFile_2017__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Boosted_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 800,900,1000,1500, 2000, 2500, 3000, 4000, 5000]
    },

    #

    "Resolved2017_M400_0.00001":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.00001_M400",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2017//rootFile_2017__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },

    "Resolved2017_M200_0.00001":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.00001_M200",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2017//rootFile_2017__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },


    "Resolved2017_M400_0.0001":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.0001_M400",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2017//rootFile_2017__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },

    "Resolved2017_M200_0.0001":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.0001_M200",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2017//rootFile_2017__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },


    "Resolved2017_M400_0.001":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.001_M400",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2017//rootFile_2017__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },

    "Resolved2017_M200_0.001":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.001_M200",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2017//rootFile_2017__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },

    
    "Resolved2017_M400_0.01":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.01_M400",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2017//rootFile_2017__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },

    "Resolved2017_M200_0.01":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.01_M200",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2017//rootFile_2017__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },



    
    "Resolved2017_M400_0.1":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.1_M400",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2017//rootFile_2017__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },

    "Resolved2017_M200_0.1":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.1_M200",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2017//rootFile_2017__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },

    "Resolved2017_M400_1":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_1_M400",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2017//rootFile_2017__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },

    "Resolved2017_M200_1":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_1_M200",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2017//rootFile_2017__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },



    ##---2018 Boosted                                                                                                                                                                                       
    "Boosted2018_M1500_0.01":{
        "cutname":"__BoostedALL_SR_NoMEKDCut",
        "variablename":"MEKD_Bst_C_0.01_M1500",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2018//rootFile_2018__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Boosted_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 1500, 2000, 2500, 3000, 4000, 5000]
    },

    "Boosted2018_M900_0.01":{
        "cutname":"__BoostedALL_SR_NoMEKDCut",
        "variablename":"MEKD_Bst_C_0.01_M900",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2018//rootFile_2018__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Boosted_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 800,900,1000,1500, 2000, 2500, 3000, 4000, 5000]
    },

    "Boosted2018_M400_0.01":{
        "cutname":"__BoostedALL_SR_NoMEKDCut",
        "variablename":"MEKD_Bst_C_0.01_M400",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2018//rootFile_2018__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Boosted_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 800,900,1000,1500, 2000, 2500, 3000, 4000, 5000]
    },




    "Resolved2018_M400_0.00001":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.00001_M400",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2018//rootFile_2018__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },

    "Resolved2018_M200_0.00001":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.00001_M200",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2018//rootFile_2018__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },


    "Resolved2018_M400_0.0001":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.0001_M400",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2018//rootFile_2018__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },

    "Resolved2018_M200_0.0001":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.0001_M200",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2018//rootFile_2018__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },


    "Resolved2018_M400_0.001":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.001_M400",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2018//rootFile_2018__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },

    "Resolved2018_M200_0.001":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.001_M200",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2018//rootFile_2018__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },

    
    "Resolved2018_M400_0.01":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.01_M400",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2018//rootFile_2018__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },

    "Resolved2018_M200_0.01":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.01_M200",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2018//rootFile_2018__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },



    
    "Resolved2018_M400_0.1":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.1_M400",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2018//rootFile_2018__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },

    "Resolved2018_M200_0.1":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_0.1_M200",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2018//rootFile_2018__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },

    "Resolved2018_M400_1":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_1_M400",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2018//rootFile_2018__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },

    "Resolved2018_M200_1":{
        "cutname":"___ResolvedALL__SR_NoMEKDCut",
        "variablename":"MEKD_Res_C_1_M200",
        "bkglist":[ 'DY', 'MultiBoson', 'qqWWqq', 'TT','tW','SingleTop','Wjets0j','Wjets1j','Wjets2j','ggWW','QCD','WW','ZHWWlnuqq_M125','WmHWWlnuqq_M125','WpHWWlnuqq_M125','qqH_hww','ggH_hww'],
        "inputpath":"../2018//rootFile_2018__cms_scratch_jhchoi_AN_PLOT_v3_VBFDNN_Opt_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root",
        'masslist':[ 115, 120, 124, 125, 126, 130, 140, 145, 150, 155, 160, 165, 170, 180, 190, 200, 210, 230, 250, 270, 300, 350, 400, 450 ],
    },




}
