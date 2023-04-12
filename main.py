from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.lang import Builder
from kivy.clock import Clock

import random
import glob

# Load the layout file
Builder.load_file('imageLayout.kv')


class MyLayout(Widget):
    def __init__(self):
        super(MyLayout, self).__init__()

        self.number_jpg_files = len(glob.glob('images/*.jpg'))
        print(self.number_jpg_files)

        Clock.schedule_interval(self.change_image, 5)

    def change_image(self, dt):
        random_img_number = random.randint(1, self.number_jpg_files)
        if random_img_number < 10:
            random_img_number = '0' + str(random_img_number) + '.jpg'
        else:
            random_img_number = str(random_img_number) + '.jpg'
        print(random_img_number)
        self.ids.mainImage.source = 'images/' + random_img_number


class MyImagesApp(App):
    def build(self):
        self.title = 'IMAGES'
        return MyLayout()


if __name__ == '__main__':
    # set the window size
    Config.set('graphics', 'width', '800')
    Config.set('graphics', 'height', '800')
    MyImagesApp().run()
