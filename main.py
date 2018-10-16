from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import ListProperty, NumericProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
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
        output_1 = execute_select_statement(create_connection('gamedb/dartboardos.db'),
                   "select player1_id,username from game_header left join player on game_header.player1_id = player.id where game_header.id = (select max(id) from game_header);")
        output_2 = execute_select_statement(create_connection('gamedb/dartboardos.db'),
                   "select player2_id,username from game_header left join player on game_header.player2_id = player.id where game_header.id = (select max(id) from game_header);")
        self.player1id = output_1[0][0]
        self.ids.player1label.text = output_1[0][1]
        self.player2id = output_2[0][0]
        self.ids.player2label.text = output_2[0][1]
    def _setup_game(self):
        output_1 = execute_select_statement(create_connection('gamedb/dartboardos.db'),
                   "select max(id) from game_header;")
        self.gameid = output_1[0][0]
        self.game_end = ''
        self.player1_scoreboard = {'20':0,'19':0,'18':0,'17':0,'16':0,'15':0,'25':0}
        self.player2_scoreboard = {'20':0,'19':0,'18':0,'17':0,'16':0,'15':0,'25':0}
        self.player1_score = 0
        self.player2_score = 0
    def mark_hit(self, player_num,dart_val):
        dart_val = str(dart_val)
        if player_num == 1:
            if self.player1_scoreboard[dart_val] < 3:
                self.player1_scoreboard[dart_val] += 1
                self.terrible_function(player_num,dart_val)
            else:
                is_open = self._check_if_open(player_num, dart_val)
                if is_open == True:
                    point_val = int(dart_val)
                    self.player1_score += point_val
                else:
                    point_val = 0
            self.ids.player1score.text = str(self.player1_score)
            # _create_game_line()
        elif player_num == 2:
            if self.player2_scoreboard[dart_val] < 3:
                self.player2_scoreboard[dart_val] += 1
                self.terrible_function(player_num,dart_val)
            else:
                is_open = self._check_if_open(player_num, dart_val)
                if is_open == True:
                    point_val = int(dart_val)
                    self.player2_score += point_val
                else:
                    point_val = 0
            self.ids.player2score.text = str(self.player2_score)
            # _create_game_line()
        else:
            exit()
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
    # def update_button_label(self,player_num,button):
    #     if player_num == 1:
    #         if self.player1_scoreboard[dart_val] < 3:
    #             retstr(self.player1_scoreboard[dart_val])
    #         else:
    #             button.text = '3'
    #     if player_num == 2:
    #         if self.player2_scoreboard[dart_val] < 3:
    #             button.text = str(self.player2_scoreboard[dart_val])
    #         else:
    #             button.text = '3'
    def terrible_function(self, player_num, dart_val):
        id = str(player_num) + str(dart_val)
        if id == '120':
            self.ids.p120.text = str(self.player1_scoreboard[dart_val])
        elif id == '119':
            self.ids.p119.text = str(self.player1_scoreboard[dart_val])
        elif id == '118':
            self.ids.p118.text = str(self.player1_scoreboard[dart_val])
        elif id == '117':
            self.ids.p117.text = str(self.player1_scoreboard[dart_val])
        elif id == '116':
            self.ids.p116.text = str(self.player1_scoreboard[dart_val])
        elif id == '115':
            self.ids.p115.text = str(self.player1_scoreboard[dart_val])
        elif id == '125':
            self.ids.p125.text = str(self.player1_scoreboard[dart_val])
        elif id == '220':
            self.ids.p220.text = str(self.player2_scoreboard[dart_val])
        elif id == '219':
            self.ids.p219.text = str(self.player2_scoreboard[dart_val])
        elif id == '218':
            self.ids.p218.text = str(self.player2_scoreboard[dart_val])
        elif id == '217':
            self.ids.p217.text = str(self.player2_scoreboard[dart_val])
        elif id == '216':
            self.ids.p216.text = str(self.player2_scoreboard[dart_val])
        elif id == '215':
            self.ids.p215.text = str(self.player2_scoreboard[dart_val])
        elif id == '225':
            self.ids.p225.text = str(self.player2_scoreboard[dart_val])


    pass

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
    def _get_players(self):
        sql = 'select username from player;'
        output = execute_select_statement(create_connection('gamedb/dartboardos.db'),sql)
        self.player_list_player = list(zip(*output))[0]
    def _create_dropdowns(self, button_id, dropdown):
        for i in self.player_list_player:
            btn = Button(text=i, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        button_id.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(button_id, 'text', x))
    def on_pre_enter(self):
        Window.size = (480,800)
    def initialize_game(self):
        header = ['cricket',
                  datetime.datetime.now(),
                  '',
                  execute_select_statement(create_connection('gamedb/dartboardos.db'),
                  "select id from player where username = '{}';".format(self.ids.player1select.text))[0][0],
                  execute_select_statement(create_connection('gamedb/dartboardos.db'),
                  "select id from player where username = '{}';".format(self.ids.player2select.text))[0][0],
                  0,
                  0,
                  0]
        create_game_header(create_connection('gamedb/dartboardos.db'),header)
        self.manager.get_screen('cricket')._set_active_players()
        self.manager.get_screen('cricket')._setup_game()
    pass

class dartboardosApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Menu(name='menu'))
        sm.add_widget(Cricket(name='cricket'))
        return sm

if __name__ == '__main__':
    dartboardosApp().run()
