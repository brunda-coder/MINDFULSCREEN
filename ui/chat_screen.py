from .base_screen import BaseScreen

class ChatScreen(BaseScreen):
    """
    Chat interface UI.
    """

    def __init__(self):
        super().__init__("Chat Screen")

    def render(self):
        return "Rendering Etherea Chat UI 💬 vruuu"
