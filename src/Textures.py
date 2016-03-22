from kivy.uix.image import Image as CoreImage

textures = {
    (0, 0, 0): CoreImage(source='../resources/block.png').texture,
    (255, 255, 255): CoreImage(source='../resources/air.png').texture
}
