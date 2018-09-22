from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import ListProperty, NumericProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from database_functions import *

class Cricket(Screen):
    def on_pre_enter(self):
        Window.size = (480,800)
    pass

class Menu(Screen):
    # player_list_player = ListProperty([])
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.ids.player1select.text = 'Select Player 1'
        self._get_players()
    def _get_players(self):
        sql = 'select username from player;'
        output = execute_select_statement(create_connection('gamedb/dartboardos.db'),sql)
        self.player_list_player = list(zip(*output))[0]
    def _create_dropdowns(self,dropdown):
        self.dropdown = DropDown()
        for i in self.player_list_player:
            btn = Button(text=i, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        self.ids.player1select.bind(on_release=dropdown.open)
        self.ids.player1select.dropdown.bind(on_select=lambda instance, x: setattr(self.ids.player1select, 'text', x))
    def on_pre_enter(self):
        Window.size = (480,800)
    pass

class dartboardosApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Menu(name='menu'))
        # sm.add_widget(Menu())
        sm.add_widget(Cricket(name='cricket'))
        return sm

if __name__ == '__main__':
    dartboardosApp().run()
