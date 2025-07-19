* Aggregates are calculations that produces a single result over a group of data
   * sum
   * min
   * max
   * mean
   * sum_horizontal
* group by to generate aggregates

```
import polars as pl
sales = pl.read_excel("data/sales.xlsx")

sales.sum()
sales.mean()
sales.select(["quantity", "price"]).mean() # gives columns for the mean of quantity and price

# grouping results
sales.group_by("product").agg(pl.count())
sales.group_by("product").agg(pl.len(), pl.col("quantity").sum()) # len and count are the same

# filtering then grouping
sales.filter(pl.col("company")=="Viva").group_by("product").agg(
    pl.len(),
    pl.col("quantity").alias("qty_sum").sum(),
    pl.col("quantity").alias("qty_mean").mean(),
)

# multiple group by's
# each unique pair of company and product
sales.group_by("company", "product").agg(
    pl.len(),
    pl.col("quantity").alias("qty_sum").sum(),
    pl.col("quantity").alias("qty_mean").mean(),
)

# Dealing with null values
# the standard deviation (std) will return null if negative values or only one value
values = sales.group_by("company", "product").agg(
    pl.col("quantity").alias("qty_sum").sum(),
    pl.col("quantity").alias("qty_std").std(),
)
# different stratgies
values.fill_null(strategy="zero") # puts zeros where there were null
values.fill_null(strategy="min")
values.fill_null(strategy="max")
values.fill_null(strategy="mean")
values.drop_nulls() # gets rid of those rows

# Pivots tables
sales.pivot(
    "product", # column headers
    index="company", # form the rows' group by
    values="quantity", # what goes into the cells
    aggregate_function="sum",
    sort_columns=True
).sort("company").fill_null(strategy="zero")

   
sales.pivot(
    "product", 
    index="company", 
    values=["quantity", "total"], # multiple things to show, so quantity->product and total->product pairs
    aggregate_function="sum",
    sort_columns=True
).sort("company").fill_null(strategy="zero")
