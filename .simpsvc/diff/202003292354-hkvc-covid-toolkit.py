--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-03-29 23:26:43.316090252 +0530
+++ hkvc-covid-toolkit.py	2020-03-29 23:39:36.838078154 +0530
@@ -1,6 +1,6 @@
 #!/usr/bin/env python3
 # Look at global COVID data from eu
-# v20200328IST1137, HanishKVC
+# v20200329IST2329, HanishKVC
 #
 
 import time
@@ -385,14 +385,14 @@
         dD2 = { 'C': {}, 'D': {}, 'CP': {}, 'DP': {},
                 'CC': {}, 'DC': {}, 'CD': {}, 'DD': {},
                 'CM': {}, 'DM': {}, 'CMR': {}, 'DMR': {},
-                'CR': {}, 'MR': {}, 'sRange': None }
+                'CR': {}, 'MR': {}, 'sRange': {} }
 
     for geoId in geoIds:
         if geoId in dD2['C']:
             #print("INFO:fill_needed_data:CC2[{}]:filled, skipping...".format(geoId))
             continue
         print("INFO:fill_needed_data:CC2[{}]:filling...".format(geoId))
-        dD2['C'][geoId], dD2['D'][geoId], dD2['sRange'] = get_covid_data(dD, geoId, iDS, iMS, iDE, iME, iY)
+        dD2['C'][geoId], dD2['D'][geoId], dD2['sRange'][geoId] = get_covid_data(dD, geoId, iDS, iMS, iDE, iME, iY)
         dD2['CP'][geoId] = calc_relative2pop(dD2['C'][geoId], geoId, dCP2010)
         dD2['DP'][geoId] = calc_relative2pop(dD2['D'][geoId], geoId, dCP2010)
         dD2['CC'][geoId] = calc_cumulatelist(dD2['C'][geoId])
@@ -448,7 +448,7 @@
         lDC = dD2['DC'][geoId]
         lDM = dD2['DM'][geoId]
         lMR = dD2['MR'][geoId]
-        sRange = dD2['sRange']
+        sRange = dD2['sRange'][geoId]
         thePltL1, axesId = plt_getl1(axes, axesId)
         pltId = 0
         if "Cases" in dataTypes:
