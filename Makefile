# This file is used to simplify the pipeline of data pulling and cleaning
# See Mike Bostock's https://bost.ocks.org/mike/make/
## NOTE: Makefiles need TABS not SPACES for indentation

all: data/transportation-railroad-casualties.csv data/samples/transportation-railroad-casualties-sample.csv

clean:
	rm data/transportation-railroad-casualties.csv data/samples/transportation-railroad-casualties-sample.csv

data/transportation-railroad-casualties.csv:
	mkdir -p "$(dir $@)"
	python cleaning/scripts/fix_railroad.py cleaning/raw-data/ALLCASUALTIES.csv data/transportation-railroad-casualties.csv

data/samples/transportation-railroad-casualties-sample.csv: data/transportation-railroad-casualties.csv
	mkdir -p "$(dir $@)"
	python cleaning/scripts/csv_sample.py data/transportation-railroad-casualties.csv data/samples/transportation-railroad-casualties-sample.csv 0.001
