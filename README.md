# ff_data
NFL data analysis for the 2023-2024 NFL season. For fun and practice. And for showing off to my fantasy leaguemates.

Data is sourced from nflverse/nflfastR packages: 
  https://github.com/nflverse/nflfastR



### Set up notes:
#### Tools:
R and R studio. Python 3. Power BI. PostgreSQL.


#### Config:
	config.yml inputs: dbname, host, port, password, user, timezone
	config.ini inputs: database, hostname, username, pwd, port_id


#### R database for play-by-play data:
Follow the 'get started' guide for nflfastR: https://www.nflfastr.com/articles/nflfastR.html
Reference example 8 for building the play-by-play database using your preferred DBMS. This project imports data to postgreSQL.


#### Import NFL data with nfl-data-py library:
See [nfl_data_py library](https://github.com/cooperdff/nfl_data_py) for data import functions.


##### Function python_to_postgres:
	dataframe: The Pandas dataframe object created from nfl_data_py functions.
	table_name: string value of table to be written to SQL db
	if_exists: string value, one of {‘fail’, ‘replace’, ‘append’} for writing to SQL database.

#### Data Analysis and Visualization:
Perform data analysis with your preferred tools. This project is to practice Microsoft Power BI.


**todo:** 
- Create visuals per player position per week
- Import and clean data from Yahoo Fantasy Sports API for league-specific data. Create visuals for in-season rewards and other novelties.