# /// script
# dependencies = ["polars", "ipdb"]
# ///

import polars as pl
import ipdb

data = {
        "name": ["Elephant", "Rhino", "Hippo", "Giraffe", "Gaur",],
        "avg_mass": [6.0, 2.0, 1.8, 1.0, 0.9],
        "max_mass": [10.4, 4.5, 4.5, 2.0, 1.5],
        "avg_length": [7.0, 4.4, 5.0, 5.2, 3.8],
        }

animals = pl.DataFrame(data)

ipdb.set_trace()

