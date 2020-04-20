--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-03-29 22:36:31.465137357 +0530
+++ hkvc-covid-toolkit.py	2020-03-29 22:53:14.695121666 +0530
@@ -380,18 +380,21 @@
     return thePltL2, pltId+1
 
 
-def fill_needed_data(dD, geoIds, iDS=1, iMS=1, iDE=31, iME=12, iY=2020):
+def fill_needed_data(dD, dD2, geoIds, iDS=1, iMS=1, iDE=31, iME=12, iY=2020):
+    if dD2 == None:
     dD2 = { 'C': {}, 'D': {}, 'CP': {}, 'DP': {},
             'CC': {}, 'DC': {}, 'CD': {}, 'DD': {},
             'CM': {}, 'DM': {}, 'CMR': {}, 'DMR': {},
-            'CR': {}, 'MR': {} }
+                'CR': {}, 'MR': {}, 'sRange': None }
+    else:
+        dD2 = {}
 
     for geoId in geoIds:
         if geoId in dD2['C']:
             print("INFO:fill_needed_data:CC2[{}]:filled, skipping...".format(geoId))
             continue
         print("INFO:fill_needed_data:CC2[{}]:filling...".format(geoId))
-        dD2['C'][geoId], dD2['D'][geoId], sRange = get_covid_data(dD, geoId, iDS, iMS, iDE, iME, iY)
+        dD2['C'][geoId], dD2['D'][geoId], dD2['sRange'] = get_covid_data(dD, geoId, iDS, iMS, iDE, iME, iY)
         dD2['CP'][geoId] = calc_relative2pop(dD2['C'][geoId], geoId, dCP2010)
         dD2['DP'][geoId] = calc_relative2pop(dD2['D'][geoId], geoId, dCP2010)
         dD2['CC'][geoId] = calc_cumulatelist(dD2['C'][geoId])
@@ -402,11 +405,19 @@
         dD2['DC'][geoId] = calc_cumulatelist(dD2['D'][geoId])
         dD2['DM'][geoId] = calc_movingavglist(dD2['D'][geoId])
         dD2['MR'][geoId] = calc_mortalityrate(dD2['CC'][geoId], dD2['DC'][geoId])
+        print("\nINFO:needed_data: ####### Data for {} #######".format(geoId))
+        print("theCasesData:{}:{}".format(len(dD2['C'][geoId]), dD2['C'][geoId]))
+        print("theCasesCumuData:{}:{}".format(len(dD2['CC'][geoId]), dD2['CC'][geoId]))
+        print("theCasesDeltaData:{}:{}".format(len(dD2['CD'][geoId]), dD2['CD'][geoId]))
+        print("theDeathData:{}:{}".format(len(dD2['D'][geoId]), dD2['D'][geoId]))
+        print("theDeathCumuData:{}:{}".format(len(dD2['DC'][geoId]), dD2['DC'][geoId]))
+        print("CasesCumu/Pop:{}\nDeathCumu/Pop:{}".format(dD2['CC'][geoId][-1]/dCP2010[geoId], dD2['DC'][geoId][-1]/dCP2010[geoId]))
+        print("1.0% of Pop:{}".format(dCP2010[geoId]*0.01))
 
     return dD2
 
 
-def plot_what(dD, geoIds = ['IN', 'UK', 'CN'], dataTypes = [ "Cases", "CasesCumu", "Death" ], iDS=1, iMS=1, iDE=31, iME=12, iY=2020, bSingle=True, sTitle=None, iPltRows=None, iPltCols=None):
+def plot_what(dD, dD2, geoIds = ['IN', 'UK', 'CN'], dataTypes = [ "Cases", "CasesCumu", "Death" ], iDS=1, iMS=1, iDE=31, iME=12, iY=2020, bSingle=True, sTitle=None, iPltRows=None, iPltCols=None):
     axesId = 0
     if (iPltRows == None) or (iPltCols == None):
         if bSingle:
@@ -422,29 +433,23 @@
     lAllD = []
     lAllDP = []
     for geoId in geoIds:
-        lC, lD, sRange = get_covid_data(dD, geoId, iDS, iMS, iDE, iME, iY)
-        lCP = calc_relative2pop(lC, geoId, dCP2010)
-        lDP = calc_relative2pop(lD, geoId, dCP2010)
+        dD2 = fill_needed_data(dD, dD2, geoId, iDS, iMS, iDE, iME, iY)
+        lC = dD2['C'][geoId]
+        lD = dD2['D'][geoId]
+        lCP = dD2['CP'][geoId]
+        lDP = dD2['DP'][geoId]
         lAllCP.append(lCP)
         lAllDP.append(lDP)
         lAllC.append(lC)
         lAllD.append(lD)
-        lCC = calc_cumulatelist(lC)
-        lCD = calc_deltalist(lC)
-        lCR = calc_relativelist(lC)
-        lCM = calc_movingavglist(lC)
-        lCMR = calc_relativelist(lCM)
-        lDC = calc_cumulatelist(lD)
-        lDM = calc_movingavglist(lD)
-        lMR = calc_mortalityrate(lCC, lDC)
-        print("\nINFO:plot_what: ####### Data for {} #######".format(geoId))
-        print("theCasesData:{}:{}".format(len(lC), lC))
-        print("theCasesCumuData:{}:{}".format(len(lCC), lCC))
-        print("theCasesDeltaData:{}:{}".format(len(lCD), lCD))
-        print("theDeathData:{}:{}".format(len(lD), lD))
-        print("theDeathCumuData:{}:{}".format(len(lDC), lDC))
-        print("CasesCumu/Pop:{}\nDeathCumu/Pop:{}".format(lCC[-1]/dCP2010[geoId], lDC[-1]/dCP2010[geoId]))
-        print("1.0% of Pop:{}".format(dCP2010[geoId]*0.01))
+        lCC = dD2['CC'][geoId]
+        lCD = dD2['CD'][geoId]
+        lCR = dD2['CR'][geoId]
+        lCM = dD2['CM'][geoId]
+        lCMR = dD2['CMR'][geoId]
+        lDC = dD2['DC'][geoId]
+        lDM = dD2['DM'][geoId]
+        lMR = dD2['MR'][geoId]
         thePltL1, axesId = plt_getl1(axes, axesId)
         pltId = 0
         if "Cases" in dataTypes:
