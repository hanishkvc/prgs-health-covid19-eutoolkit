--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-04-18 04:10:16.984154114 +0530
+++ .simpsvc/cache/hkvc-covid-toolkit.py	2020-04-21 01:43:43.051929806 +0530
@@ -560,7 +560,7 @@
     if sTitle != None:
         plt.title(sTitle)
     ts = time.strftime("%Y%m%d%H%M%S")
-    fig.text(0.01, 0.98, "Data: Europa.EU Covid Consolidated, hkvc")
+    fig.text(0.01, 0.99, "Data: Europa.EU Covid Consolidated, {}, hkvc".format(sRange.replace(geoId,"")))
     fig.set_tight_layout(True)
     sImgFile = "/tmp/{}-covid.png".format(ts)
     fig.savefig(sImgFile, bbox_inches="tight")
@@ -608,7 +608,7 @@
 
 def do_boxplot(dD, dD2):
     geoIds = [ 'IN', 'CA', 'UK' ]
-    geoIds = [ 'IN', 'CA', 'UK', 'ES', 'FR', 'US', 'IT', 'CN' ]
+    geoIds = [ 'IN', 'CA', 'UK', 'IE', 'AE', 'ES', 'FR', 'US', 'IT', 'CN' ]
     dataTypes = [ "CasesBox" ]
     #plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True, sTitle="Cases/Day")
     dD2 = plot_what(dD, dD2, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True, iPltRows=2, iPltCols=1)
