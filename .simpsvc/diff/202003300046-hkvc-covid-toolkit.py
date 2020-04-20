--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-03-29 23:55:52.439062895 +0530
+++ hkvc-covid-toolkit.py	2020-03-30 00:42:14.577019383 +0530
@@ -407,6 +407,8 @@
         print("theCasesData:{}:{}".format(len(dD2['C'][geoId]), dD2['C'][geoId]))
         print("theCasesCumuData:{}:{}".format(len(dD2['CC'][geoId]), dD2['CC'][geoId]))
         print("theCasesDeltaData:{}:{}".format(len(dD2['CD'][geoId]), dD2['CD'][geoId]))
+        print("theCasesMovAvg:{}:{}".format(len(dD2['CM'][geoId]), dD2['CM'][geoId]))
+        print("theCasesMovAvrRel:{}:{}".format(len(dD2['CMR'][geoId]), dD2['CMR'][geoId]))
         print("theDeathData:{}:{}".format(len(dD2['D'][geoId]), dD2['D'][geoId]))
         print("theDeathCumuData:{}:{}".format(len(dD2['DC'][geoId]), dD2['DC'][geoId]))
         print("CasesCumu/Pop:{}\nDeathCumu/Pop:{}".format(dD2['CC'][geoId][-1]/dCP2010[geoId], dD2['DC'][geoId][-1]/dCP2010[geoId]))
@@ -420,12 +422,20 @@
     if (iPltRows == None) or (iPltCols == None):
         if bSingle:
             fig,axes = plt.subplots(1)
+            iPltRows = 1
+            iPltCols = 1
         else:
-            fig,axes = plt.subplots(len(geoIds), len(dataTypes))
+            iPltRows = len(geoIds)
+            iPltCols = len(dataTypes)
+            fig,axes = plt.subplots(iPltRows, iPltCols)
     else:
         fig,axes = plt.subplots(iPltRows, iPltCols)
-    fig.set_figwidth(2*len(geoIds))
-    fig.set_figheight(8*len(dataTypes))
+    figWidth = 4*iPltRows
+    figHeight = 4*iPltCols
+    figWidth = 16
+    figHeight = 16
+    fig.set_figwidth(figWidth)
+    fig.set_figheight(figHeight)
     lAllC = []
     lAllCP = []
     lAllD = []
@@ -520,7 +530,8 @@
         # thePlt.boxplot(lAllC, 0, '') # No outliers
     if sTitle != None:
         plt.title(sTitle)
-    fig.savefig("/tmp/covid.png", bbox_inches="tight")
+    sImgFile = "/tmp/{}-covid.png".format(time.strftime("%Y%m%d%H%M%S"))
+    fig.savefig(sImgFile, bbox_inches="tight")
     plt.margins(0,0)
     plt.show()
     return dD2
