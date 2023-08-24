#!/usr/bin/env python3

import sqlite3
import json

def create_table(db_conn, table_name, columns):
    db_conn.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})")
    db_conn.commit()

def insert_data(db_conn, table_name, data):
    column_names = ', '.join(data.keys())
    placeholders = ', '.join(['?'] * len(data.keys()))
    db_conn.execute(
        f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})",
        tuple([str(val) for val in data.values()])
    )
    db_conn.commit()

def process_json(json_file, db_conn):
    with open(json_file) as f:
        data = json.load(f)

        for table_name, table_data in data.items():
            all_possible_columns = set()
            all_possible_columns.update(['key'])
            for record_key, record in table_data.items():
                all_possible_columns.update(record.keys())
            create_table(db_conn, table_name, all_possible_columns)

            for record_key, record in table_data.items():
                record['key'] = record_key
                insert_data(db_conn, table_name, record)

export_datetime = '20230823'
json_file_path = f"database-export-{export_datetime}.json"
db_conn = sqlite3.connect(f"db_{export_datetime}.db")
process_json(json_file_path, db_conn)
db_conn.close()
