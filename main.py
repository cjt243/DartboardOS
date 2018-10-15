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
    pass

class dartboardosApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Menu(name='menu'))
        sm.add_widget(Cricket(name='cricket'))
        return sm

if __name__ == '__main__':
    dartboardosApp().run()
