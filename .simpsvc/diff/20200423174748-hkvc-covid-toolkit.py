--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-04-23 17:25:21.767241538 +0530
+++ .simpsvc/cache/hkvc-covid-toolkit.py	2020-04-23 17:47:42.596108916 +0530
@@ -43,7 +43,7 @@
     if bDownload:
         if os.system("wget -c {} --output-document=data/{}".format(url, xls)) != 0:
             return False
-    convert_xls2csv(xls, csvCovid)
+    convert_xls2csv("data/{}".format(xls), csvCovid)
     print(url)
     return True
 
