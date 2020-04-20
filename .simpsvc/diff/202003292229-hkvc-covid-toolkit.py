--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-03-29 22:04:13.585167665 +0530
+++ hkvc-covid-toolkit.py	2020-03-29 22:28:11.105145183 +0530
@@ -380,6 +380,32 @@
     return thePltL2, pltId+1
 
 
+def fill_needed_data(dD, geoIds, iDS=1, iMS=1, iDE=31, iME=12, iY=2020):
+    dD2 = { 'C': {}, 'D': {}, 'CP': {}, 'DP': {},
+            'CC': {}, 'DC': {}, 'CD': {}, 'DD': {},
+            'CM': {}, 'DM': {}, 'CMR': {}, 'DMR': {},
+            'CR': {}, 'MR': {} }
+
+    for geoId in geoIds:
+        if geoId in dD2['C']:
+            print("INFO:fill_needed_data:CC2[{}]:filled, skipping...".format(geoId))
+            continue
+        print("INFO:fill_needed_data:CC2[{}]:filling...".format(geoId))
+        dD2['C'][geoId], dD2['D'][geoId], sRange = get_covid_data(dD, geoId, iDS, iMS, iDE, iME, iY)
+        dD2['CP'][geoId] = calc_relative2pop(dD2['C'][geoId], geoId, dCP2010)
+        dD2['DP'][geoId] = calc_relative2pop(dD2['D'][geoId], geoId, dCP2010)
+        dD2['CC'][geoId] = calc_cumulatelist(dD2['C'][geoId])
+        dD2['CD'][geoId] = calc_deltalist(dD2['C'][geoId])
+        dD2['CR'][geoId] = calc_relativelist(dD2['C'][geoId])
+        dD2['CM'][geoId] = calc_movingavglist(dD2['C'][geoId])
+        dD2['CMR'][geoId] = calc_relativelist(dD2['CM'][geoId])
+        dD2['DC'][geoId] = calc_cumulatelist(dD2['D'][geoId])
+        dD2['DM'][geoId] = calc_movingavglist(dD2['D'][geoId])
+        dD2['MR'][geoId] = calc_mortalityrate(dD2['CC'][geoId], dD2['DC'][geoId])
+
+    return dD2
+
+
 def plot_what(dD, geoIds = ['IN', 'UK', 'CN'], dataTypes = [ "Cases", "CasesCumu", "Death" ], iDS=1, iMS=1, iDE=31, iME=12, iY=2020, bSingle=True, sTitle=None, iPltRows=None, iPltCols=None):
     axesId = 0
     if (iPltRows == None) or (iPltCols == None):
@@ -389,9 +415,6 @@
             fig,axes = plt.subplots(len(geoIds), len(dataTypes))
     else:
         fig,axes = plt.subplots(iPltRows, iPltCols)
-    #fig,axes = plt.subplots(len(geoIds))
-    #fig,axes = plt.subplots(1)
-    #fig,axes = plt.subplots(1,2)
     fig.set_figwidth(2*len(geoIds))
     fig.set_figheight(8*len(dataTypes))
     lAllC = []
