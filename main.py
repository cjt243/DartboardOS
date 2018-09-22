from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.core.window import Window
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '800')

class Cricket(Screen):
    def on_pre_enter(self):
        Window.size = (480,800)
    pass

class Menu(Screen):
    def on_pre_enter(self):
        Window.size = (480,800)
    pass

class dartboardosApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Menu(name='menu'))
        sm.add_widget(Cricket(name='cricket'))
        return sm

if __name__ == '__main__':
    dartboardosApp().run()
