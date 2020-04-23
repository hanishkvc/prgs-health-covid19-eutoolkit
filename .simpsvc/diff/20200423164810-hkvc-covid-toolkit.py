--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-04-23 16:22:09.651088917 +0530
+++ .simpsvc/cache/hkvc-covid-toolkit.py	2020-04-23 16:45:18.499144814 +0530
@@ -41,7 +41,7 @@
         if (got.strip() == "Y"):
             bDownload = True
     if bDownload:
-        if os.system("wget -c {}".format(url)) != 0:
+        if os.system("wget -c {} --output-document=data/{}".format(url, xls)) != 0:
             return False
     convert_xls2csv(xls, csvCovid)
     print(url)
@@ -128,6 +128,7 @@
             else:
                 tKey = keyBase
             dCur[tKey] = la[csvIndex[d]]
+    f.close()
     return dCur
 
 
@@ -140,16 +141,17 @@
     numCases = 0
     numDeath = 0
     # geoid-year-month-day-cases
-    # geoid-year-month-day-death
-    csvIndex = { 'day': 1, 'month': 2, 'year': 3, 'cases': 4, 'death': 5, 'geoid': 7 }
+    # geoid-year-month-day-deaths
+    csvIndex = { 'day': 1, 'month': 2, 'year': 3, 'cases': 4, 'deaths': 5, 'geoid': 7 }
     keyList = [ 'geoid', 'year', 'month', 'day' ]
-    dataList = [ 'cases', 'death' ]
+    dataList = [ 'cases', 'deaths' ]
     dD = _load_csv(sFile, csvIndex, keyList, dataList)
+    print("DBG:{}:{}".format(sFile, dD))
     for k in dD:
         if k.endswith('cases'):
             dD[k] = int(dD[k])
             numCases += dD[k]
-        elif k.endswith('death'):
+        elif k.endswith('deaths'):
             dD[k] = int(dD[k])
             numDeath += dD[k]
     input("INFO:LOAD:Cases {}, Deaths {}: Press any key...".format(numCases, numDeath))
@@ -251,7 +253,7 @@
                     continue
             keyBase="{}-{}-{}-{}-".format(geoId, iY, m, d)
             keyCases = keyBase+"cases"
-            keyDeath = keyBase+"death"
+            keyDeath = keyBase+"deaths"
             if keyCases in dD:
                 if sCStart == None:
                     sCStart = keyBase
