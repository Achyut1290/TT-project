MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "1290"
MYSQL_DATABASE = "constructionos"

import mysql.connector


def get_db_connection():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
    )
