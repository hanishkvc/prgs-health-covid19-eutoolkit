--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-04-21 01:44:48.695224571 +0530
+++ .simpsvc/cache/hkvc-covid-toolkit.py	2020-04-23 15:17:25.374932587 +0530
@@ -36,7 +36,8 @@
     if bDownload:
         if os.system("wget -c {}".format(url)) != 0:
             return False
-    os.system("./hkvc_pyuno_toolkit.py ss2csv {} {}".format(xls,csvCovid))
+    #os.system("xlsx2csv {} > {}".format(xls,csvCovid))
+    os.system("./helpers/hkvc_pyuno_toolkit/hkvc_pyuno_toolkit.py ss2csv {} {}".format(xls,csvCovid))
     print(url)
     return True
 
