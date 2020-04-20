--- .simpcvs/copy/hkvc-covid-toolkit.py	2020-03-28 12:59:56.829314260 +0530
+++ hkvc-covid-toolkit.py	2020-03-28 16:59:00.934617790 +0530
@@ -14,14 +14,21 @@
 csvCovid="/tmp/covid.csv"
 
 
-def _download_data(d,m,y):
+def _download_data_xlsts(d,m,y):
+    """ timestamped xls file download.
+        Given the Day, Month & Year, create the url for xlsx file
+        and download the file using wget.
+        If file already exists, it gives the option to user as to
+        whether to redownload the file or not.
+        Once downloaded, convert the xlsx file to csv using xlsx2csv.
+        """
     xls = xlssch.format(y,m,d)
     url = urlsch.format(xls)
     bDownload = False
     if not os.path.exists(xls):
         bDownload = True
     else:
-        got = input("Do you want to redownload?[Y/*]:")
+        got = input("INFO:download_data:%g\nDo you want to redownload?[Y/*]:" %(xls))
         if (got.strip() == "Y"):
             bDownload = True
     if bDownload:
@@ -32,13 +39,17 @@
     return True
 
 
-def download_data(d=None, m=None, y=2020):
+def download_data_ts(d=None, m=None, y=2020):
+    """ Download timestamped data file
+        If no day or month is given, then it is determined from
+        the current date
+        """
     if (d == None):
         d = time.gmtime().tm_mday
     if (m == None):
         m = time.gmtime().tm_mon
-    if not _download_data(d,m,y):
-        _download_data((d-1),m,y)
+    if not _download_data_xlsts(d,m,y):
+        _download_data_xlsts((d-1),m,y)
 
 
 
@@ -65,6 +76,27 @@
 
 
 def _load_csv(sFile, csvIndex, keyList, dataList, bDataListInKey=True, iSkipLinesAtBegin=1, cDelim=','):
+    """ Load a specified csv file (default delim [,] but user can change the same)
+        sFile: The name (incl path) of file to load
+        csvIndex: a dictionary which maps a column header name to its column index
+        keyList: a list of column header names, whose corresponding record's values 
+            will be used to generate the key for that record, in the returned dictionary.
+        dataList: list of column header names. For each specified col, corresponding record
+            value will be stored in the returned dictionary as a independent entry.
+            Ex: If 2 col names are specified, then each record in the given csv file
+                will have two records/entries in the returned dictionary
+        bDataListInKey: if true, then specified col names in the dataList will be
+            suffixed as part of the dictionary key for corresponding records.
+            This helps ensure that one can distinguish the multiple records in the
+            returned dictionary, corresponding to a given record in the csv file.
+            NOTE: This needs to be True, if dataList has more than 1 col specified.
+        iSkipLinesAtBegin: Specifies the number of lines to skip at the begining
+            of the given csv file.
+        cDelim: specify the delimiter char used in the given csv file.
+
+        This func returns a dictionary containing one or more records corresponding
+        to each record in the given csv file.
+        """
     f = open(sFile)
     for i in range(iSkipLinesAtBegin):
         f.readline()
@@ -91,6 +123,10 @@
 
 
 def load_csv_eucovid(sFile=csvCovid):
+    """ Load csv file generated from the daily eu geographics covid xlsx
+        It also prints the total covid cases and deaths in the world
+        as per the given csv file.
+        """
     numCases = 0
     numDeath = 0
     # geoid-year-month-day-cases
@@ -112,6 +148,9 @@
 
 
 def load_csv_cc(sFile):
+    """ Load country code CC3 to CC2 mapping data.
+        This logic is configured to work with github-lukes csv file
+        """
     csvIndex= { 'cc2' : 1, 'cc3': 2 }
     keyList = [ 'cc3' ]
     dataList = [ 'cc2' ]
@@ -121,6 +160,11 @@
 
 
 def load_csv_pop(sFile):
+    """ Load country population data.
+        This logic is configured to work with github-dataset csv file
+        It also takes care of converting the country code from CC3
+        to CC2 format for use by other logics in the program.
+        """
     csvIndex = { 'cc3': 1, 'year': 2, 'pop': 3 }
     keyList = [ 'cc3', 'year' ]
     dataList = [ 'pop' ]
@@ -348,7 +392,7 @@
     plt.show()
 
 
-download_data()
+download_data_ts()
 dD = load_csv_eucovid()
 #print(dD)
 dCC = load_csv_cc(sys.argv[1])
