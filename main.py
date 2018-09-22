from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '800')

class dartboardosGame(Screen):
    pass

class mainMenu(Screen):
    pass

sm = ScreenManager()
sm.add_widget(dartboardosGame(name='scoreboard'))
sm.add_widget(mainMenu(name='menu'))


class dartboardosApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    dartboardosApp().run()
    # mainMenuScreen().run()
