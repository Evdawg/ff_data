import nfl_data_py as nfl
import pandas as pd
import datetime as dt

from python_to_postgres import python_df_to_postgres

# set the variables for start and end years. May need to adjust end year by -1 year
start_year = 1999
curr_year = dt.date.today().year
years_range = [year for year in range(start_year, curr_year)]
print(f"Loading data between dates: {start_year} - {curr_year - 1}")
#print(years_range)

rosters = nfl.import_rosters(years_range)
rosters_df = pd.DataFrame(rosters)
nfl.clean_nfl_data(rosters_df)
#print(rosters_df)


print(f"Writing the dataframe to postgreSQL: \n")
python_df_to_postgres(rosters_df, 'nfl_data_py_rosters', 'replace')