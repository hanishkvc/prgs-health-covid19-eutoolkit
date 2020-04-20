--- .simpcvs/copy/hkvc-covid-toolkit.py	2020-03-28 23:16:06.306096556 +0530
+++ hkvc-covid-toolkit.py	2020-03-28 23:44:04.606132070 +0530
@@ -28,7 +28,7 @@
     if not os.path.exists(xls):
         bDownload = True
     else:
-        got = input("INFO:download_data:%g\nDo you want to redownload?[Y/*]:" %(xls))
+        got = input("INFO:download_data:%s\nDo you want to redownload?[Y/*]:" %(xls))
         if (got.strip() == "Y"):
             bDownload = True
     if bDownload:
@@ -170,6 +170,7 @@
     dataList = [ 'pop' ]
     tdCP = _load_csv(sFile, csvIndex, keyList, dataList, bDataListInKey=False)
     dCP = {}
+    lCCMissing = {}
     for k in tdCP:
         tS = k
         atS = tS.split('-')
@@ -177,7 +178,9 @@
             atS[0] = dCC[atS[0]]
             dCP["{}-{}".format(atS[0],atS[1])] = float(tdCP[k])
         else:
-            print("Missing CC3 {}".format(atS[0]))
+            if not atS[0] in lCCMissing:
+                lCCMissing.append(atS[0])
+    print("Missing CC3 {}".format(lCCMissing))
     return dCP
 
 
@@ -220,10 +223,10 @@
                 else:
                     sCEnd = keyBase
                 lC.append(dD[keyCases])
-                print(keyCases, dD[keyCases])
+                #print(keyCases, dD[keyCases])
             if keyDeath in dD:
                 lD.append(dD[keyDeath])
-                print(keyDeath, dD[keyDeath])
+                #print(keyDeath, dD[keyDeath])
     sRange = "{} to {}".format(sCStart, sCEnd)
     return lC, lD, sRange
 
@@ -444,9 +447,9 @@
 dD = load_csv_eucovid()
 #print(dD)
 dCC = load_csv_cc(sys.argv[1])
-input("CountryCodes: {}".format(dCC))
+input("CountryCodes: {}\nPress any key...".format(dCC))
 dCP = load_csv_pop(sys.argv[2])
-print(dCP)
+input("CountryPopulation: {}\nPress any key...".format(dCP))
 
 def do_plots(dD):
     geoIds = [ 'IN', 'US', 'CA', 'IT', 'CN' ]
