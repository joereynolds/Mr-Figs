class FadeOut():
    """
    Fades out an element. This class should be passed 
    through to the component that requires fading

    Thanks to pyroller for implementation details:
    repo: https://github.com/iminurnamez/pyroller/
    file: flair_pieces.py
    """

    def __init__(self,surface, fade_speed=0.1):
        self.parent_surface = surface
        self.alpha = self.parent_surface.get_alpha()
        self.faded= False

    def update(self, delta_time):
        """
        Gradually increment the alpha value of the parent's
        surface.
        Once we're fully faded out, we're finished
        """
        self.alpha = min(self.alpha + self.fade_speed * delta_time, 255)
        if self.alpha == 255:
            self.faded = True
        self.parent_surface.set_alpha(self.alpha)    

