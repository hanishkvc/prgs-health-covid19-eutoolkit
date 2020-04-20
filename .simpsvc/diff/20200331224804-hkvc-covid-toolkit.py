--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-03-31 21:53:11.193187508 +0530
+++ hkvc-covid-toolkit.py	2020-03-31 22:47:44.595256775 +0530
@@ -291,12 +291,12 @@
     for data in datas:
         thePlt.plot(data,"o-", label=msgs[i])
         i += 1
-    thePlt.grid()
     thePlt.set_xscale(xscale)
     thePlt.set_yscale(yscale)
     if title != None:
         thePlt.set_title(title)
     thePlt.legend()
+    thePlt.grid()
 
 
 def calc_mortalityrate(lCC, lDC):
@@ -425,29 +425,27 @@
             fig,axes = plt.subplots(1)
             iPltRows = 1
             iPltCols = 1
+            figWidth = 12
+            figHeight = 8
         else:
             iPltRows = len(geoIds)
             iPltCols = len(dataTypes)
             fig,axes = plt.subplots(iPltRows, iPltCols)
+            figWidth = 12*iPltCols
+            figHeight = 8*iPltRows
     else:
         fig,axes = plt.subplots(iPltRows, iPltCols)
+        figWidth = 12*iPltCols
+        figHeight = 8*iPltRows
     if bFigSizeSetup:
-        figWidth = 4*iPltRows
-        figHeight = 4*iPltCols
-        bReAdjustFigSize = False
-        if figWidth < 20:
-            figWidth = 20
-        else:
-            bReAdjustFigSize = True
-        if figHeight < 20:
-            figHeight = 20
-        else:
-            bReAdjustFigSize = True
-        if bReAdjustFigSize:
-            if figWidth > figHeight:
-                figWidth = int(figHeight*0.3)
-            else:
-                figHeight = int(figWidth*0.3)
+        print("Pre:figWidth: {}, figHeight: {}".format(figWidth, figHeight))
+        widthThres = int(figHeight*2)
+        heightThres = int(figWidth*2)
+        if figWidth > widthThres:
+            figWidth = widthThres
+        if figHeight > heightThres:
+            figHeight = heightThres
+        input("Post:figWidth: {}, figHeight: {}".format(figWidth, figHeight))
         fig.set_figwidth(figWidth)
         fig.set_figheight(figHeight)
     lAllC = []
@@ -525,6 +523,7 @@
         thePlt.set_yscale("log")
         thePlt.set_xticklabels(geoIds)
         thePlt.set_title("Cases/Day")
+        thePlt.grid()
         thePltL1, axesId = plt_getl1(axes, axesId)
         print("axesId",axesId)
         pltId = 0
@@ -533,6 +532,7 @@
         thePlt.set_yscale("log")
         thePlt.set_xticklabels(geoIds)
         thePlt.set_title("CasesRel2Pop/Day")
+        thePlt.grid()
         # thePlt.boxplot(lAllC, 0, '') # No outliers
     if "DeathBox" in dataTypes:
         thePltL1, axesId = plt_getl1(axes, axesId)
@@ -541,6 +541,7 @@
         thePlt.boxplot(lAllD)
         thePlt.set_yscale("log")
         thePlt.set_xticklabels(geoIds)
+        thePlt.grid()
         # thePlt.boxplot(lAllC, 0, '') # No outliers
     if sTitle != None:
         plt.title(sTitle)
