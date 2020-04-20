--- .simpcvs/copy/hkvc-covid-toolkit.py	2020-03-28 23:44:51.874133070 +0530
+++ hkvc-covid-toolkit.py	2020-03-28 23:45:29.246133861 +0530
@@ -170,7 +170,7 @@
     dataList = [ 'pop' ]
     tdCP = _load_csv(sFile, csvIndex, keyList, dataList, bDataListInKey=False)
     dCP = {}
-    lCCMissing = {}
+    lCCMissing = []
     for k in tdCP:
         tS = k
         atS = tS.split('-')
