"""File that contains the function definitions to insert, update, and delete from dartboardos.db"""
import sqlite3
from sqlite3 import Error

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
    return cur.lastrowid

def create_game_header(conn, game_header):
    """
    Create a new game header in the game_header table
    :param conn:
    :param game_header:
    :return: game_header id
    """
    sql = ''' INSERT INTO game_header(game_type,game_start,game_end,player1_id,player2_id,winner_id,player1_score,player2_score)
              VALUES(?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, game_header)
    return cur.lastrowid

def create_game_line(conn, game_line):
    """
    Create a new game header in the game_header table
    :param conn:
    :param game_header:
    :return: game_header id
    """
    sql = ''' INSERT INTO game_line(game_id,datetimestamp,hit,points,player_id)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, game_line)




    return cur.lastrowid

def update_player_username(conn, player_update):
        """
        Update player username in the player table
        :param conn:
        :param player_update (username, player_id):
        :return: player id
        """
        sql = ''' UPDATE player
                  SET username = ?
                  WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, player_update)
        return cur.lastrowid

def update_game_header(conn,game_header_update):
        """
        Update game_header in the game_header table
        :param conn:
        :param game_header_update (game_end, winner, player1_score, player2_score, game_id):
        :return: game_id
        """
        sql = ''' UPDATE game_header
                  SET game_end = ?,
                      winner = ?,
                      player1_score = ?,
                      player2_score = ?
                  WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, game_header_update)
        return cur.lastrowid

def delete_player(conn, id):
    """
    Delete a player by player id
    :param conn:  Connection to the SQLite database
    :param id: id of the player
    :return:
    """
    sql = 'DELETE FROM player WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))

def delete_game_header(conn, id):
    """
    Delete a game_header by game_id
    :param conn:  Connection to the SQLite database
    :param id: id of the game_header
    :return:
    """
    sql = 'DELETE FROM game_header WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))

def delete_game_line(conn,game_id):
    """
    Delete a game_line by game_line id
    :param conn:  Connection to the SQLite database
    :param id: id of the player
    :return:
    """
    sql = 'DELETE FROM player WHERE game_id=? and id=max(id)'
    cur = conn.cursor()
    cur.execute(sql, (game_id,))
