--- .simpcvs/copy/hkvc-covid-toolkit.py	2020-03-29 00:23:38.835182310 +0530
+++ hkvc-covid-toolkit.py	2020-03-29 00:26:18.079185680 +0530
@@ -191,7 +191,8 @@
         else:
             if not tCC3 in lCCMissing:
                 lCCMissing.append(tCC3)
-    print("Missing CC3 {}".format(lCCMissing))
+    print("WARN:Missing CC3 {}".format(lCCMissing))
+    print("INFO:LatestPopInfoYear:{}".format(dCPSeen))
     return dCP, dCP2010
 
 
