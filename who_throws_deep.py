import pandas as pd
import nfl_data_py as nfl


""" let's see who throw the ball more deep (quarterback) in 2021 """

"""
    First, we need, of course, to import the data from 2021, and we can do it
    with the function below, passing a list with the year wich we want the data
    the 'pbp' means play by play
"""

pbp_dataFrom2021 = nfl.import_pbp_data([2021]);

"""
    Now we are going to filter the data, we can do it readily, passing the
    filter criteria, filter_crit, into query() as an object, we are doing this
    to sava space line space
    then we can group the data by the attributes 'passer_id' and 'passer'
    and finally we can aggregate the data by using a python dictionary
    with the function .agg()
    so, let's do it
"""

filter_crit = 'play_type == "pass" & air_yards.notnull()';

pbp_dataFrom2021_filtered = (
    pbp_dataFrom2021.query(filter_crit)
        .groupby(["passer_id", "passer"])
        .agg({"air_yards": ["count", "mean"]})
)

"""
    the pandas package also requires reformatting the column heads via a 
    list() function and chanching the header from being two rows to a single
    row via map()
    Next, print the outputs after sorting by the mean of the air yards via the 
    query() function 
    with to_string() we can print the outputs
"""

pbp_dataFrom2021_filtered.columns = list(map("_".join, pbp_dataFrom2021_filtered.columns.values))
sort_crit = "air_yards_count > 100"

print(
    pbp_dataFrom2021_filtered.query(sort_crit)\
        .sort_values(by="air_yards_mean", ascending=[False])\
        .to_string()
)