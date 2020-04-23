--- .simpsvc/copy/hkvc-run.sh	1970-01-01 05:30:00.000000000 +0530
+++ .simpsvc/cache/hkvc-run.sh	2020-04-23 17:52:14.567573062 +0530
@@ -0,0 +1,5 @@
+if [ "$1" == "" ]; then
+	python3 hkvc-covid-toolkit.py download ../../../../../DATA/Countries/github/lukes/all.csv.txt ../../../../../DATA/Population/github/dataset/population.csv
+else
+	python3 hkvc-covid-toolkit.py $1 ../../../../../DATA/Countries/github/lukes/all.csv.txt ../../../../../DATA/Population/github/dataset/population.csv
+fi
