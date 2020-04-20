--- .simpcvs/copy/hkvc-covid-toolkit.py	2020-03-29 00:36:08.127198166 +0530
+++ hkvc-covid-toolkit.py	2020-03-29 00:48:01.856213269 +0530
@@ -367,7 +367,7 @@
     return thePltL2, pltId+1
 
 
-def plot_what(dD, geoIds = ['IN', 'UK', 'CN'], dataTypes = [ "Cases", "CasesCumu", "Death" ], iDS=1, iMS=1, iDE=31, iME=12, iY=2020, bSingle=True):
+def plot_what(dD, geoIds = ['IN', 'UK', 'CN'], dataTypes = [ "Cases", "CasesCumu", "Death" ], iDS=1, iMS=1, iDE=31, iME=12, iY=2020, bSingle=True, sTitle=None):
     axesId = 0
     if bSingle:
         fig,axes = plt.subplots(1)
@@ -388,6 +388,7 @@
         lCD = calc_deltalist(lC)
         lCR = calc_relativelist(lC)
         lCM = calc_movingavglist(lC)
+        lCMR = calc_relativelist(lCM)
         lDC = calc_cumulatelist(lD)
         lDM = calc_movingavglist(lD)
         lMR = calc_mortalityrate(lCC, lDC)
@@ -405,6 +406,9 @@
         if "CasesMovAvg" in dataTypes:
             thePlt, pltId = plt_getl2(thePltL1, pltId)
             plot_data(thePlt, [lCM], ["CasesMovAvg "+sRange])
+        if "CasesMovAvgRel" in dataTypes:
+            thePlt, pltId = plt_getl2(thePltL1, pltId)
+            plot_data(thePlt, [lCMR], ["CasesMovAvgRel "+sRange])
         if "CasesRelative" in dataTypes:
             thePlt, pltId = plt_getl2(thePltL1, pltId)
             plot_data(thePlt, [lCR], ["CasesRelative "+sRange])
@@ -451,6 +455,8 @@
         thePlt.set_yscale("log")
         thePlt.set_xticklabels(geoIds)
         # thePlt.boxplot(lAllC, 0, '') # No outliers
+    if sTitle != None:
+        plt.title(sTitle)
     fig.savefig("/tmp/covid.png", bbox_inches="tight")
     plt.margins(0,0)
     plt.show()
@@ -476,6 +482,9 @@
     dataTypes = [ "CasesMovAvgPlus", "CasesCumu", "Death", "DeathCumu" ]
     dataTypes = [ "CasesMovAvgPlus", "CasesCumu", "DeathCumu", "MortalityRate" ]
     plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=False)
+    dataTypes = [ "CasesMovAvgRel" ]
+    geoIds = [ 'IN', 'CA', 'UK', 'ES', 'FR', 'US', 'IT', 'CN' ]
+    plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True)
     dataTypes = [ "MortalityRate" ]
     geoIds = [ 'IN', 'CA', 'UK', 'ES', 'FR', 'US', 'IT', 'CN' ]
     plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True)
@@ -490,9 +499,9 @@
     geoIds = [ 'IN', 'CA', 'UK' ]
     geoIds = [ 'IN', 'CA', 'UK', 'ES', 'FR', 'US', 'IT', 'CN' ]
     dataTypes = [ "CasesBox" ]
-    plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True)
+    plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True, sTitle="Cases/Day")
     dataTypes = [ "DeathBox" ]
-    plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True)
+    plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True, sTitle="Death/Day")
 
 iDS = 20
 iMS = 1
