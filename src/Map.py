from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image as CoreImage
import Image
import os
from Textures import textures


class Map:
    def __init__(self, map_file_path, textures):
        """
        Load and create a map.
        :param map_file_path: string
        """
        is_file = os.path.isfile(map_file_path)
        if not is_file:
            raise ValueError("File given does not exist.")
        is_png = map_file_path.lower().endswith('.png')
        if not is_png:
            raise ValueError("File given is not a png image.")

        image = Image.open(map_file_path)

        image_width = image.size[0]
        image_height = image.size[1]

        if image_width <= 0 or image_height <= 0:
            raise ValueError("Image given is not valid for use.")

        self.textures = textures

        self.grid = GridLayout(rows=image_width, cols=image_height)

        pixels = image.load()

        for y in range(0, image_height):
            for x in range(0, image_width):
                rgb = pixels[x, y]
                texture = self.get_texture(rgb)
                self.grid.add_widget(CoreImage(texture=texture))

    def get_texture(self, rgb):
        """
        Match texture needed with texture from Textures.py
        :param rgb:tuple of red, green, blue
        :return:texture
        """

        try:
            # print(rgb)
            texture = self.textures[rgb]
        except KeyError, error:
            raise KeyError("Texture ", rgb, " doesn't exist :", error)

        return texture


from kivy.app import App
if __name__ == '__main__':

    class TestApp(App):
        def build(self):
            grid = Map("../resources/test.png", textures).grid
            return grid

    TestApp().run()
