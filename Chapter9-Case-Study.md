Goal is to generate the following reports from three different dataset
* GDP by country over time
    * Include best and worst years
* GDP per capita
* Government research spend as a percentage of GDP


Best practices for setting up a project:
* seperate the raw data into a folder
    * leave this untouched
* add results into a different folder

```
import polars as pl
gdp = pl.read_csv("raw/gdp.csv")
gdp.rename({
    "Country Name": "county",
    "Country Code": "code",
    "Year": "year",
    "Value": gdp",
    })  # first run is to verify we like the result
gdp = gdp.rename({
    "Country Name": "county",
    "Country Code": "code",
    "Year": "year",
    "Value": gdp",
    })  # now save the results

# Chek out the data - looks for problems
gdp.describe()
# Shows min value for GDP is very low compared to other values
gdp.filter(pl.col("gdp") < 20000)
# returns three rows for the country of Georgia
gdp.filter(pl.col("code") == "GEO")

# check the upper bounds
top_gdp = gdp.select(pl.col("gdp").max()).item()
# top_gdp = 10192863589032 (10^14)
pdf.filter(pl.col(gdp) == top_gdp)
# ends up being a sum column

count = gdp.group_by(["country", "code"]).agg(pl.len())
count.max() ## REMEMBER this is not the same rows


