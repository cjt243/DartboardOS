from kivy.app import App
from kivy.uix.widget import Widget

class cricketGame(Widget):
    pass

class dartboardos(App):
    def build(self):
        return cricketGame()

if __name__ == '__main__':
    dartboardos().run()
