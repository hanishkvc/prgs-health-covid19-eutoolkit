--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-03-29 20:11:24.345273536 +0530
+++ hkvc-covid-toolkit.py	2020-03-29 21:04:55.754223310 +0530
@@ -380,21 +380,30 @@
     return thePltL2, pltId+1
 
 
-def plot_what(dD, geoIds = ['IN', 'UK', 'CN'], dataTypes = [ "Cases", "CasesCumu", "Death" ], iDS=1, iMS=1, iDE=31, iME=12, iY=2020, bSingle=True, sTitle=None):
+def plot_what(dD, geoIds = ['IN', 'UK', 'CN'], dataTypes = [ "Cases", "CasesCumu", "Death" ], iDS=1, iMS=1, iDE=31, iME=12, iY=2020, bSingle=True, sTitle=None, iPltRows=None, iPltCols=None):
     axesId = 0
+    if (iPltRows == None) or (iPltCols == None):
     if bSingle:
         fig,axes = plt.subplots(1)
     else:
         fig,axes = plt.subplots(len(geoIds), len(dataTypes))
+    else:
+        fig,axes = plt.subplots(iPltRows, iPltCols)
     #fig,axes = plt.subplots(len(geoIds))
     #fig,axes = plt.subplots(1)
     #fig,axes = plt.subplots(1,2)
     fig.set_figwidth(2*len(geoIds))
     fig.set_figheight(8*len(dataTypes))
     lAllC = []
+    lAllCP = []
     lAllD = []
+    lAllDP = []
     for geoId in geoIds:
         lC, lD, sRange = get_covid_data(dD, geoId, iDS, iMS, iDE, iME, iY)
+        lCP = calc_relative2pop(lC, geoId, dCP2010)
+        lDP = calc_relative2pop(lD, geoId, dCP2010)
+        lAllCP.append(lCP)
+        lAllDP.append(lDP)
         lAllC.append(lC)
         lAllD.append(lD)
         lCC = calc_cumulatelist(lC)
@@ -412,7 +421,7 @@
         print("theDeathData:{}:{}".format(len(lD), lD))
         print("theDeathCumuData:{}:{}".format(len(lDC), lDC))
         print("CasesCumu/Pop:{}\nDeathCumu/Pop:{}".format(lCC[-1]/dCP2010[geoId], lDC[-1]/dCP2010[geoId]))
-        print("0.06% of Pop:{}".format(dCP2010[geoId]*0.0006))
+        print("1.0% of Pop:{}".format(dCP2010[geoId]*0.01))
         thePltL1, axesId = plt_getl1(axes, axesId)
         pltId = 0
         if "Cases" in dataTypes:
@@ -455,12 +464,24 @@
             thePlt, pltId = plt_getl2(thePltL1, pltId)
             plot_data(thePlt, [lMR], ["MortalityRate "+sRange])
     if "CasesBox" in dataTypes:
+        axesId = 0
+        print("axesId",axesId)
         thePltL1, axesId = plt_getl1(axes, axesId)
+        print("axesId",axesId)
         pltId = 0
         thePlt, pltId = plt_getl2(thePltL1, pltId)
         thePlt.boxplot(lAllC)
         thePlt.set_yscale("log")
         thePlt.set_xticklabels(geoIds)
+        thePlt.set_title("Cases/Day")
+        thePltL1, axesId = plt_getl1(axes, axesId)
+        print("axesId",axesId)
+        pltId = 0
+        thePlt, pltId = plt_getl2(thePltL1, pltId)
+        thePlt.boxplot(lAllCP)
+        thePlt.set_yscale("log")
+        thePlt.set_xticklabels(geoIds)
+        thePlt.set_title("CasesRel2Pop/Day")
         # thePlt.boxplot(lAllC, 0, '') # No outliers
     if "DeathBox" in dataTypes:
         thePltL1, axesId = plt_getl1(axes, axesId)
@@ -514,7 +535,8 @@
     geoIds = [ 'IN', 'CA', 'UK' ]
     geoIds = [ 'IN', 'CA', 'UK', 'ES', 'FR', 'US', 'IT', 'CN' ]
     dataTypes = [ "CasesBox" ]
-    plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True, sTitle="Cases/Day")
+    #plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True, sTitle="Cases/Day")
+    plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True, iPltRows=2, iPltCols=1)
     dataTypes = [ "DeathBox" ]
     plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True, sTitle="Death/Day")
 
@@ -522,6 +544,6 @@
 iMS = 1
 iDE = 31
 iME = 3
-do_plots(dD)
+#do_plots(dD)
 do_boxplot(dD)
 
