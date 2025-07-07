Polars' columns have datatypes. To perform data specific functions __accessors__ must be used.

Two common __accessors__ are
* `.dt` - datatime
* `.str` - string

Extracting date information
```
import polars as pl
sales = pl.read_excel("data/sales.xlsx")

# Get the year - returns a column of years
sales.select(year=pl.col("purchase_date").dt.year())
```

Add the columns to the dataframe
```
sales.with_columns(
    year=pl.col("purchase_date").dt.year(),
    month=pl.col("purchase_date").dt.month(),
    day=pl.col("purchase_date").dt.day(),
    quarter=pl.col("purchase_date").dt.quarter(),
)
```

More Examples
```
# alias here is for the column title
date_string = sales.select(pl.col("purchase_date").alias("date").dt.to_string())
date_string.select(pl.col("date").str.split("-"))
```

Filtering data

```
# Filter by order quantity 10 or more
sales.filter(pl.col("quantity") >= 10) # returns another dataframe

# multiple filters
sales.filter(
    pl.col("company") == "Viva",
    pl.col("quantity") >= 10,
)

```
Changing the `filter` to a `select` returns a dataframe of true/false

```
# create a mask, a column of true/false. Must be converted to a series to use in a filter
qty_10 = sales.select(pl.col("quantity") >= 10).to_series()
sales.filter(qty_10)

# Using the masks allows for complex boolean logic
viva = sales.select(pl.col("company") == "Viva")
sales.filter(viva, qty_10) # defaults to AND
sales.filter(viva & qty_10) # Same as previous line
sales.filter(viva | qty_10) # OR
```

Filter by data
```
from datetime import date
sales.filter(pl.col("purchase_date") >= date(2019, 12, 1))

sales.filter(
    pl.col("product") == book,
    pl.col("purchase_date").is_between(date(2019,11,1), data(2019,11,30))
).sort("purchase_date")

# Same result, but different filter for month
sales.filter(
    pl.col("product") == book,
    pl.col("purchase_date").dt.month() == 11),
    pl.col("purchase_date").dt.year() == 2019),
).sort("purchase_date")
```
