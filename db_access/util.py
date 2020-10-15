import psycopg2


def map_row(cursor, row):
    columns = [d[0].lower() for d in cursor.description]
    return dict(zip(columns, row))


def get_connection():
    """
   This utility function is used for connecting to the database

   :return: connection to database
   """
    conn = psycopg2.connect(
        host="ec2-174-129-229-162.compute-1.amazonaws.com",
        database="d3fkgbedn66ll5",
        user="vsimxlvondhgoo",
        password="7402a95816c42b475ae285eb18918c56c9a012e96a85aafce983ea1618010511",
        port=5432
    )
    return conn


def get_query_single_row(query, *args):
    """
    This utility function is used for getting a single row from an SQL query

    :param query: SQL query to be executed

    :param args: optional arguments to filter the result row

    :return: single result row
    """
    conn = get_connection()
    cursor = conn.cursor()

    rows = cursor.execute(query, args).fetchall()

    result = map_row(cursor, rows[0])

    cursor.close()
    conn.close()

    return result


def insert_row(insert_statement, *args):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(insert_statement, args)

    conn.commit()

    cursor.close()
    conn.close()

