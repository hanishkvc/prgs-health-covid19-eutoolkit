if [ "$1" == "" ]; then
	python3 hkvc-covid-toolkit.py download ../../../../../DATA/Countries/github/lukes/all.csv.txt ../../../../../DATA/Population/github/dataset/population.csv
else
	python3 hkvc-covid-toolkit.py $1 ../../../../../DATA/Countries/github/lukes/all.csv.txt ../../../../../DATA/Population/github/dataset/population.csv
fi
