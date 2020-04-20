--- .simpsvc/copy/hkvc-covid-toolkit.py	2020-03-31 23:07:16.868281581 +0530
+++ .simpsvc/cache/hkvc-covid-toolkit.py	2020-04-01 21:58:44.632191432 +0530
@@ -545,7 +545,10 @@
         # thePlt.boxplot(lAllC, 0, '') # No outliers
     if sTitle != None:
         plt.title(sTitle)
-    sImgFile = "/tmp/{}-covid.png".format(time.strftime("%Y%m%d%H%M%S"))
+    ts = time.strftime("%Y%m%d%H%M%S")
+    sImgFile = "/tmp/{}-covid.png".format(ts)
+    fig.savefig(sImgFile, bbox_inches="tight")
+    sImgFile = "/tmp/{}-covid.svg".format(ts)
     fig.savefig(sImgFile, bbox_inches="tight")
     plt.margins(0,0)
     plt.show()
