from .base_template import BaseTemplate

class DashboardTemplate(BaseTemplate):
    """
    Template for the main Etherea dashboard screen.
    """

    def __init__(self):
        super().__init__("Dashboard")

    def render(self):
        return "Rendering Etherea dashboard vruuu ⚡"
