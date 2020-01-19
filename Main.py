import kivy
import os.path
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from pathlib import Path
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)
# kv = Builder.load_file(os.path.join(dirname(__file__), '../uofthacks2020/my.kv'))
Builder.load_string("""
<ItemsScreen>:
    GridLayout:
        cols: 2
        GridLayout:
            rows: 5
            Label:
                text: "CS:GO Market Place"
                color: 0,0,0,1
                size_hint_x: None
                width: 200
            Button:
                text: "Items"
                background_color: 1, .3, .4, .85
                size_hint_x: None
                width: 200
                on_press:
                    items_event()
            Button:
                text: "Transactions"
                size_hint_x: None
                width: 200
                on_press:
                    transactions_event()
            Button:
                text: "Users"
                size_hint_x: None
                width: 200
                on_press:
                    users_event()
            Button:
                text: "My vault"                
                size_hint_x: None
                width: 200
                on_press:
                    vault_event()
                
        Label:
            button: "Right"
            background_color: 1, .3, .4, .85
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
                app.login_event()
<LoginFailPopup>
    BoxLayout:
        height: "40dp"
        # size_hint_y: None
        Label:
            text: "Username"
            size_hint_x: 20
        TextInput:
            size_hint_x: 20
        Button:
            text: "Check Answer"
            size_hint_x: 25
    # TextInput:
    #     id: username
    # Label:
    #     text: "Credential does not match"
    #     size_hint: 0.6, 0.2
    #     pos_hint: {"x":0.2,"top":0.1}
    # Button:
    #     text: "Create New Account"
    #     size_hint: 0.8, 0.2
    #     pos_hint: {"x":0.1, "y":0.1}
    #     on_press:
    #         app.create_new_account()
""")


# class LoginScreen(Screen):
#     pass
#     # def __init__(self, **kwargs):
#     #     super(LoginScreen, self).__init__(**kwargs)
#     #     self.inside = GridLayout()
#     #     self.inside.cols = 2
#     #     self.cols = 1
#     #
#     #     self.inside.add_widget(Label(text='User Name'))
#     #     self.username = TextInput(multiline=False)
#     #     self.inside.add_widget(self.username)
#     #     self.inside.add_widget(Label(text='password'))
#     #     self.password = TextInput(password=True, multiline=False)
#     #     self.inside.add_widget(self.password)
#     #     self.add_widget(self.inside)
#     #
#     #     self.login = Button(text="Login", font_size=40)
#     #     self.add_widget(self.login)
#     #     self.login.bind(on_press=self.login_pressed)
#     #
#     # def login_pressed(self, instance):
#     #     username = self.username.text
#     #     password = self.password.text
#     #     # get data from toda and compare


class ItemsScreen(Screen):
    pass


class TransactionsScreen(Screen):
    pass


class UsersScreen(Screen):
    pass


class VaultScreen(Screen):
    pass


# class LoginFailPopup(Screen):
#     pass
#
#
# class CreateNewAccountPopup(Screen):
#     pass


wm = ScreenManager()
wm.add_widget(ItemsScreen(name='items'))
wm.add_widget(TransactionsScreen(name='transactions'))
wm.add_widget(UsersScreen(name='users'))
wm.add_widget(VaultScreen(name='vault'))


# wm.add_widget(LoginScreen(name='second'))
# wm.add_widget(LoginFailPopup(name='fail_login'))


class Main(App):
    def build(self):
        return wm

    # def login_event(self):
    #     # CHECK LOGIN CREDENTIAL
    #     # if PASS
    #     self.root.current = "items"
    #     # if FAIL
    #     self.show_pop_up()

    def transactions_event(self):
        self.root.current = "transactions"

    def users_event(self):
        self.root.current = "users"

    def vault_event(self):
        self.root.current = "vault"

    # def show_pop_up(self):
    #     show = LoginFailPopup()
    #     popupWindow = Popup(title="Login", content=show,
    #                         size_hint=(None, None), size=(400, 400))
    #     popupWindow.open()

    # def create_new_account(self):
    #     pass
    #
    # def open_crate(self):
    #     pass
    #
    # def start_trade(self):
    #     pass


if __name__ == '__main__':
    Main().run()
