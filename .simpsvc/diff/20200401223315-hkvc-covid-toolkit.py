--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-04-01 22:16:33.892214058 +0530
+++ .simpsvc/cache/hkvc-covid-toolkit.py	2020-04-01 22:33:06.443235061 +0530
@@ -241,6 +241,8 @@
                     sCEnd = keyBase
                 lC.append(dD[keyCases])
                 #print(keyCases, dD[keyCases])
+            else:
+                print("WARN: Missing data for %s" %(keyCases))
             if keyDeath in dD:
                 lD.append(dD[keyDeath])
                 #print(keyDeath, dD[keyDeath])
@@ -602,8 +604,9 @@
 
 iDS = 20
 iMS = 1
-iDE = 31
-iME = 4
+iDE = time.gmtime().tm_mday
+iME = time.gmtime().tm_mon
+input("From: 2020-{}-{} to 2020-{}-{}, press any key to continue...".format(iMS,iDS, iME,iDE))
 dD2 = do_plots(dD, dD2)
 dD2 = do_boxplot(dD, dD2)
 
