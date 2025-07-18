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


## Objective 1: Get the min and max gdp for each country and the year this happend
# Start with one country
maf = gdp.filter(pl.col("code") == "MAF") # pick a country with a few records
maf.with_columns(
    lowest_gdp = pl.col("gdp").get(pl.col("gdp").arg.min()).over("code")  # the over is a kind of group by
    lowest_year = pl.col("year").get(pl.col("gdp").arg.min()).over("code")  # Gets the year column based on min of gdp
)

# The full set 
gdp = gdp.with_columns(
    lowest_gdp = pl.col("gdp").get(pl.col("gdp").arg.min()).over("code")  # the over is a kind of group by
    lowest_year = pl.col("year").get(pl.col("gdp").arg.min()).over("code")  # Gets the year column based on min of gdp
    highest_gdp = pl.col("gdp").get(pl.col("gdp").arg.max()).over("code")  
    highest_year = pl.col("year").get(pl.col("gdp").arg.max()).over("code")
)

# This results in every row having the min and max gdp and year in it. Not really what is needed, so should build a pivot table
gdp.pivot("year", index=["country", "code"], values="gdp", sort_columns=True)

# This results in a column for each year with the max amount
gpd_pivot.columns # this will give a list of the columns for use in the next command
gdp_pivot = gdp_pivot.with_columns(
    best_gdp=pl.max_horizontal(gdp_pivot.columns[2:66]),
    worst_gdp=pl.min_horizontal(gdp_pivot.columns[2:66])
    )
# save the results
gdp_pivot.wrtie_csv("results/gdp_pivot.csv")

## Another task - gdp per capita
# The infer_schema is because the column has inconcistent data, floats inside an integer col
# instead everything is a string
# polars make a guess after reading a few rows
pop = pl.read_csv("data/population.csv", infer_schema=False) 

# first attempt at converting - also fails at floats
pop.with_columns(value=pl.column('pop").cast(pl.Int64))
# this converts to float then to int
pop = pop.with_columns(
    value=pl.column('pop").cast(pl.Float64).cast(pl.Int64),
    year=pl.column('year").cast(pl.Int64),
    )
pop = pop.drop("pop") # get rid of unused column

# Join the population data with gdp data
gdp = gdp.join(pop, on=["country", "code", "year"], how="left")
# add the per capita
gdp = gdp.with_columns(capita=pl.col("gdp") / pl.col("pop"))
gdp.wrtie_csv("results/per_capita.csv")

## Another task R&D
rd = pl.read_csv("raw/expenditures", columns=["LOCATION", "Country", "TIME", "Government"])
# rename column names
rd = rd.select(code=pl.col("LOCATION"), year=pl.col("TIME"), spend=pl.column("Government")) 
