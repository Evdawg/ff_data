import nfl_data_py as nfl
import pandas as pd
import datetime as dt
import config_file
import sqlalchemy
from sqlalchemy import create_engine, URL, text
from sqlalchemy.orm import sessionmaker
import psycopg2

### This is a template for using config file settings to connect to user's SQL db.
#-----------------------------------------------------------------------------------------------------------------------

# Reads the config file for reference to user SQLdb
config = config_file.read_config()

# construct a URL object to utilize config.ini settings:
url_object = URL.create(
    "postgresql+psycopg2",
    username= config['SQLdb']['username'],
    password= config['SQLdb']['pwd'],
    host= config['SQLdb']['hostname'],
    database= config['SQLdb']['database'],)

try:
# Create the engine:
    engine = create_engine(url_object)

#-----------------------------------------------------------------------------------------------------------------------
### Place your code block here that outputs a Pandas DataFrame:

# set the variables for start and end years. May need to adjust end year by -1 year
    start_year = 1999
    curr_year = dt.date.today().year
    print(f"{start_year} - {curr_year - 1}")

    years_range = [year for year in range(start_year, curr_year)]
    print(years_range)

    rosters = nfl.import_rosters(years_range)
    rosters_df = pd.DataFrame(rosters)
    nfl.clean_nfl_data(rosters_df)
    print(rosters_df)


### End code block here.
#-----------------------------------------------------------------------------------------------------------------------

# Send the Pandas DataFrame (roster_df) to a SQL database using psycopg2 and SQLalchemy libraries:
    with engine.begin() as connection:
        rosters_df.to_sql(
            name= 'nfl_data_py_rosters',
            con= engine,
            if_exists= 'replace', # or {‘fail’, ‘replace’, ‘append’}, default ‘fail’
            index= False)


# Close the connection if no error in try-except block:
except Exception as error:
    print(error)