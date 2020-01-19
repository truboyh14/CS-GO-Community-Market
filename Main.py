import kivy
import os.path
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from pathlib import Path
from kivy.app import App
from kivy.lang import Builder



# kv = Builder.load_file(os.path.join(dirname(__file__), '../uofthacks2020/my.kv'))
Builder.load_string("""
<LoginScreen>:
    GridLayout:
        cols: 1
        GridLayout:
            cols: 2
            Label:
                text: "Username"
            TextInput:
                id: username
        GridLayout:
            cols: 2
            Label:
                text: "Password"
            TextInput:
                id: password
        Button:
            text:"Login"
            on_press:
                root.manager.current="second"
<MainScreen>:
    Button:
        text:"Go Back"
        on_press:
            root.manager.current="main"
""")

class LoginScreen(Screen):
    pass
    # def __init__(self, **kwargs):
    #     super(LoginScreen, self).__init__(**kwargs)
    #     self.inside = GridLayout()
    #     self.inside.cols = 2
    #     self.cols = 1
    #
    #     self.inside.add_widget(Label(text='User Name'))
    #     self.username = TextInput(multiline=False)
    #     self.inside.add_widget(self.username)
    #     self.inside.add_widget(Label(text='password'))
    #     self.password = TextInput(password=True, multiline=False)
    #     self.inside.add_widget(self.password)
    #     self.add_widget(self.inside)
    #
    #     self.login = Button(text="Login", font_size=40)
    #     self.add_widget(self.login)
    #     self.login.bind(on_press=self.login_pressed)
    #
    # def login_pressed(self, instance):
    #     username = self.username.text
    #     password = self.password.text
    #     # get data from toda and compare


class MainScreen(Screen):
    pass
    # def __init__(self, **kwargs):
    #     super(MainScreen, self).__init__(**kwargs)
    #     self.cols = 1
    #     self.goback = Button(text="Go Back", font_size=40)
    #     self.add_widget(self.goback)
    #     self.goback.bind(on_press=self.go_back_pressed)
    #
    # def go_back_pressed(self, instance):
    #     self.app.current = LoginScreen


wm = ScreenManager()
wm.add_widget(LoginScreen(name='main'))
wm.add_widget(MainScreen(name='second'))

class MyApp(App):
    def build(self):
        return wm

class MainApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    MyApp().run()
