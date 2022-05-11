# %%

import boto3
import pandas as pd
import sqlalchemy

# conexão com o banco de dados
con = sqlalchemy.create_engine('sqlite:///../data/gc.db')

# salva o nome das tabelas do db
tables = con.table_names()


def save_s3(table, bucket):
    df = pd.read_sql_table(table, db_con)
    df.to_csv(f'../data/{table}.csv')

# data lake - 30m
