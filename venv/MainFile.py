import kivy


from  kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.camera import Camera
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
class login_window(Widget):
    pass
class ImageButton(ButtonBehavior,Image):
    pass
class otp_window(Widget):
    pass
class create_profile_window(Widget):
    username=ObjectProperty(None)
    password = ObjectProperty(None)
    phone = ObjectProperty(None)
class complete_registration_window(Widget):
    pass
class choice_window(Widget):
    pass


class new_meeting_window(Widget):
    camera=ObjectProperty(None)
    chats=ObjectProperty(None)


class execution(App):
    def build(self):
        self.chatscounter=0
        ############################# attaching the main screen #########################
        self.screen_manager = ScreenManager()


        self.loginscreen = login_window()
        screen = Screen(name='loginscreen')
        screen.add_widget(self.loginscreen)
        self.screen_manager.add_widget(screen)

        self.createprofilescreen = create_profile_window()
        screen = Screen(name='createprofilescreen')
        screen.add_widget(self.createprofilescreen)
        self.screen_manager.add_widget(screen)

        self.otpscreen = otp_window()
        screen = Screen(name='otpscreen')
        screen.add_widget(self.otpscreen)
        self.screen_manager.add_widget(screen)

        self.completeregistrationscreen = complete_registration_window()
        screen = Screen(name='completeregistrationscreen')
        screen.add_widget(self.completeregistrationscreen)
        self.screen_manager.add_widget(screen)

        self.choicewindowscreen = choice_window()
        screen = Screen(name='choicewindowscreen')
        screen.add_widget(self.choicewindowscreen)
        self.screen_manager.add_widget(screen)


        self.newmeetingscreen = new_meeting_window()
        screen = Screen(name='newmeetingscreen')
        screen.add_widget(self.newmeetingscreen)
        self.screen_manager.add_widget(screen)
        self.newmeetingscreen.camera.resolution = (3000, 1000)

        return self.screen_manager
    def chat(self):


        if self.chatscounter == 0:
            self.chatscounter+=1
            self.newmeetingscreen.chats.opacity = 1
            self.newmeetingscreen.camera.x = -200
        else:
            self.chatscounter-=1
            self.newmeetingscreen.chats.opacity = 0
            self.newmeetingscreen.camera.x = 0
    def loginscreen_to_create_profile_window(self):
        self.screen_manager.transition.direction = 'left'
        self.screen_manager.current = 'createprofilescreen'

    def create_profile_window_to_otp_window(self):
        if self.createprofilescreen.username!='' and self.createprofilescreen.password!='' and self.createprofilescreen.phone!='':
            self.screen_manager.transition.direction = 'left'
            self.screen_manager.current = 'otpscreen'
    def otp_window_to_create_profile_window(self):
        self.screen_manager.transition.direction = 'right'
        self.screen_manager.current = 'createprofilescreen'

    def create_profile_window_to_login_window(self):
        self.screen_manager.transition.direction = 'right'
        self.screen_manager.current = 'loginscreen'

    def login_screen_to_choice_window_screen(self):
        self.screen_manager.transition.direction = 'up'
        self.screen_manager.current = 'choicewindowscreen'

    def choice_window_screen_to_new_meeting_screen(self):
        self.screen_manager.transition.direction = 'up'
        self.screen_manager.current = 'newmeetingscreen'
app=execution()
app.run()

