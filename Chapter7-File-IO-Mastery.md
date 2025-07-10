Reading Excel files that are messy

```
import polars as pl

df = pl.read_excel("complicated.xlsx", sheet_id=2))  # 2nd sheet in the workbook
df = pl.read_excel("complicated.xlsx", sheet_name="sales data"))  # based on the name of the sheet 
df = pl.read_excel("complicated.xlsx", sheet_name="sales data", read_options={"header_row": 2}))  # starts the import at row 3, skip 2 rows
df = pl.read_excel("complicated.xlsx", sheet_name="sales data", read_options={"header_row": 2}, columns="A,C:H"))  # Gets only some of the columns

```
