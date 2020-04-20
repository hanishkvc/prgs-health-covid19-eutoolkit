--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-03-31 22:49:32.489259058 +0530
+++ hkvc-covid-toolkit.py	2020-03-31 22:53:59.364264706 +0530
@@ -296,7 +296,7 @@
     if title != None:
         thePlt.set_title(title)
     thePlt.legend()
-    thePlt.grid()
+    thePlt.grid(True)
 
 
 def calc_mortalityrate(lCC, lDC):
@@ -523,7 +523,7 @@
         thePlt.set_yscale("log")
         thePlt.set_xticklabels(geoIds)
         thePlt.set_title("Cases/Day")
-        thePlt.grid()
+        thePlt.grid(True)
         thePltL1, axesId = plt_getl1(axes, axesId)
         print("axesId",axesId)
         pltId = 0
@@ -532,7 +532,7 @@
         thePlt.set_yscale("log")
         thePlt.set_xticklabels(geoIds)
         thePlt.set_title("CasesRel2Pop/Day")
-        thePlt.grid()
+        thePlt.grid(True)
         # thePlt.boxplot(lAllC, 0, '') # No outliers
     if "DeathBox" in dataTypes:
         thePltL1, axesId = plt_getl1(axes, axesId)
@@ -541,7 +541,7 @@
         thePlt.boxplot(lAllD)
         thePlt.set_yscale("log")
         thePlt.set_xticklabels(geoIds)
-        thePlt.grid()
+        thePlt.grid(True)
         # thePlt.boxplot(lAllC, 0, '') # No outliers
     if sTitle != None:
         plt.title(sTitle)
