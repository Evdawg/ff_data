import nfl_data_py as nfl
import pandas as pd
import datetime as dt

from python_to_postgres import python_df_to_postgres

start_year = 1999
curr_year = dt.date.today().year
print(f"Loading data between dates: {start_year} - {curr_year - 1}")
years_range = [year for year in range(start_year, curr_year)]
# print(years_range)

weekly_data = nfl.import_weekly_data(years_range)
weekly_df = pd.DataFrame(weekly_data)
nfl.clean_nfl_data(weekly_df)

print(f"Attempting to write the dataframe to postgreSQL: \n")
python_df_to_postgres(weekly_df, 'nfl_data_py_weekly', 'append')
