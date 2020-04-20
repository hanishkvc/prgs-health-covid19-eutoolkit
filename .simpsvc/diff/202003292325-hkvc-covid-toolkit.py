--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-03-29 23:19:52.668096674 +0530
+++ hkvc-covid-toolkit.py	2020-03-29 23:24:49.219092036 +0530
@@ -389,7 +389,7 @@
 
     for geoId in geoIds:
         if geoId in dD2['C']:
-            print("INFO:fill_needed_data:CC2[{}]:filled, skipping...".format(geoId))
+            #print("INFO:fill_needed_data:CC2[{}]:filled, skipping...".format(geoId))
             continue
         print("INFO:fill_needed_data:CC2[{}]:filling...".format(geoId))
         dD2['C'][geoId], dD2['D'][geoId], dD2['sRange'] = get_covid_data(dD, geoId, iDS, iMS, iDE, iME, iY)
