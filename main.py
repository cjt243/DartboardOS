from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
import datetime
from database_functions import *

class Cricket(Screen):
    def __init__(self, **kwargs):
        super(Cricket, self).__init__(**kwargs)
    def on_pre_enter(self):
        Window.size = (480,800)
    def _set_active_players(self):
        #Get player1 and player 2 from the created game header via sql statement
        output_1 = execute_sql_statement(create_connection('gamedb/dartboardos.db'),
                   "select player1_id,username from game_header left join player on game_header.player1_id = player.id where game_header.id = (select max(id) from game_header);")
        output_2 = execute_sql_statement(create_connection('gamedb/dartboardos.db'),
                   "select player2_id,username from game_header left join player on game_header.player2_id = player.id where game_header.id = (select max(id) from game_header);")
        #set the name and player ids from the sql output
        self.player1id = output_1[0][0]
        self.ids.player1label.text = output_1[0][1]
        self.player2id = output_2[0][0]
        self.ids.player2label.text = output_2[0][1]
    def _setup_game(self):
        #get game id from created header
        output_1 = execute_sql_statement(create_connection('gamedb/dartboardos.db'),
                   "select max(id) from game_header;")
        self.gameid = output_1[0][0]
        self.game_end = ''
        self.player1_scoreboard = {'20':0,'19':0,'18':0,'17':0,'16':0,'15':0,'25':0}
        self.player2_scoreboard = {'20':0,'19':0,'18':0,'17':0,'16':0,'15':0,'25':0}
        self.player1_score = 0
        self.player2_score = 0
        #set the paths to the images for hit markers
        self.image_list = ['assets/images/transparent.png',
                           'assets/images/hit-marker-singleslash.png',
                           'assets/images/hit-marker-doubleslash.png',
                           'assets/images/hit-marker-fullmark.png']
        #create a dictionary that contains the image objects that represent hit markers
        self.button_to_image_dict = {'p120':self.ids.p120_img,
                                     'p119':self.ids.p119_img,
                                     'p118':self.ids.p118_img,
                                     'p117':self.ids.p117_img,
                                     'p116':self.ids.p116_img,
                                     'p115':self.ids.p115_img,
                                     'p125':self.ids.p125_img,
                                     'p220':self.ids.p220_img,
                                     'p219':self.ids.p219_img,
                                     'p218':self.ids.p218_img,
                                     'p217':self.ids.p217_img,
                                     'p216':self.ids.p216_img,
                                     'p215':self.ids.p215_img,
                                     'p225':self.ids.p225_img}
    def _clear_game(self):
        #reset all of the game state variables, lists and dictionaries to prep for a new game
        self.gameid = 0
        self.game_end = ''
        self.player1_scoreboard = {'20':0,'19':0,'18':0,'17':0,'16':0,'15':0,'25':0}
        self.player2_scoreboard = {'20':0,'19':0,'18':0,'17':0,'16':0,'15':0,'25':0}
        self.player1_score = 0
        self.player2_score = 0
        self.ids.player1score.text = '0'
        self.ids.player2score.text = '0'
        self.ids.player1winner.text = ''
        self.ids.player2winner.text = ''
        for key in self.button_to_image_dict:
            self.button_to_image_dict[key].source = self.image_list[0]


    def mark_hit(self, player_num,dart_val):
        #logic for when a player hits a hit marker button
        dart_val = str(dart_val)
        if player_num == 1:
            if self.player1_scoreboard[dart_val] < 3:
                #If it is an unclosed number, simply mark the hit and update game_line
                self.player1_scoreboard[dart_val] += 1
                self._write_game_line(self.player1id,dart_val,False)
                self._update_marker(player_num,dart_val,self.player1_scoreboard[dart_val])
            else:
                #If the number is closed, check to see if the opponent has closed
                #If the opponent has not closed, count the hit for points, else do nothing
                is_open = self._check_if_open(player_num, dart_val)
                if is_open == True:
                    point_val = int(dart_val)
                    self._write_game_line(self.player1id,point_val,True)
                    self.player1_score += point_val
                else:
                    point_val = 0
            #set the score text on the screen
            self.ids.player1score.text = str(self.player1_score)
            if self._check_if_winner(1):
                #if _check_if_winner returns True, update the game header and set the winner text
                update = [datetime.datetime.now(),self.player1id,self.player1_score,self.player2_score,self.gameid]
                update_game_header(create_connection('gamedb/dartboardos.db'),update)
                self.ids.player1winner.text = 'Winner!'
            else:
                pass

        elif player_num == 2:
            if self.player2_scoreboard[dart_val] < 3:
                #If it is an unclosed number, simply mark the hit and update game_line
                self.player2_scoreboard[dart_val] += 1
                self._write_game_line(self.player2id,dart_val,False)
                self._update_marker(player_num,dart_val,self.player2_scoreboard[dart_val])
            else:
                #If the number is closed, check to see if the opponent has closed
                #If the opponent has not closed, count the hit for points, else do nothing
                is_open = self._check_if_open(player_num, dart_val)
                if is_open == True:
                    point_val = int(dart_val)
                    self._write_game_line(self.player2id,point_val,True)
                    self.player2_score += point_val
                else:
                    point_val = 0
            #set the score text on the screen
            self.ids.player2score.text = str(self.player2_score)
            if self._check_if_winner(2):
                #if _check_if_winner returns True, update the game header and set the winner text
                update = [datetime.datetime.now(),self.player2id,self.player1_score,self.player2_score,self.gameid]
                update_game_header(create_connection('gamedb/dartboardos.db'),update)
                self.ids.player2winner.text = 'Winner!'
            else:
                pass
        else:
            print('Passed a player value != 1 or 2. Killing app.')
            exit()

    def _undo_mark_hit(self):
        #logic to undo hits in reverse sequence
        try:
            last_record = execute_sql_statement(create_connection('gamedb/dartboardos.db'),
                                                'select game_id, hit, points, player_id, id from game_line where id = (select max(id) from game_line where game_id = {})'.format(self.gameid))[0]
        except:
            #If there is nothing to undo, except will catch an IndexError
            return None

        if last_record[2] > 0:
            #if the last hit scored points, subtract them from the player's score
            if last_record[3] == self.player1id:
                self.player1_score -= int(last_record[2])
                self.ids.player1score.text = str(self.player1_score)
                player = 1
            else:
                self.player2_score -= int(last_record[2])
                self.ids.player2score.text = str(self.player2_score)
                player = 2
        else:
            #If the last hit did not score points step back the hit marker image
            if last_record[3] == self.player1id:
                player = 1
                key = 'p' + str(player) + str(last_record[1])
                i = self.image_list.index(self.button_to_image_dict[key].source)
                self.button_to_image_dict[key].source = self.image_list[i-1]
            else:
                player = 2
                key = 'p' + str(player) + str(last_record[1])
                i = self.image_list.index(self.button_to_image_dict[key].source)
                self.button_to_image_dict[key].source = self.image_list[i-1]
        #Always decrement the player's hit count for that number
        if player == 1:
            self.player1_scoreboard[last_record[1]] -= 1
        else:
            self.player2_scoreboard[last_record[1]] -= 1

        #delete the game_line from the db when complete
        delete_game_line(create_connection('gamedb/dartboardos.db'),last_record[4])

    def _check_if_open(self, player_num,dart_val):
        #when a hit is recorded, check to see if the other player has closed out the number
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

    def _update_marker(self, player_num, dart_val,hit_count):
        #update the image displayed when the player records a hit
        id = 'p' + str(player_num) + str(dart_val)
        self.button_to_image_dict[id].source = self.image_list[int(hit_count)]


    def _write_game_line(self,playerid,dart_val,ispoint):
        #build the game line record and write it to the db
        if ispoint:
            points = int(dart_val)
        else:
            points = 0
        game_line = [self.gameid,
                     datetime.datetime.now(),
                     str(dart_val),
                     points,
                     playerid]
        create_game_line(create_connection('gamedb/dartboardos.db'),game_line)

    def _check_if_winner(self,player_num):
        checker = 0
        if player_num == 1:
            #First check to see if the player has closed everything out
            for v in list(self.player1_scoreboard.values()):
                if v < 3:
                    return False
                else:
                    pass
            #If the player has closed everything out, check to see if they have the higher score
            if self.player1_score > self.player2_score:
                return True
            else:
                return False
        elif player_num == 2:
            for v in list(self.player2_scoreboard.values()):
            #First check to see if the player has closed everything out
                if v < 3:
                    return False
                else:
                    pass
            #If the player has closed everything out, check to see if they have the higher score
            if self.player2_score > self.player1_score:
                return True
            else:
                return False
        else:
            exit()


