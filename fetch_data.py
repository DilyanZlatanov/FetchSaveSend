import psycopg2

# Function collecting data from outside source
def fetch_data():
    # Set attributes to connect database
    conn = psycopg2.connect(
        host="hafsql.mahdiyari.info",
        port=5432,
        user="hafsql_public",
        password="hafsql_public",
        database="haf_block_log"
    )
    # Create a cursor
    cur = conn.cursor()

    # Execute a query
    cur.execute("SELECT block_num, trx_id FROM hafsql.op_custom_json LIMIT 10;")
    result = str(cur.fetchall())

    # Close cursor and connection
    cur.close()
    conn.close()

    return result
