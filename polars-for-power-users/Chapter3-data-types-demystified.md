Polars use numpy compatible datatypes, which use C compatible data types

examples:
* int16
* int64
* float32
* float64
* ...


32 bit float
* 1 bit for the sign
* 8 bits for the exponent
* 23 bits for the mantissa
* mantissa bits represent 1 / 2^n

Float data types in polars
* float32
* float64

Fixed decimal representation
- some bits for the integer
- some for the decimal 
- polars uses a 128 bit number for decimal representation
- slower than floating point math

Text
- ascii
- unicode (first 256 are same as ascii)
- multiple encoding for unicode, default in python is UTF-8

Dates 
- Python datetime objects are a decimal value
- Polars has 32 bit signed integer, much like the unix epoch, which is the Date
- time is kept in a 32 bit interger, but can represent milli, micro or 
