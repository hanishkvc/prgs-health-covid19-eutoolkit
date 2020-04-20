--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-03-29 23:11:46.703104275 +0530
+++ hkvc-covid-toolkit.py	2020-03-29 23:14:02.512102151 +0530
@@ -448,6 +448,7 @@
         lDC = dD2['DC'][geoId]
         lDM = dD2['DM'][geoId]
         lMR = dD2['MR'][geoId]
+        sRange = dD2['sRange']
         thePltL1, axesId = plt_getl1(axes, axesId)
         pltId = 0
         if "Cases" in dataTypes:
@@ -574,6 +575,6 @@
 iMS = 1
 iDE = 31
 iME = 3
-#dD2 = do_plots(dD, dD2)
+dD2 = do_plots(dD, dD2)
 dD2 = do_boxplot(dD, dD2)
 
