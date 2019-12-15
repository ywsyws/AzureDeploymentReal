from urllib import parse
import pyodbc
import config

def configuration():
    """ Get the configurationi information
    """
    
    driver = config.DRIVER
    server = config.SERVER
    db = config.DB
    uid = config.UID
    pwd= config.PWD
    return driver, server, db, uid, pwd


def sqldb_conn(driver, server, db, uid, pwd):
    """ Establish connection with the Azure SQL database
    """

    # Connect to the Azure SQL Database
    conn = pyodbc.connect(
            'Driver=%s;Server=%s;Database=%s;Trusted_Connectoin=yes;UID=%s;PWD=%s;' % \
                (driver, server, db, uid, pwd))

    cursor = conn.cursor()
    return conn, cursor


def query():
    """ Define INSERT query
    """
    query = """
            INSERT INTO cc_comments (user_id, movie_id, comment)
            VALUES (?, ?, ?)
            """
    return query