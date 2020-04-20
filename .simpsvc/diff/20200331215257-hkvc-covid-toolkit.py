--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-03-30 00:46:50.873015061 +0530
+++ hkvc-covid-toolkit.py	2020-03-31 21:50:20.802183903 +0530
@@ -417,6 +417,7 @@
     return dD2
 
 
+bFigSizeSetup=True
 def plot_what(dD, dD2, geoIds = ['IN', 'UK', 'CN'], dataTypes = [ "Cases", "CasesCumu", "Death" ], iDS=1, iMS=1, iDE=31, iME=12, iY=2020, bSingle=True, sTitle=None, iPltRows=None, iPltCols=None):
     axesId = 0
     if (iPltRows == None) or (iPltCols == None):
@@ -430,10 +431,23 @@
             fig,axes = plt.subplots(iPltRows, iPltCols)
     else:
         fig,axes = plt.subplots(iPltRows, iPltCols)
+    if bFigSizeSetup:
     figWidth = 4*iPltRows
     figHeight = 4*iPltCols
-    figWidth = 16
-    figHeight = 16
+        bReAdjustFigSize = False
+        if figWidth < 20:
+            figWidth = 20
+        else:
+            bReAdjustFigSize = True
+        if figHeight < 20:
+            figHeight = 20
+        else:
+            bReAdjustFigSize = True
+        if bReAdjustFigSize:
+            if figWidth > figHeight:
+                figWidth = int(figHeight*0.3)
+            else:
+                figHeight = int(figWidth*0.3)
     fig.set_figwidth(figWidth)
     fig.set_figheight(figHeight)
     lAllC = []
