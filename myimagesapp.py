from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.uix.image import Image
from kivy.lang import Builder

# Load the layout file
Builder.load_file('imageLayout.kv')

class MyLayout(Widget):
    def __init__(self):
        super(MyLayout, self).__init__()
        self.ids.mainImage.source = 'images/02.jpg'

class MyImagesApp(App):
    def build(self):
        self.title = 'IMAGES'
        return MyLayout()


if __name__ == '__main__':
    # set the window size
    Config.set('graphics', 'width', '800')
    Config.set('graphics', 'height', '800')
    MyImagesApp().run()