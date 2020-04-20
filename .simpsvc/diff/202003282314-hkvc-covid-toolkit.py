--- .simpcvs/copy/hkvc-covid-toolkit.py	2020-03-28 18:15:50.879715339 +0530
+++ hkvc-covid-toolkit.py	2020-03-28 23:12:50.571092414 +0530
@@ -352,7 +352,7 @@
     return thePltL2, pltId+1
 
 
-def plot_what(geoIds = ['IN', 'UK', 'CN'], dataTypes = [ "Cases", "CasesCumu", "Death" ], iDS=1, iMS=1, iDE=31, iME=12, iY=2020, bSingle=True):
+def plot_what(dD, geoIds = ['IN', 'UK', 'CN'], dataTypes = [ "Cases", "CasesCumu", "Death" ], iDS=1, iMS=1, iDE=31, iME=12, iY=2020, bSingle=True):
     axesId = 0
     if bSingle:
         fig,axes = plt.subplots(1)
@@ -366,7 +366,7 @@
     lAllC = []
     lAllD = []
     for geoId in geoIds:
-        lC, lD, sRange = get_covid_data(geoId, iDS, iMS, iDE, iME, iY)
+        lC, lD, sRange = get_covid_data(dD, geoId, iDS, iMS, iDE, iME, iY)
         lAllC.append(lC)
         lAllD.append(lD)
         lCC = calc_cumulatelist(lC)
@@ -448,7 +448,7 @@
 dCP = load_csv_pop(sys.argv[2])
 print(dCP)
 
-def do_plots():
+def do_plots(dD):
     geoIds = [ 'IN', 'US', 'CA', 'IT', 'CN' ]
     geoIds = [ 'IN', 'US', 'CA', 'IT' ]
     geoIds = [ 'IN', 'CA', 'UK', 'US', 'CN' ]
@@ -459,29 +459,29 @@
     dataTypes = [ "CasesMovAvgPlus", "Death", "DeathCumu" ]
     dataTypes = [ "CasesMovAvgPlus", "CasesCumu", "Death", "DeathCumu" ]
     dataTypes = [ "CasesMovAvgPlus", "CasesCumu", "DeathCumu", "MortalityRate" ]
-    plot_what(geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=False)
+    plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=False)
     dataTypes = [ "MortalityRate" ]
     geoIds = [ 'IN', 'CA', 'UK', 'ES', 'FR', 'US', 'IT', 'CN' ]
-    plot_what(geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True)
+    plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True)
     dataTypes = [ "CasesRelative" ]
     geoIds = [ 'IN', 'CA', 'UK', 'ES', 'FR', 'US', 'IT', 'CN' ]
-    plot_what(geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True)
+    plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True)
     dataTypes = [ "CasesRelative", "MortalityRate" ]
     geoIds = [ 'IN', 'CA', 'UK', 'ES', 'FR', 'US', 'IT', 'CN' ]
-    plot_what(geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=False)
+    plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=False)
 
-def do_boxplot():
+def do_boxplot(dD):
     geoIds = [ 'IN', 'CA', 'UK' ]
     geoIds = [ 'IN', 'CA', 'UK', 'ES', 'FR', 'US', 'IT', 'CN' ]
     dataTypes = [ "CasesBox" ]
-    plot_what(geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True)
+    plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True)
     dataTypes = [ "DeathBox" ]
-    plot_what(geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True)
+    plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True)
 
 iDS = 20
 iMS = 1
 iDE = 31
 iME = 3
-do_plots()
-do_boxplot()
+do_plots(dD)
+do_boxplot(dD)
 
