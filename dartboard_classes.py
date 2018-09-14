import datetime
from database_functions import *

class player():
    def __init__(self,userid,username):
        self.userid = userid
        self.username = username

class cricket():
    def __init__(self):
        self.game_start = datetime.now()
        self.game_end = ''
        self.gameid = """_create_game_header()"""
        self.game_type = 'cricket'
        self.player1_scoreboard = {'20':0,'19':0,'18':0,'17':0,'16':0,'15':0,'25':0}
        self.player2_scoreboard = {'20':0,'19':0,'18':0,'17':0,'16':0,'15':0,'25':0}
        self.player1_score = 0
        self.player2_score = 0

    def _check_if_open(self, player_num,dart_val):
        """when a hit is recorded, check to see if the other player has
        closed out the number"""
        if player_num == 1:
            if self.player2_scoreboard[dart_val] < 3:
                return True
            else:
                return False
        if player_num == 2:
            if self.player1_scoreboard[dart_val] < 3:
                return True
            else:
                return False

    def mark_hit(self, player_num,dart_val):
        dart_val = str(dart_val)
        if player_num == 1:
            if self.player1_scoreboard[dart_val] < 3:
                self.player1_scoreboard += 1
            else:
                is_open = _check_if_open(player_num, dart_val)
                if is_open == True:
                    point_val = int(dart_val)
                    self.player1_score += point_val
                else:
                    point_val = 0
            _create_game_line()
        if player_num == 2:
            if self.player2_scoreboard[dart_val] < 3:
                self.player2_scoreboard += 1
            else:
                is_open = _check_if_open(player_num, dart_val)
                if is_open == True:
                    point_val = int(dart_val)
                    self.player2_score += point_val
                else:
                    point_val = 0
            _create_game_line()
        else:
            exit()
