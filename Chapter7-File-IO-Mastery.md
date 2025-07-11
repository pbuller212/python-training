Reading Excel files that are messy

```
import polars as pl

df = pl.read_excel("complicated.xlsx", sheet_id=2))  # 2nd sheet in the workbook
df = pl.read_excel("complicated.xlsx", sheet_name="sales data"))  # based on the name of the sheet 
df = pl.read_excel("complicated.xlsx", sheet_name="sales data", read_options={"header_row": 2}))  # starts the import at row 3, skip 2 rows
df = pl.read_excel("complicated.xlsx", sheet_name="sales data", read_options={"header_row": 2}, columns="A,C:H"))  # Gets only some of the columns

```


Excel engines
* __calamine__ (default) - fastexcel, rust based
    * uses `read_options`
    * these options are pass to the the `load_sheet_by_name` call
* __openpyxl__
    * use `engine_options`
* __xlsx2csv__
    * use `engine_options`
    
# Multiple sheets

use `concat()` to combine dataframes

```
import polars as pl
sales = pl.read_excel('data/sales.xlsx')
extra = pl.read_excel('data/extra.xlsx')

# concating the dataframes requires them to be the same shape
# columns also have to match

# check the column names are the same
sales.schema
extra.schema

# here, one has a total, the other an amount
extra = extra.rename({"amount": "total"}) # renames columns OLD => NEW

# Now things match
sales = pl.concat([sales, extra])
```

# Joining sheets with cross referenced data (a JOIN, or using VLOOKUP in excel)
```
import polars as pl
sales = pl.read_excel('data/sales.xlsx')
levels = pl.read_excel('data/levels.xlsx')

# Levels looks like
# Customer | Level
# ABC      | gold
# XYZ      | silver
# etc.

levels = levels.rename({"customer": "company"}) # make sure the columns to cross reference have same name

sales.join(levels, on="company") # removes rows with no match (inner join)
sales.join(levels, on="company", how="left")  # now has rows with null for level values

# Another way to do the above
sales.join(levels, left_on="company", right_on="customer", how="left")
```

# Writing a dataframe to a file

uses ` write_excel()`. Requires the library __XlsxWriter__ to be installed.

```
import polars as pl
sales = pl.read_excel('data/sales.xlsx')
viva = sale.filter(pl.col("company")=="Viva")

from xlsxwriter.workbook import workbook
with Workbook("processed/viva.xlsx") as wb: # filename to save to
    viva.write_excel(  # dataframe to save
        workbook=wb,
        worksheet="sales"    # what the sheet will be named
        column_totals=True,  # adds sums to bottom of the table
        autofit=True,        # columns look right
        dtype_formats={pl.Date: "mm/dd/yyyy"},  # how date columns will look
        header_format={"bold": True, "font_color": "#702963"},
    )
```

With the context, multiple sheets can be produced so different dataframes could be saved to different worksheets.


