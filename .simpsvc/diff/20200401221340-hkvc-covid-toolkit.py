--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-04-01 21:59:41.476192635 +0530
+++ .simpsvc/cache/hkvc-covid-toolkit.py	2020-04-01 22:13:24.345210047 +0530
@@ -445,7 +445,7 @@
             figWidth = widthThres
         if figHeight > heightThres:
             figHeight = heightThres
-        input("Post:figWidth: {}, figHeight: {}".format(figWidth, figHeight))
+        print("Post:figWidth: {}, figHeight: {}".format(figWidth, figHeight))
         fig.set_figwidth(figWidth)
         fig.set_figheight(figHeight)
     lAllC = []
@@ -603,7 +603,7 @@
 iDS = 20
 iMS = 1
 iDE = 31
-iME = 3
+iME = 4
 dD2 = do_plots(dD, dD2)
 dD2 = do_boxplot(dD, dD2)
 
