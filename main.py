from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '800')

class dartboardosGame(Widget):
    pass

class mainMenu(Widget):
    pass


class dartboardosApp(App):
    def build(self):
        return dartboardosGame()

class mainMenuScreen(App):
    def build(self):
        return mainMenu()

if __name__ == '__main__':
    # dartboardosApp().run()
    mainMenuScreen().run()
