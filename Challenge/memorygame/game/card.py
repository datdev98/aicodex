class Card:
    def __init__(self, name, image_url):
        self.name = name
        self.image_url = image_url
        self.is_face_up = False
        self.is_matched = False

    def flip(self):
        self.is_face_up = not self.is_face_up