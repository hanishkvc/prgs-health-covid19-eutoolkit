--- .simpcvs/copy/hkvc-covid-toolkit.py	2020-03-28 23:46:21.811134973 +0530
+++ hkvc-covid-toolkit.py	2020-03-29 00:17:16.323174216 +0530
@@ -170,18 +170,29 @@
     dataList = [ 'pop' ]
     tdCP = _load_csv(sFile, csvIndex, keyList, dataList, bDataListInKey=False)
     dCP = {}
+    dCP2010 = {}
+    dCPLatest = {}
     lCCMissing = []
+    dCPSeen = {}
     for k in tdCP:
         tS = k
-        atS = tS.split('-')
-        if atS[0] in dCC:
-            atS[0] = dCC[atS[0]]
-            dCP["{}-{}".format(atS[0],atS[1])] = float(tdCP[k])
+        tCC3,tYear = tS.split('-')
+        tYear = int(tYear)
+        if tCC3 in dCPSeen:
+            if dCPSeen[tCC3] < tYear:
+                dCPSeen[tCC3] = tYear
         else:
-            if not atS[0] in lCCMissing:
-                lCCMissing.append(atS[0])
+            dCPSeen[tCC3] = tYear
+        if tCC3 in dCC:
+            tCC2 = dCC[tCC3]
+            dCP["{}-{}".format(tCC2,tYear)] = float(tdCP[k])
+            if tYear == 2010:
+                dCP2010[tCC2] = float(tdCP[k])
+        else:
+            if not tCC3 in lCCMissing:
+                lCCMissing.append(tCC3)
     print("Missing CC3 {}".format(lCCMissing))
-    return dCP
+    return dCP, dCP2010
 
 
 
@@ -379,6 +390,7 @@
         lDC = calc_cumulatelist(lD)
         lDM = calc_movingavglist(lD)
         lMR = calc_mortalityrate(lCC, lDC)
+        print("\nINFO:plot_what: ####### Data for {} #######".format(geoId))
         print("theCasesData:{}:{}".format(len(lC), lC))
         print("theCasesCumuData:{}:{}".format(len(lCC), lCC))
         print("theCasesDeltaData:{}:{}".format(len(lCD), lCD))
@@ -448,8 +460,8 @@
 #print(dD)
 dCC = load_csv_cc(sys.argv[1])
 input("CountryCodes: {}\nPress any key...".format(dCC))
-dCP = load_csv_pop(sys.argv[2])
-input("CountryPopulation: {}\nPress any key...".format(dCP))
+dCP,dCP2010 = load_csv_pop(sys.argv[2])
+input("CountryPopulation:2010: {}\nPress any key...".format(dCP2010))
 
 def do_plots(dD):
     geoIds = [ 'IN', 'US', 'CA', 'IT', 'CN' ]
