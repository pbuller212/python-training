* CSV import
  * Reader determines the data type
  * Basic data types are numbers and text
  * Use Polar's `read_csv()` to read a file
* Excel import
  * many more data types build into Excel
  * Polars requires `fastexecel` as a dependancy to read excel files
  * Use Polars' `read_excel()` to read files
  
Example using read_csv
```
import polars as pl
sales = pl.read_csv("data/sales.csv")
sales.schema
```

Converting strings to date
```
# Filters sales by purchases made in March (month==3)
sales.filter(pl.col("purchase_date").cast(pl.Date).dt.month()==3)
# Same information, but instead returns a column of true/false that matches the condition
sales.select(pl.col("purchase_date").cast(pl.Date).dt.month()==3)
```

Loading the csv and have it load the dates as dates instead of strings
```
sales = pl.csv_reader("data/sales.csv", try_parse_dates=True)
```

Example using read_excel
```
import polars as pl
sales = pl.read_excel("data"sales.xlsx")
sales.filter(pl.col("purchase_date").dt.month()==3).sort("purchase_date")
```

* Formulas are evaluated
* date is already in correct datatype, no casting required.

# Adding and calculating on the resulting dataframe
```
sales = sales.with_columns(County=pl.lit('USA')) # lit is short for literal, setting every row to have same value
sales = sales.with_columns(tax=pl.col("total")*0.10)
```

# Adding rows to the dataframe
```
row = { ...some data ...} # column: [values] - even if one value, still use a list
sales = pl.concat([sales, pl.DataFrame(row)])
```

# Rename with_column
```
sales.columns # returns a list of column names
Country = sales.to_series[7]
country = pl.Series("country", Country)
sales_replace_column(7, country)
```

# Editing a cell
```
row = -1
column = 0
sales[row, column] = "something new"
sales[:, "invoice"] # can also name the columns
```
__Take care - this changes data in place__   
Assignment only works on a single cell. So while more than cell can be selected to display, this cannot be used to assigned multiple calls.


