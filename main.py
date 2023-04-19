import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivymd.app import MDApp
Window.size = (800, 500)


class MainWidget(Widget):

    def start_sort(self):
        print("you clicked me")

    def cancel_sort(self):
            print("you canceled sort")


class CapaSorterApp(App):
    def build(self):
        return MainWidget()


if __name__ == "__main__":
    CapaSorterApp().run()


