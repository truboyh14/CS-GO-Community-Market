from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen

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
                app.login_attempt()
<MainScreen>:
    Button:
        text:"Go Back"
        on_press:
            root.manager.current="main"
<Login_Fail_Popup>
    Label:
        text: "Credential does not match"
        size_hint: 0.6, 0.2
        pos_hint: {"x":0.2,"top":0.1}
    Button:
        text: "Create New Account"
        size_hint: 0.8, 0.2
        pos_hint: {"x":0.1, "y":0.1}
        on_press:
            app.create_new_account()
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


class Login_Fail_Popup(Screen):
    pass


class Create_New_Account_Popup(Screen):
    pass


wm = ScreenManager()
wm.add_widget(LoginScreen(name='main'))
wm.add_widget(MainScreen(name='second'))
wm.add_widget(Login_Fail_Popup(name='fail_login'))


class MyApp(App):
    def build(self):
        return wm

    def login_attempt(self):
        # CHECK LOGIN CREDENTIAL
        if True:
            # if PASS
            self.root.current = "second"
        else:
            pass
            # # if FAIL
            # self.show_pop_up()


def show_pop_up(self):
    show = Login_Fail_Popup()
    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None, None), size=(400, 400))
    popupWindow.open()


def create_new_account(self):
    pass
    # create new account


class MainApp(App):
    def build(self):
        return MainScreen()


if __name__ == '__main__':
    MyApp().run()
