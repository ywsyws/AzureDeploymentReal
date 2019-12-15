# import libraries
import pyodbc
from sql import configuration, sqldb_conn, write_query

def write_sql(user_id, movie_id, comment):

    # Connect to the Azure SQL database
    driver, server, db, uid, pwd = configuration()
    conn, cursor = sqldb_conn(driver, server, db, uid, pwd)

    # Execute the query and write to Azure DB table
    query = write_query()
    cursor.execute(query, user_id, movie_id, comment)

    # Commit the connection since it is not autocimmited by default
    conn.commit()

    return

    # Close the connection
    conn.close()