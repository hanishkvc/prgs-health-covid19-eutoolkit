--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-04-23 16:49:07.163154017 +0530
+++ .simpsvc/cache/hkvc-covid-toolkit.py	2020-04-23 17:13:10.659212113 +0530
@@ -85,7 +85,7 @@
 
 
 
-def _load_csv(sFile, csvIndex, keyList, dataList, bDataListInKey=True, iSkipLinesAtBegin=1, cDelim=','):
+def _load_csv(sFile, csvIndex, keyList, dataList, bDataListInKey=True, iSkipLinesAtBegin=1, cDelim=',', iUpdateHeaderColumnIndex=None):
     """ Load a specified csv file (default delim [,] but user can change the same)
         sFile: The name (incl path) of file to load
         csvIndex: a dictionary which maps a column header name to its column index
@@ -103,13 +103,28 @@
         iSkipLinesAtBegin: Specifies the number of lines to skip at the begining
             of the given csv file.
         cDelim: specify the delimiter char used in the given csv file.
+        iUpdateHeaderColumnIndex: Specifies which line among the skipped lines at
+            begining, contains the column header info. Inturn the same is used to
+            update the csvIndex dictionary.
 
         This func returns a dictionary containing one or more records corresponding
         to each record in the given csv file.
         """
     f = open(sFile)
+    theHeader = None
     for i in range(iSkipLinesAtBegin):
-        f.readline()
+        l = f.readline()
+        if (iUpdateHeaderColumnIndex != None) and (iUpdateHeaderColumnIndex == i):
+            theHeader = l.strip()
+
+    if theHeader != None:
+        headerCols = theHeader.split(cDelim)
+        for k in csvIndex:
+            i = headerCols.index(k)
+            if i != csvIndex[k]:
+                print("WARN:load_csv: For col [{}] index given [{}] != seen [{}], updating...".format(k, csvIndex[k], i))
+                csvIndex[k] = i
+
     dCur = {}
     dCnt = {}
     for l in f:
@@ -145,7 +160,7 @@
     csvIndex = { 'day': 1, 'month': 2, 'year': 3, 'cases': 4, 'deaths': 5, 'geoid': 7 }
     keyList = [ 'geoid', 'year', 'month', 'day' ]
     dataList = [ 'cases', 'deaths' ]
-    dD = _load_csv(sFile, csvIndex, keyList, dataList)
+    dD = _load_csv(sFile, csvIndex, keyList, dataList, iUpdateHeaderColumnIndex=0)
     print("DBG:{}:{}".format(sFile, dD))
     for k in dD:
         if k.endswith('cases'):
