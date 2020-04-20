--- .simpcvs/copy/hkvc-covid-toolkit.py	2020-03-28 17:06:39.132627486 +0530
+++ hkvc-covid-toolkit.py	2020-03-28 18:11:40.635710044 +0530
@@ -182,7 +182,21 @@
 
 
 
-def get_data(geoId, iDS, iMS, iDE, iME, iY):
+def get_covid_data(dD, geoId, iDS, iMS, iDE, iME, iY):
+    """ Get covid data for the given period of dates from the
+        specified covid data dictionary.
+
+        dD: The covid data dictionary
+        geoId: The CC2 code of the country
+        iDS: the starting day
+        iMS: the starting month
+        iDE: the ending day
+        iME: the ending month
+        iY: the Year
+
+        This returns both the list of cases and list of deaths.
+        It also returns the range of date as a string.
+        """
     lC = []
     lD = []
     sCStart = None
@@ -214,7 +228,10 @@
     return lC, lD, sRange
 
 
-def list_cumulate(lIn):
+def calc_cumulatelist(lIn):
+    """ Generate a new list where each entry is cumulated data
+        over the given input list till (and including) that entry
+        """
     tCur = 0
     lOut = []
     for c in lIn:
@@ -223,14 +240,20 @@
     return lOut
 
 
-def list_delta(lIn):
+def calc_deltalist(lIn):
+    """ Generate a new list where each entry is delta between
+        the current and previous entry in the input list.
+        """
     lOut = []
     for i in range(1,len(lIn)):
         lOut.append(lIn[i] - lIn[i-1])
     return lOut
 
 
-def list_movingavg(lIn, days=7):
+def calc_movingavglist(lIn, days=7):
+    """ Generate a new list which contains a moving average
+        over the last 7 days in the given input list.
+        """
     lOut = []
     for i in range(1,len(lIn)):
         tSum = 0
@@ -257,6 +280,10 @@
 
 
 def calc_mortalityrate(lCC, lDC):
+    """ Generate a new list which contains the mortality rate
+        calculated from total cases and deaths for each entry
+        in the given Cases and Deaths list
+        """
     lMR = []
     for i in range(0,len(lCC)):
         if lCC[i] == 0:
@@ -266,7 +293,11 @@
     return lMR
 
 
-def calc_relative(lIn):
+def calc_relativelist(lIn):
+    """ Generate a new list where each entry is relative value 
+        of corresponding entry in the given/input list to the 
+        total value in the given list.
+        """
     iMax = 0
     iSum = 0
     for i in range(len(lIn)):
@@ -281,6 +312,14 @@
 
 
 def plt_getl1(axes, axesId):
+    """ Helper logic to work with plots, irrespective of whether
+        there is a single plot or multiple plots in the figure 
+        being created
+
+        This is used to handle the 1st level (the row) of plot matrix
+        TOCHECK: Have to cross check the explanation once again later.
+                    as I had created the logic few days back.
+        """
     try:
         t = len(axes)
         if (axesId >= t):
@@ -293,6 +332,15 @@
 
 
 def plt_getl2(pltL1, pltId):
+    """ Helper logic to work with plots, irrespective of whether
+        there is a single plot or multiple plots in the figure 
+        being created
+
+        This is used to handle the 2nd level (i.e the col, with in
+        a given row) of plot matrix
+        TOCHECK: Have to cross check explanation once again later.
+                    as I had created the logic few days back.
+        """
     try:
         t = len(pltL1)
         if (pltId >= t):
@@ -318,15 +366,15 @@
     lAllC = []
     lAllD = []
     for geoId in geoIds:
-        lC, lD, sRange = get_data(geoId, iDS, iMS, iDE, iME, iY)
+        lC, lD, sRange = get_covid_data(geoId, iDS, iMS, iDE, iME, iY)
         lAllC.append(lC)
         lAllD.append(lD)
-        lCC = list_cumulate(lC)
-        lCD = list_delta(lC)
-        lCR = calc_relative(lC)
-        lDC = list_cumulate(lD)
-        lCM = list_movingavg(lC)
-        lDM = list_movingavg(lD)
+        lCC = calc_cumulatelist(lC)
+        lCD = calc_deltalist(lC)
+        lCR = calc_relativelist(lC)
+        lCM = calc_movingavglist(lC)
+        lDC = calc_cumulatelist(lD)
+        lDM = calc_movingavglist(lD)
         lMR = calc_mortalityrate(lCC, lDC)
         print("theCasesData:{}:{}".format(len(lC), lC))
         print("theCasesCumuData:{}:{}".format(len(lCC), lCC))
