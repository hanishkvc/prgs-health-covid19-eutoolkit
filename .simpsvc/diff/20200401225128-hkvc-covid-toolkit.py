--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-04-01 22:41:19.003245484 +0530
+++ .simpsvc/cache/hkvc-covid-toolkit.py	2020-04-01 22:51:24.403258294 +0530
@@ -233,6 +233,11 @@
             tDE = 32
         for d in range(tDS,tDE):
             if d > calendar.mdays[m]:
+                bSkip = True
+                if (m == 2) and (d == 29):
+                    if (calendar.isleap(iY)):
+                        bSkip = False
+                if bSkip:
                 print("INFO:get_covid_data: Skipping invalid date m-d [{}-{}]".format(m,d))
                 continue
             keyBase="{}-{}-{}-{}-".format(geoId, iY, m, d)
@@ -251,7 +256,7 @@
                 lD.append(dD[keyDeath])
                 #print(keyDeath, dD[keyDeath])
             else:
-                print("WARN: Missing data for %s" %(keyCases))
+                print("WARN: Missing data for %s" %(keyDeath))
     sRange = "{} to {}".format(sCStart, sCEnd)
     return lC, lD, sRange
 
