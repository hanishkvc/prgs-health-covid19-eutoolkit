--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-04-23 15:20:31.266940068 +0530
+++ .simpsvc/cache/hkvc-covid-toolkit.py	2020-04-23 15:43:17.782995066 +0530
@@ -16,6 +16,13 @@
 csvCovid="/tmp/covid.csv"
 
 
+
+def convert_xls2csv(xls, csv):
+    #os.system("xlsx2csv {} > {}".format(xls,csvCovid))
+    return os.system("./helpers/hkvc_pyuno_toolkit/hkvc_pyuno_toolkit.py ss2csv {} {}".format(xls,csv))
+
+
+
 def _download_data_xlsts(d,m,y):
     """ timestamped xls file download.
         Given the Day, Month & Year, create the url for xlsx file
@@ -36,12 +43,12 @@
     if bDownload:
         if os.system("wget -c {}".format(url)) != 0:
             return False
-    #os.system("xlsx2csv {} > {}".format(xls,csvCovid))
-    os.system("./helpers/hkvc_pyuno_toolkit/hkvc_pyuno_toolkit.py ss2csv {} {}".format(xls,csvCovid))
+    convert_xls2csv(xls, csvCovid)
     print(url)
     return True
 
 
+
 def download_data_ts(d=None, m=None, y=2020):
     """ Download timestamped data file
         If no day or month is given, then it is determined from
@@ -572,12 +579,15 @@
     return dD2
 
 
-download_data_ts()
+if sys.argv[1] == "download":
+    download_data_ts()
+else:
+    convert_xls2csv(sys.argv[1], csvCovid)
 dD = load_csv_eucovid()
 #print(dD)
-dCC = load_csv_cc(sys.argv[1])
+dCC = load_csv_cc(sys.argv[2])
 input("CountryCodes: {}\nPress any key...".format(dCC))
-dCP,dCP2010 = load_csv_pop(sys.argv[2])
+dCP,dCP2010 = load_csv_pop(sys.argv[3])
 input("CountryPopulation:2010: {}\nPress any key...".format(dCP2010))
 dD2 = None
 
@@ -625,3 +635,5 @@
 dD2 = do_plots(dD, dD2)
 dD2 = do_boxplot(dD, dD2)
 
+
+# vim: set softtabstop=4 expandtab: #
