### This is a starting example of using nflreadr to import roster data through
### the year 1920 at earliest. I will be using similar method in python with
### nfl_data_py to send a DF of all rosters to postgreSQL.

#install.packages("nflreadr")


# dependencies:
library(nflreadr)

# This prevents R from displaying numbers in scientific notation
options(scipen = 9999)

#----------------------------------------------------
# use config.yml for your DBMS connection:



rosters <- load_rosters(2022, file_type = "csv")

