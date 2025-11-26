class BaseScreen:
    """
    Base class for all screens.
    """

    def __init__(self, title):
        self.title = title

    def render(self):
        return f"Rendering screen: {self.title} vruuu 🌀"
