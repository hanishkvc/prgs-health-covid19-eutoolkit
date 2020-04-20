--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-03-29 23:03:36.746111938 +0530
+++ hkvc-covid-toolkit.py	2020-03-29 23:08:34.780107276 +0530
@@ -386,8 +386,6 @@
                 'CC': {}, 'DC': {}, 'CD': {}, 'DD': {},
                 'CM': {}, 'DM': {}, 'CMR': {}, 'DMR': {},
                 'CR': {}, 'MR': {}, 'sRange': None }
-    else:
-        dD2 = {}
 
     for geoId in geoIds:
         if geoId in dD2['C']:
@@ -433,7 +431,7 @@
     lAllD = []
     lAllDP = []
     for geoId in geoIds:
-        dD2 = fill_needed_data(dD, dD2, geoId, iDS, iMS, iDE, iME, iY)
+        dD2 = fill_needed_data(dD, dD2, [geoId], iDS, iMS, iDE, iME, iY)
         lC = dD2['C'][geoId]
         lD = dD2['D'][geoId]
         lCP = dD2['CP'][geoId]
