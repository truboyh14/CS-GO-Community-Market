import kivy

from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.inside = GridLayout()
        self.inside.cols = 2
        self.cols = 1

        self.inside.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.inside.add_widget(self.username)
        self.inside.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.inside.add_widget(self.password)
        self.add_widget(self.inside)

        self.login = Button(text="Login", font_size=40)
        self.login.bind(on_pressed=self.login_pressed)
        self.add_widget(self.login)

    def login_pressed(self, instance):
        username = self.username.text
        password = self.password.text
        print("HIHIHIHIHIHIHIH")




class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()



