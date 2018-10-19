import datetime

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def create_player(conn, player):
    """
    Create a new player in the player table
    :param conn:
    :param player:
    :return: player id
    """
    sql = '''INSERT INTO player(username,create_date)
             VALUES (?,?)'''
    cur = conn.cursor()
    cur.execute(sql, player)
    conn.commit()
    return cur.lastrowid

players = ['Cullin','Zack','Charles','Mike','Cam','Hayden']

conn = create_connection('dartboardos.db')

for p in players:
    create_player(conn,[p,datetime.datetime.now()])

conn.close()
