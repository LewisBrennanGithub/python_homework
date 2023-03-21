import psycopg2
import psycopg2.extras as ext

def run_sql(sql, values=None):
    # set up a variable for the connection
    conn = None
    # set up an empty list
    results = []
    # try to connect to the database / db
    try:
        conn = psycopg2.connect("dbname='music_collection'")
       # get a cursor (which still step through db rows)
        cur = conn.cursor(cursor_factory=ext.DictCursor)
      # execute the sql
        cur.execute(sql, values)
       # commit the execution
        conn.commit()
      # get the results
        results = cur.fetchall()
    # close the db connection
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    # return the list
    return results