from .base_template import BaseTemplate

class ChatTemplate(BaseTemplate):
    """
    Template for chat screens.
    """

    def __init__(self):
        super().__init__("Chat")

    def render(self):
        return "Rendering Etherea Chat UI vruuu 💬"
