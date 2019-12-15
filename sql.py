from urllib import parse
import pyodbc


def parse_url(url):
    """ Parce URL into dictionary for INPUT to Azure SQL server
    """
    # Parse URL String and capture query part
    url_query = dict(parse.parse_qsl(parse.urlsplit(url).query))
    print (url_query)
    return url_query


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