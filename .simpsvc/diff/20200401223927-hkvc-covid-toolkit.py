--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-04-01 22:33:44.660235870 +0530
+++ .simpsvc/cache/hkvc-covid-toolkit.py	2020-04-01 22:39:16.283242887 +0530
@@ -7,6 +7,7 @@
 import os
 import matplotlib.pyplot as plt
 import sys
+import calendar
 
 url="https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-2020-03-20.xlsx"
 xlssch="COVID-19-geographic-disbtribution-worldwide-{}-{:02}-{:02}.xlsx"
@@ -231,6 +232,9 @@
         else:
             tDE = 32
         for d in range(tDS,tDE):
+            if d > calendar.mdays[m]:
+                print("INFO:get_covid_data: Skipping invalid date m-d [{}-{}]".format(m,d))
+                continue
             keyBase="{}-{}-{}-{}-".format(geoId, iY, m, d)
             keyCases = keyBase+"cases"
             keyDeath = keyBase+"death"
@@ -246,6 +250,8 @@
             if keyDeath in dD:
                 lD.append(dD[keyDeath])
                 #print(keyDeath, dD[keyDeath])
+            else:
+                print("WARN: Missing data for %s" %(keyCases))
     sRange = "{} to {}".format(sCStart, sCEnd)
     return lC, lD, sRange
 
