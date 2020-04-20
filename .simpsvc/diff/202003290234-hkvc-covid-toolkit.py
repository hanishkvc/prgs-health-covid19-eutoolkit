--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-03-29 00:55:52.059223218 +0530
+++ hkvc-covid-toolkit.py	2020-03-29 01:53:47.775296767 +0530
@@ -473,8 +473,8 @@
 def do_plots(dD):
     geoIds = [ 'IN', 'US', 'CA', 'IT', 'CN' ]
     geoIds = [ 'IN', 'US', 'CA', 'IT' ]
-    geoIds = [ 'IN', 'CA', 'UK', 'US', 'CN' ]
     geoIds = [ 'IN', 'CA', 'UK', 'CN' ]
+    geoIds = [ 'IN', 'CA', 'UK', 'US', 'CN' ]
     dataTypes = [ "Death" ]
     dataTypes = [ "Cases", "Death" ]
     dataTypes = [ "Cases", "CasesMovAvg", "Death", "DeathCumu" ]
