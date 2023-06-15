# install.packages("nflfastR")
# install.packages("gsisdecoder")
# install.packages("config")
# if (!require("DBI")) install.packages("DBI")
# if (!require("RPostgres")) install.packages("RPostgres")

# dependencies:
library(tidyverse)
library(ggrepel)
library(nflreadr)
library(nflplotR)
library(nflfastR)
library(DBI)
library(RPostgres)
library(config)

# This prevents R from displaying numbers in scientific notation
options(scipen = 9999)

#----------------------------------------------------
# use config.yml for your DBMS connection:

drv = RPostgres::Postgres()
my_postgres <- dbConnect(
  drv,
  dbname = config::get("dbname"),
  host = config::get("host"),
  port = config::get("port"),
  password = config::get("password"),
  user = config::get("user"),
  service = NULL,
  bigint = c("integer64", "integer", "numeric", "character"),
  check_interrupts = FALSE,
  timezone = config::get("timezone"),
  timezone_out = NULL
)

#now create the new play-by-play db:
#source: https://www.nflfastr.com/articles/nflfastR.html#example-8-using-the-built-in-database-function

update_db(
  tblname = "nflfastR_pbp",
  force_rebuild = FALSE,
  db_connection = my_postgres
)


#return list of all tables in my NFLdb
DBI::dbListTables(my_postgres)

# Set table name as the postgres db table for future calls:
pbp_db <- dplyr::tbl(my_postgres, "nflfastR_pbp")

#summary.table(pbp_db)

# S4 method for PqConnection (close connection to NFLdb)
dbDisconnect(my_postgres)