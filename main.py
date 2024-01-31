from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
import sqlite3
import pyodbc as pyo

kv = """
<LoginApp>:
ScreenManager:
    LoginScreen:
        name: "login_screen"
    SuccessScreen:
        name: "success_screen"
    SalesScreen:
        name: "sales_screen"
    PurchaseScreen:
        name: "purchase_screen"
    LogoutScreen:
        name: "logout_screen"

<LoginScreen>:
    name: "login_screen"
    MDScreen:
        md_bg_color: [210/255,230/255,240/255]
        MDCard:
            size_hint: None,None
            size: 320,400
            pos_hint: {"center_x":.5,"center_y":.5}
            #elevation: 15
            md_bg_color: [190/255,195/255,200/255]
            padding: 20
            spacing: 30
            orientation: "vertical"
            MDLabel:
                text: "LOGIN"
                font_size: 45
                halign: "center"
                size_hint_y: None
                height: self.texture_size[1]
            MDTextField:
                id: username_input
                hint_text: "Username"
                icone_right: "account"
                size_hint_x: .85
                font_size: 20
                pos_hint: {"center_x":.5}
            MDTextField:
                id: password_input
                hint_text: "Password"
                icone_right: "eye_off"
                size_hint_x: .85
                font_size: 20
                pos_hint: {"center_x":.5}
                password: True
            BoxLayout:
                size_hint: .85, None
                width: "30dp"
                height: "30dp"
                pos_hint: {"center_x":.5,"center_y":0.5}
                MDCheckbox:
                    id: check
                    size_hint: None,None
                    width: "30dp"
                    height: "30dp"
                    on_press: 
                        password_input.password = False if password_input.password == True else True
                        password_input.icon_right = "eye" if password_input.icon_right == "eye_off" else "eye_off"
                MDLabel:
                    text: "[ref=Show Password]Show Password[/ref]"
                    markup: True
            BoxLayout:
                size_hint: .85, None
                height: "30dp"
                pos_hint: {"center_x":.5,"center_y":0.5}
                spacing: "5dp"
                MDRaisedButton:
                    text: "Login"
                    font_size: "22dp"
                    size_hint_x: 1
                    spacing: 10
                    on_press: app.on_login(username_input.text, password_input.text)
                MDRaisedButton:
                    text: "Cancel"
                    font_size: "22dp"
                    size_hint_x: 1
                    on_press: app.stop()
<SuccessScreen>:
    name: "success_screen"
    MDScreen:
        md_bg_color: [210/255,230/255,240/255]
        MDCard:
            size_hint: None,None
            size: 320,320
            pos_hint: {"center_x":.5,"center_y":.5}
            elevation: 15
            md_bg_color: [190/255,195/255,200/255]
            padding: 20
            spacing: 30
            orientation: "vertical"
            MDLabel:
                text: "Welcome To Link Solution"
                font_size: 20
                halign: "center"
                #pos_hint: {"center_x":.5,"center_y":0.9}
            MDRaisedButton:
                text: "Sales"
                font_size: "22dp"
                pos_hint: {"center_x":.5,"center_y":.5}
                size_hint_x: 1
                spacing: 10
                on_press: app.on_press_sales("sales_screen")
            MDRaisedButton:
                text: "Purcahse"
                font_size: "22dp"
                pos_hint: {"center_x":.5,"center_y":.5}
                size_hint_x: 1
                on_press: app.on_press_purchase("purchase_screen")
<SalesScreen>:
    name: "sales_screen"
    MDScreen:
        md_bg_color: [210/255,230/255,240/255]
        MDCard:
            size_hint: None,None
            size: 320,320
            pos_hint: {"center_x":.5,"center_y":.5}
            elevation: 15
            md_bg_color: [190/255,195/255,200/255]
            padding: 20
            spacing: 30
            orientation: "vertical"
            MDLabel:
                text: "Sales"
                font_size: 20
                halign: "center"
                #pos_hint: {"center_x":.5,"center_y":0.9}
            MDRaisedButton:
                text: "Sales Order"
                font_size: "22dp"
                pos_hint: {"center_x":.5,"center_y":.5}
                size_hint_x: 1
                spacing: 10
                #on_press: app.on_press_sales("sales_screen")
            MDRaisedButton:
                text: "Sales Challan"
                font_size: "22dp"
                pos_hint: {"center_x":.5,"center_y":.5}
                size_hint_x: 1
                #on_press: app.stop()
            MDRaisedButton:
                text: "Sales Invoice"
                font_size: "22dp"
                pos_hint: {"center_x":.5,"center_y":.5}
                size_hint_x: 1
                #on_press: app.stop()
<PurchaseScreen>:
    name: "purchase_screen"
    MDScreen:
        md_bg_color: [210/255,230/255,240/255]
        MDCard:
            size_hint: None,None
            size: 320,320
            pos_hint: {"center_x":.5,"center_y":.5}
            elevation: 15
            md_bg_color: [190/255,195/255,200/255]
            padding: 20
            spacing: 30
            orientation: "vertical"
            MDLabel:
                text: "Purchase"
                font_size: 20
                halign: "center"
                #pos_hint: {"center_x":.5,"center_y":0.9}
            MDRaisedButton:
                text: "Purchase Order"
                font_size: "22dp"
                pos_hint: {"center_x":.5,"center_y":.5}
                size_hint_x: 1
                spacing: 10
                #on_press: app.on_press_sales("sales_screen")
            MDRaisedButton:
                text: "Purchase Challan"
                font_size: "22dp"
                pos_hint: {"center_x":.5,"center_y":.5}
                size_hint_x: 1
                #on_press: app.stop()
            MDRaisedButton:
                text: "Purchase Invoice"
                font_size: "22dp"
                pos_hint: {"center_x":.5,"center_y":.5}
                size_hint_x: 1
                #on_press: app.stop()
<LogoutScreen>:
    name: "logout_screen"
    MDScreen:
        md_bg_color: [210/255,230/255,240/255]
        MDCard:
            size_hint: None,None
            size: 320,400
            pos_hint: {"center_x":.5,"center_y":.5}
            #elevation: 15
            md_bg_color: [190/255,195/255,200/255]
            padding: 20
            spacing: 30
            orientation: "vertical"
            MDLabel:
                text: "Invalid credentials"
                font_size: 45
                halign: "center"
                size_hint_y: None
                height: self.texture_size[1]
            BoxLayout:
                size_hint: .85, None
                height: "30dp"
                pos_hint: {"center_x":.5,"center_y":0.5}
                spacing: "5dp"
                MDRaisedButton:
                    text: "Re-Login"
                    font_size: "22dp"
                    size_hint_x: 1
                    spacing: 10
                    on_press: app.on_relogin("login_screen")
"""

class LoginScreen(Screen):
    pass
class SuccessScreen(Screen):
    pass
class SalesScreen(Screen):
    pass
class PurchaseScreen(Screen):
    pass
class LogoutScreen(Screen):
    pass

class LoginApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "A700"
        return Builder.load_string(kv)

    def on_login(self, username, password):
        conn_string = 'Driver={SQL Server}; server=MAHESH\SQLEXPRESS; database=KARAN_LINK;Trusted_connection=yes;'
        my_conn = pyo.connect(conn_string,autocommit=True)
        cursor = my_conn.cursor()
        cursor.execute(' select * from comp_user where uname=? and upass=? ',(username,password))
        data = cursor.fetchall()
        my_conn.close()
        if data:
            self.root.current = "success_screen"
        else:
            self.root.current = "logout_screen"
            
    def on_relogin(self,screen_name):
        if screen_name == "login_screen":
            self.root.current = "login_screen"
    
    def on_press_sales(self,screen_name):
        if screen_name == "sales_screen":
            self.root.current = "sales_screen"
        
    def on_press_purchase(self,screen_name):
        if screen_name == "purchase_screen":
            self.root.current = "purchase_screen"

if __name__ == "__main__":
    LoginApp().run()
