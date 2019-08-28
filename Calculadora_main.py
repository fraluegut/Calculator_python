from builtins import super

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CustomButton(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.font_size = "30sp"

class MinhaCalculadora(GridLayout):

    def press(self, button):

        if(button.text=="AC"):
            self.ti.text = ""
        elif(button.text=="="):
            self.ti.text = str(eval(self.ti.text))
        else:
            self.ti.text += button.text

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 5
        self.padding = "10dp"
        self.spacing = "10dp"

        bl = BoxLayout()
        self.add_widget(bl)
        self.ti = TextInput(font_size="30sp", multiline=False, readonly=True)
        bl.add_widget(self.ti)

        bl = BoxLayout(spacing = "7sp")
        self.add_widget(bl)
        bl.add_widget(CustomButton(text="7", on_press=self.press))
        bl.add_widget(CustomButton(text="8", on_press=self.press))
        bl.add_widget(CustomButton(text="9", on_press=self.press))
        bl.add_widget(CustomButton(text="+", on_press=self.press))

        bl = BoxLayout(spacing = "7sp")
        self.add_widget(bl)
        bl.add_widget(CustomButton(text="4", on_press=self.press))
        bl.add_widget(CustomButton(text="5", on_press=self.press))
        bl.add_widget(CustomButton(text="6", on_press=self.press))
        bl.add_widget(CustomButton(text="-", on_press=self.press))

        bl = BoxLayout(spacing = "7sp")
        self.add_widget(bl)
        bl.add_widget(CustomButton(text="1", on_press=self.press))
        bl.add_widget(CustomButton(text="2", on_press=self.press))
        bl.add_widget(CustomButton(text="3", on_press=self.press))
        bl.add_widget(CustomButton(text="*", on_press=self.press))

        bl = BoxLayout(spacing = "7sp")
        self.add_widget(bl)
        bl.add_widget(CustomButton(text="AC", on_press=self.press))
        bl.add_widget(CustomButton(text="0", on_press=self.press))
        bl.add_widget(CustomButton(text="=", on_press=self.press))
        bl.add_widget(CustomButton(text="/", on_press=self.press))

class CalculadoraApp(App):

    def build(self):
        return MinhaCalculadora()

CalculadoraApp().run()