class Menu(Screen):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.ids.player1select.text = 'Select Player 1'
        self.ids.player2select.text = 'Select Player 2'
        self.dropdown1 = DropDown()
        self.dropdown2 = DropDown()
        self._get_players()
        self._create_dropdowns(self.ids.player1select, self.dropdown1)
        self._create_dropdowns(self.ids.player2select, self.dropdown2)
    def on_pre_enter(self):
        Window.size = (480,800)
    def _get_players(self):
        sql = 'select username from player;'
        output = execute_sql_statement(create_connection('gamedb/dartboardos.db'),sql)
        self.player_list_player = list(zip(*output))[0]
    def _create_dropdowns(self, button_id, dropdown):
        for i in self.player_list_player:
            btn = Button(text=i, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        button_id.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(button_id, 'text', x))
    def initialize_game(self):
        header = ['cricket',
                  datetime.datetime.now(),
                  '',
                  execute_sql_statement(create_connection('gamedb/dartboardos.db'),
                  "select id from player where username = '{}';".format(self.ids.player1select.text))[0][0],
                  execute_sql_statement(create_connection('gamedb/dartboardos.db'),
                  "select id from player where username = '{}';".format(self.ids.player2select.text))[0][0],
                  0,
                  0,
                  0]
        create_game_header(create_connection('gamedb/dartboardos.db'),header)
        self.manager.get_screen('cricket')._set_active_players()
        self.manager.get_screen('cricket')._setup_game()

class dartboardosApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Menu(name='menu'))
        sm.add_widget(Cricket(name='cricket'))
        return sm

if __name__ == '__main__':
    dartboardosApp().run()
