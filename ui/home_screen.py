from .base_screen import BaseScreen

class HomeScreen(BaseScreen):
    """
    Etherea’s main home screen.
    """

    def __init__(self):
        super().__init__("Home Screen")

    def render(self):
        return "Rendering Etherea Home Screen 🔮 vruuu"
