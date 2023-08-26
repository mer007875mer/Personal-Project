from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class TicTacToeApp(App):

    def build(self):
        self.layout = GridLayout(cols=3)
        self.buttons = []
        for i in range(9):
            button = Button(text='', font_size=40)
            button.bind(on_press=self.on_button_click)
            self.buttons.append(button)
            self.layout.add_widget(button)
        return self.layout

    def on_button_click(self, button):
        if button.text == '':
            button.text = 'X'
        else:
            button.text = ''

if __name__ == '__main__':
    TicTacToeApp().run()
