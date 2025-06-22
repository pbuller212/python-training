Differences between polars and pandas
 * no index, just a row. Just use square brackets
 * does not quare brackets, but operation are on objects

Basic concepts in polars
* DataFrame
* Series
* Date type
* Expressions
* Contexts

Creating a dataframe
```
df = pl.DataFrame(data)
df.shape
df.schema
df.describe()
new_df = df.select("col", "col2")
```

Using an expression to create a new dataframe. 
```
new_df = animals.select(avg_length_converted=pl.col("avg_length")*3.28)
```

The expression can be stored in a variable and then used later. Expressions are a Python object.
```
(avg_length_converted=pl.col("avg_length")*3.28
new_df = animals.select(avg_length_converted=avg_lenght_converted)
```

Expressions:
* Are a python object
* WHen using multiplication in an expression, it is not multiplication
  * Polars has overriden that operation
  * turns it into a vectorized operation
  * applies it to a column
* __Cannot simply use funtiocns from the _math_ module__
  * must use the polars version
  * `values.select(pl.col("num").sum())
  * `values.select(pl.col("num").sqrt())

Adding a column to an existing dataframe
```
animals = nimals.with_columns(avg_length_converted=avg_lenght_converted)
```

Filtering rows, returns a new dataframe
```
animals.filter(pl.col("avg_mass")>=2)
animals.filter(pl.col("avg_mass").is_between(1,2))
animals.filter(
    pl.col("avg_mass").is_between(1,2),
    pl.col("max_mass").is_between(1,2) < 5
    )
```

# Series

`quad = pl.Series("quad", [x*4 for x in range(1000)])`

Can be used with with_columns on a dataframe

To find a value in a series
```
quad.index_of(40)
```
returns 10, as this is the row that contains the value, the 11th row as it is zero-indexed

Test for uniqueness in the series
```
quad.is_unique()
quad.is_unique_counts()
```
Returns a series of the same length with booleans or counts

# Chapter 2 review
* A __DataFrame__ is made up of rows and with_columns
* DataFrames can be created from a dictionary
* __Expressions__ are operations performed on a DataFrame
* A __context__ is a subset of the DataFrame to operate on
  * .select()
  * .with_columns()
  * .filter()
