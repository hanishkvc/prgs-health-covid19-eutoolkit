--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-04-23 17:18:32.407225063 +0530
+++ .simpsvc/cache/hkvc-covid-toolkit.py	2020-04-23 17:23:55.931238084 +0530
@@ -155,10 +155,10 @@
         """
     numCases = 0
     numDeath = 0
-    # geoid-year-month-day-cases
-    # geoid-year-month-day-deaths
-    csvIndex = { 'day': 1, 'month': 2, 'year': 3, 'cases': 4, 'deaths': 5, 'geoid': 7 }
-    keyList = [ 'geoid', 'year', 'month', 'day' ]
+    # geoId-year-month-day-cases
+    # geoId-year-month-day-deaths
+    csvIndex = { 'day': 1, 'month': 2, 'year': 3, 'cases': 4, 'deaths': 5, 'geoId': 7 }
+    keyList = [ 'geoId', 'year', 'month', 'day' ]
     dataList = [ 'cases', 'deaths' ]
     dD = _load_csv(sFile, csvIndex, keyList, dataList, iUpdateHeaderColumnIndex=0)
     print("DBG:{}:{}".format(sFile, dD))
