import pyodbc
import config

def configuration():
    """ Get the configuration information
    """
    
    driver = config.DRIVER
    server = config.SERVER
    db = config.DB
    uid = config.UID
    pwd= config.PWD
    return driver, server, db, uid, pwd


def sqldb_conn(driver, server, db, uid, pwd):
    """ Establish connection with the Azure SQL database

    Using the connect function of pyodbc to connect 
    to the Azure SQL Database and
    create connection and cursor instances.
    """

    # Connect to the Azure SQL Database
    conn = pyodbc.connect(
            'Driver=%s;Server=%s;Database=%s;Trusted_Connectoin=yes;UID=%s;PWD=%s;' % \
                (driver, server, db, uid, pwd))

    cursor = conn.cursor()
    return conn, cursor


def write_query():
    """ Define INSERT query
    """
    query = """
            INSERT INTO cc_comments (user_id, movie_id, comment)
            VALUES (?, ?, ?)
            """
    return query
            
def fetch_query():
    """ Define query to get analysis_movies data
    """
    query = """SELECT year, COUNT(year) AS count
            FROM analysis_movies
            GROUP BY year
            """
    return query

def write_to_sql(user_id, movie_id, comment):
    """ Write users' movie comments into the comments database

    Connect to the Azure SQL Database and 
    write to the Azure SQL database.
    """

    # Get Azure SQL database login configuration
    driver, server, db, uid, pwd = configuration()
    # Get connection and cursor instances
    conn, cursor = sqldb_conn(driver, server, db, uid, pwd)
    # Making the SQL INSERT query
    query = write_query()
    # Execute the query and write to Azure DB table
    cursor.execute(query, user_id, movie_id, comment)

    # Commit the connection since it is not autocimmited by default
    conn.commit()

    # Close the connection
    conn.close()
    
    return