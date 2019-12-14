# import libraries
from functions import parse_url, sqldb_conn, query
import config

def write_sql(user_id, movie_id, comment):
    # Set URL
    # url = 'https://www.yws.com?user_id=11&movie_id=111&comment=asdf'
    # url_query = parse_url(url)

    # Connect to the Azure SQL database
    conn = pyodbc.connect(
        'Driver={ODBC Driver 17 for SQL Server};'
        'Server=azuresqlorange.database.windows.net;'
        'Database=orange_azure;'
        'Trusted_Connectoin=yes;'
        'UID=orange;'
        'PWD=Supermotdepasse!42;')
    cursor = conn.cursor()

    # Execute the query and write to Azure DB table
    query = """
            INSERT INTO cc_comments (user_id, movie_id, comment)
            VALUES (?, ?, ?)
            """
    cursor.execute(query, user_id, movie_id, comment)

    # Commit the connection since it is not autocimmited by default
    conn.commit()

    return

    # Close the connection
    conn.close()