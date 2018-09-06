from kivy.app import App
from kivy.uix.widget import Widget

class dartboardosGame(Widget):
    pass

class dartboardosApp(App):
    def build(self):
        return dartboardosGame()

if __name__ == '__main__':
    dartboardosApp().run()
