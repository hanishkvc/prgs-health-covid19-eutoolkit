--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-04-02 04:22:04.000000000 +0530
+++ .simpsvc/cache/hkvc-covid-toolkit.py	2020-04-18 04:06:57.600565898 +0530
@@ -9,6 +9,7 @@
 import sys
 import calendar
 
+
 url="https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-2020-03-20.xlsx"
 xlssch="COVID-19-geographic-disbtribution-worldwide-{}-{:02}-{:02}.xlsx"
 urlsch="https://www.ecdc.europa.eu/sites/default/files/documents/{}"
@@ -35,7 +36,7 @@
     if bDownload:
         if os.system("wget -c {}".format(url)) != 0:
             return False
-    os.system("xlsx2csv {} > {}".format(xls,csvCovid))
+    os.system("./hkvc_pyuno_toolkit.py ss2csv {} {}".format(xls,csvCovid))
     print(url)
     return True
 
@@ -559,6 +560,8 @@
     if sTitle != None:
         plt.title(sTitle)
     ts = time.strftime("%Y%m%d%H%M%S")
+    fig.text(0.01, 0.98, "Data: Europa.EU Covid Consolidated, hkvc")
+    fig.set_tight_layout(True)
     sImgFile = "/tmp/{}-covid.png".format(ts)
     fig.savefig(sImgFile, bbox_inches="tight")
     sImgFile = "/tmp/{}-covid.svg".format(ts)
