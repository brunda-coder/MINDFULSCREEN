class BaseTemplate:
    """
    A reusable base template for UI screens and system modules.
    """

    def __init__(self, name):
        self.name = name
        self.data = {}

    def render(self):
        return f"Rendering template: {self.name} vruuu 🌀"

    def load_data(self, data):
        self.data = data
