--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-03-29 02:35:09.348349278 +0530
+++ hkvc-covid-toolkit.py	2020-03-29 20:08:46.123276011 +0530
@@ -185,6 +185,11 @@
             dCPSeen[tCC3] = tYear
         if tCC3 in dCC:
             tCC2 = dCC[tCC3]
+            if (tCC2 == "UK"):
+                print("DBUG:csv_pop: UK for GB, already taken")
+                exit()
+            if (tCC2 == "GB"):
+                tCC2 = "UK"
             dCP["{}-{}".format(tCC2,tYear)] = float(tdCP[k])
             if tYear == 2010:
                 dCP2010[tCC2] = float(tdCP[k])
@@ -326,6 +331,14 @@
     return lOut
 
 
+def calc_relative2pop(lIn, geoId, dCP):
+    tPop = dCP[geoId]
+    lOut = []
+    for i in lIn:
+        lOut.append(i/tPop)
+    return lOut
+
+
 def plt_getl1(axes, axesId):
     """ Helper logic to work with plots, irrespective of whether
         there is a single plot or multiple plots in the figure 
@@ -398,6 +411,8 @@
         print("theCasesDeltaData:{}:{}".format(len(lCD), lCD))
         print("theDeathData:{}:{}".format(len(lD), lD))
         print("theDeathCumuData:{}:{}".format(len(lDC), lDC))
+        print("CasesCumu/Pop:{}\nDeathCumu/Pop:{}".format(lCC[-1]/dCP2010[geoId], lDC[-1]/dCP2010[geoId]))
+        print("0.06% of Pop:{}".format(dCP2010[geoId]*0.0006))
         thePltL1, axesId = plt_getl1(axes, axesId)
         pltId = 0
         if "Cases" in dataTypes:
