Lazy evaluation - used for very large datasets

__LaztFrame__ - allows the creation of queries without loading all the data into memory
* create a LazyFrame with __scan_XYZ()__ methods like the read_XYZ()
* Excel is not supported
* __.collect()__ is then used to generate results

```
import polars as pl
sales = pl.scan_csv('data/sales.csv', try_parse_dates=True)
query = (
    sales # the LazyFrame
    .filter(pl.col("company") == "Viva")
    .group_by("product").agg(
        pl.len(),  # the count
        pl.col("quantity").alias("qty_sum").sum(),
        pl.col("quantity").alias("qty_mean").mean()
    )
)
# query is also a lazyframe
result = query.collect()
# result is a dataframe
```

Methods to get information about a LazyFrame
* __.explain()__, can be wrapped in a print to get better output
* __.show_graph()__, requires Mapplotlib and Graphviz

Converting a dataframe to a lazyframe
```
# if sales_df is a dataframe
sales_lf = sales_df.lazy()
```

Really only useful if this is going to followed with alot of queries.