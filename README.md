# Bayes Hack 2016
### Department of Transportation Prompt #2

_How can data help us heal communities at high risk for suicide?_

## Prompt

A person or vehicle is hit by a train about once every three hours. This results in approximately 700 deaths per year, by accident and by suicide.

By creating descriptive models that examine empiric data on train fatalities and predictive models that can anticipate accidents and suicide attempts, we can decrease the number of deaths that occur and focus on communities that are at disproportinately high risk. Good data can be a focus national efforts to heal areas impacted by suicide, and to promote smart planning and routing to prevent accidents.

## In this Repo

* `data/` - Cleaned and prepared data sources. NOTE - Not all data exists here -- see Resources section below.
   * `data-samples/` contains heavily downsampled versions of datasets, so you can poke around easily. They're in CSV, so Excel or Google Sheets should be able to load them too.
* `analysis-examples/` - iPyton notebook files (which you can view right here on GitHub) loading the data and exploring a few things. Good to understand the datasets and get ideas for your project.
* `cleaning/` - See the data preprocessing code we used (`cleaning/scripts/`), and the raw data sources that preceded the clean ones (`cleaning/raw-data/`).
   * `Makefile` has the rules to create the clean data from raw. It's generally a great pattern for data processing pipelines, see https://bost.ocks.org/mike/make/

## Data Quirks
#### Important things to know or notice
* Foo
* Bar

## Resources

* External resource links
