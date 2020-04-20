--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-03-29 22:57:00.628118133 +0530
+++ hkvc-covid-toolkit.py	2020-03-29 23:00:58.447114413 +0530
@@ -524,6 +524,7 @@
     fig.savefig("/tmp/covid.png", bbox_inches="tight")
     plt.margins(0,0)
     plt.show()
+    return dD2
 
 
 download_data_ts()
@@ -533,8 +534,9 @@
 input("CountryCodes: {}\nPress any key...".format(dCC))
 dCP,dCP2010 = load_csv_pop(sys.argv[2])
 input("CountryPopulation:2010: {}\nPress any key...".format(dCP2010))
+dD2 = None
 
-def do_plots(dD):
+def do_plots(dD, dD2):
     geoIds = [ 'IN', 'US', 'CA', 'IT', 'CN' ]
     geoIds = [ 'IN', 'US', 'CA', 'IT' ]
     geoIds = [ 'IN', 'CA', 'UK', 'CN' ]
@@ -545,33 +547,35 @@
     dataTypes = [ "CasesMovAvgPlus", "Death", "DeathCumu" ]
     dataTypes = [ "CasesMovAvgPlus", "CasesCumu", "Death", "DeathCumu" ]
     dataTypes = [ "CasesMovAvgPlus", "CasesCumu", "DeathCumu", "MortalityRate" ]
-    plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=False)
+    dD2 = plot_what(dD, dD2, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=False)
     dataTypes = [ "CasesMovAvgRel" ]
     geoIds = [ 'IN', 'CA', 'UK', 'ES', 'FR', 'US', 'IT', 'CN' ]
-    plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True)
+    dD2 = plot_what(dD, dD2, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True)
     dataTypes = [ "MortalityRate" ]
     geoIds = [ 'IN', 'CA', 'UK', 'ES', 'FR', 'US', 'IT', 'CN' ]
-    plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True)
+    dD2 = plot_what(dD, dD2, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True)
     dataTypes = [ "CasesRelative" ]
     geoIds = [ 'IN', 'CA', 'UK', 'ES', 'FR', 'US', 'IT', 'CN' ]
-    plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True)
+    dD2 = plot_what(dD, dD2, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True)
     dataTypes = [ "CasesRelative", "MortalityRate" ]
     geoIds = [ 'IN', 'CA', 'UK', 'ES', 'FR', 'US', 'IT', 'CN' ]
-    plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=False)
+    dD2 = plot_what(dD, dD2, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=False)
+    return dD2
 
-def do_boxplot(dD):
+def do_boxplot(dD, dD2):
     geoIds = [ 'IN', 'CA', 'UK' ]
     geoIds = [ 'IN', 'CA', 'UK', 'ES', 'FR', 'US', 'IT', 'CN' ]
     dataTypes = [ "CasesBox" ]
     #plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True, sTitle="Cases/Day")
-    plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True, iPltRows=2, iPltCols=1)
+    dD2 = plot_what(dD, dD2, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True, iPltRows=2, iPltCols=1)
     dataTypes = [ "DeathBox" ]
-    plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True, sTitle="Death/Day")
+    dD2 = plot_what(dD, dD2, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True, sTitle="Death/Day")
+    return dD2
 
 iDS = 20
 iMS = 1
 iDE = 31
 iME = 3
-#do_plots(dD)
-do_boxplot(dD)
+#dD2 = do_plots(dD, dD2)
+dD2 = do_boxplot(dD, dD2)
 
