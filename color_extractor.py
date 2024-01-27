from colorthief import ColorThief

class ColorExtractor:
    def __init__(self, image_path):
        self.image_path= image_path
    
    def close_to_white(self, rgb_color, distance=5):
        """
        Given a RGB code, decide if it is close to the background color (231, 231, 231).
        """
        color_diff = [231-c for c in rgb_color]
        if all(value < distance for value in color_diff):
            return True
        else:
            return False

    def get_dominant_color(self):
        color_thief = ColorThief(self.image_path)
        dominant_color = color_thief.get_color(quality=1)
        palette = color_thief.get_palette(color_count=5)

        if self.close_to_white(dominant_color):
            if self.close_to_white(palette[0]):
                return palette[1]
            else:
                return palette[0]
        else:
            return dominant_color
